"""
US Energy Information Administration (EIA) Open Data
Source: https://www.eia.gov/opendata/
Auth: None (API key optional for higher limits)
"""

import pandas as pd
import requests


BASE_URL = "https://api.eia.gov/v2"


def fetch_energy(
    frequency: str = "annual",
    data: list = None,
   facets: dict = None,
    start: str = "2000",
    end: str = None,
) -> pd.DataFrame:
    """
    Fetch US energy data from EIA.

    Args:
        frequency: 'annual', 'monthly', 'weekly', 'daily'
        data: Data columns to fetch
        facets: Filter facets (e.g., {"fueltype": ["ELC"]})
        start: Start year
        end: End year

    Returns:
        DataFrame with energy data

    Example:
        >>> df = fetch_energy(frequency="monthly", data=["value"])
        >>> print(df.head())
    """
    if data is None:
        data = ["value"]

    url = f"{BASE_URL}/electricity/rto/fuel-type-data/data/"
    params = {
        "frequency": frequency,
        "data[0]": "value",
        "start": start,
        "facets[fueltype][]": "SUN",
        "api_key": "DEMO_KEY",
        "length": "5000",
    }

    response = requests.get(url, params=params, timeout=60)
    response.raise_for_status()
    data = response.json()

    records = data.get("response", {}).get("data", [])
    return pd.DataFrame(records)
