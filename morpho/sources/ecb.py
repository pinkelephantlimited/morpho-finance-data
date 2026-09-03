"""
ECB Statistical Data Warehouse
Source: https://sdw.ecb.europa.eu/
Auth: None
"""

import pandas as pd
import requests
from typing import Optional


BASE_URL = "https://data-api.ecb.europa.eu/service/data"


def fetch_series(
    flow_ref: str = "FM",
    key: str = "D.U2.EUR.4F.KR.MRR_FR.LEV",
    start_period: Optional[str] = None,
    end_period: Optional[str] = None,
) -> pd.DataFrame:
    """
    Fetch ECB time series data.

    Args:
        flow_ref: Data flow reference
        key: Series key
        start_period: Start date (YYYY-MM-DD)
        end_period: End date (YYYY-MM-DD)

    Returns:
        DataFrame with ECB data

    Example:
        >>> df = fetch_series(key="D.U2.EUR.4F.KR.MRR_FR.LEV")
        >>> print(df.head())
    """
    url = f"{BASE_URL}/{flow_ref}/{key}"
    params = {"format": "csvdata"}
    if start_period:
        params["startPeriod"] = start_period
    if end_period:
        params["endPeriod"] = end_period

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()

    from io import StringIO
    df = pd.read_csv(StringIO(response.text))
    return df
