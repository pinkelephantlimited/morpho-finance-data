"""
Bank for International Settlements (BIS) Statistics
Source: https://data.bis.gov/
Auth: None
"""

import pandas as pd
import requests
from typing import Optional


BASE_URL = "https://data.bis.gov/api/xkDimensions/children"


def fetch_reserve_data() -> pd.DataFrame:
    """
    Fetch BIS reserve currency data.

    Returns:
        DataFrame with central bank reserve holdings
    """
    url = "https://data.bis.gov/api/data/BIS.LBP.LUB.1._Z.1.00.1.00.D.SD"
    headers = {"Accept": "application/vnd.sdmx.data+csv"}

    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        from io import StringIO
        return pd.read_csv(StringIO(response.text))
    except Exception:
        # Fallback: return empty DataFrame if API unavailable
        return pd.DataFrame()


def fetch_credit_to_gdp() -> pd.DataFrame:
    """
    Fetch BIS credit-to-GDP gap data.

    Returns:
        DataFrame with credit gap indicators
    """
    url = "https://data.bis.org/api/data/BIS.AM.CRE.GDP.Z.S.Z.00.Z"
    headers = {"Accept": "application/vnd.sdmx.data+csv"}

    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        from io import StringIO
        return pd.read_csv(StringIO(response.text))
    except Exception:
        return pd.DataFrame()
