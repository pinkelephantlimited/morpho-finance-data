"""
International Monetary Fund (IMF) Data
Source: https://data.imf.org/
Auth: None
"""

import pandas as pd
import requests
from typing import Optional


def fetch_weo(
    country: Optional[str] = None,
    indicator: Optional[str] = None,
) -> pd.DataFrame:
    """
    Fetch IMF World Economic Outlook data.

    Args:
        country: Country code (e.g., "US", "GB", "JP")
        indicator: Indicator code (e.g., "NGDP_RPCH" for GDP growth)

    Returns:
        DataFrame with WEO data

    Example:
        >>> df = fetch_weo(country="US")
        >>> print(df.head())
    """
    url = "https://www.imf.org/external/datamapper/api/v1/WEO"
    params = {"periods": "2020,2021,2022,2023,2024,2025"}
    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    data = response.json()

    records = []
    for indicator_code, indicator_data in data.get("values", {}).items():
        for country_code, country_data in indicator_data.items():
            for period, value in country_data.items():
                records.append({
                    "indicator": indicator_code,
                    "country": country_code,
                    "period": period,
                    "value": value,
                })

    df = pd.DataFrame(records)
    if country:
        df = df[df["country"] == country]
    if indicator:
        df = df[df["indicator"] == indicator]
    return df


def fetch_commodity_prices() -> pd.DataFrame:
    """
    Fetch IMF Primary Commodity Price projections.

    Returns:
        DataFrame with commodity prices
    """
    url = "https://www.imf.org/-/media/Files/Research/CommodityPrices/MPP-NEW.ashx"
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    from io import StringIO
    return pd.read_csv(StringIO(response.text))
