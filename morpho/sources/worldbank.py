"""
World Bank Open Data
Source: https://data.worldbank.org/
Auth: None
"""

import pandas as pd
import requests
from typing import Optional


BASE_URL = "https://api.worldbank.org/v2"


def fetch_indicators(
    indicator: str = "NY.GDP.MKTP.CD",
    country: str = "all",
    start_year: int = 2000,
    end_year: int = 2024,
) -> pd.DataFrame:
    """
    Fetch World Bank indicator data.

    Args:
        indicator: Indicator code (e.g., "NY.GDP.MKTP.CD" for GDP)
        country: Country code or "all" for all countries
        start_year: Start year
        end_year: End year

    Returns:
        DataFrame with indicator values

    Example:
        >>> df = fetch_indicators("NY.GDP.MKTP.CD")
        >>> print(df.head())
    """
    url = f"{BASE_URL}/country/{country}/indicator/{indicator}"
    params = {
        "date": f"{start_year}:{end_year}",
        "format": "json",
        "per_page": 5000,
    }

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    data = response.json()

    if len(data) < 2:
        return pd.DataFrame()

    records = []
    for item in data[1]:
        records.append({
            "country_id": item.get("country", {}).get("id"),
            "country_name": item.get("country", {}).get("value"),
            "indicator_id": item.get("indicator", {}).get("id"),
            "indicator_name": item.get("indicator", {}).get("value"),
            "date": item.get("date"),
            "value": item.get("value"),
        })

    df = pd.DataFrame(records)
    df["date"] = pd.to_numeric(df["date"])
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    return df.sort_values(["country_name", "date"]).reset_index(drop=True)


def list_indicators(search: Optional[str] = None) -> pd.DataFrame:
    """
    List available World Bank indicators.

    Args:
        search: Search term to filter indicators

    Returns:
        DataFrame with indicator metadata
    """
    url = f"{BASE_URL}/indicator"
    params = {"format": "json", "per_page": 500}
    if search:
        params["q"] = search

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    data = response.json()

    if len(data) < 2:
        return pd.DataFrame()

    return pd.DataFrame(data[1])
