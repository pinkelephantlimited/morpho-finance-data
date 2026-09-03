"""
FRED (Federal Reserve Economic Data) - No API Key Required
Source: https://fred.stlouisfed.org/
Auth: None (direct CSV download)
"""

import pandas as pd
import requests
from typing import Optional


def fetch_series(
    series_id: str,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
) -> pd.DataFrame:
    """
    Fetch a FRED time series via direct CSV download (no API key needed).

    Args:
        series_id: Series ID (e.g., "DGS10" for 10-year Treasury yield)
        start_date: Start date (YYYY-MM-DD)
        end_date: End date (YYYY-MM-DD)

    Returns:
        DataFrame with date and value columns

    Example:
        >>> df = fetch_series("DGS10")
        >>> print(df.tail())
    """
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv"
    params = {"id": series_id}
    if start_date:
        params["cosd"] = start_date
    if end_date:
        params["coed"] = end_date

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()

    from io import StringIO
    df = pd.read_csv(StringIO(response.text))
    df.columns = df.columns.str.strip()
    df["DATE"] = pd.to_datetime(df["DATE"])
    df = df.replace(".", None)
    df.iloc[:, 1] = pd.to_numeric(df.iloc[:, 1], errors="coerce")
    return df.sort_values("DATE").reset_index(drop=True)


# Common series shortcuts
SERIES = {
    "DGS10": "10-Year Treasury Yield",
    "DGS2": "2-Year Treasury Yield",
    "DGS30": "30-Year Treasury Yield",
    "DFF": "Federal Funds Rate",
    "UNRATE": "Unemployment Rate",
    "CPIAUCSL": "CPI (All Urban Consumers)",
    "GDP": "Gross Domestic Product",
    "FEDFUNDS": "Federal Funds Effective Rate",
    "T10Y2Y": "10Y-2Y Treasury Spread",
    "T10Y3M": "10Y-3M Treasury Spread",
    "VIXCLS": "VIX Close",
}
