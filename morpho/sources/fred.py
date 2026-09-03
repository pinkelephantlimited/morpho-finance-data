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

    # Find the date column (could be "DATE", "observation_date", etc.)
    date_col = [c for c in df.columns if "date" in c.lower()]
    if date_col:
        df[date_col[0]] = pd.to_datetime(df[date_col[0]])
        df = df.sort_values(date_col[0]).reset_index(drop=True)

    df = df.replace(".", None)
    # Convert numeric columns
    for col in df.columns:
        if col != date_col[0] if date_col else True:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


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
