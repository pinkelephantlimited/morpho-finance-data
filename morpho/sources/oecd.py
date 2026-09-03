"""
OECD Data
Source: https://data.oecd.org/
Auth: None
"""

import pandas as pd
import requests
from typing import Optional


BASE_URL = "https://sdmx.oecd.org/public/rest"


def fetch_indicator(
    indicator: str = "B1GQ",
    country: Optional[str] = None,
    start_year: int = 2000,
    end_year: int = 2024,
) -> pd.DataFrame:
    """
    Fetch OECD indicator data.

    Args:
        indicator: Indicator code (e.g., "B1GQ" for GDP)
        country: Country code (e.g., "USA", "GBR")
        start_year: Start year
        end_year: End year

    Returns:
        DataFrame with OECD data

    Example:
        >>> df = fetch_indicator("B1GQ", country="USA")
        >>> print(df.head())
    """
    url = f"{BASE_URL}/data/DSD_NAMAIN1@DF_TABLE1"
    params = {
        "startPeriod": str(start_year),
        "endPeriod": str(end_year),
    }
    if country:
        params["c[REF_AREA]"] = country

    headers = {"Accept": "application/vnd.sdmx.data+csv"}
    response = requests.get(url, params=params, headers=headers, timeout=30)
    response.raise_for_status()

    from io import StringIO
    df = pd.read_csv(StringIO(response.text))
    return df
