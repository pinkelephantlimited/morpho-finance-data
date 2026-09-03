"""
CFTC Commitments of Traders Data
Source: https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm
Auth: None
"""

import pandas as pd
import requests
from io import StringIO
from typing import Optional


def fetch_cot(
    report_type: str = "legacy",
    commodity: Optional[str] = None,
) -> pd.DataFrame:
    """
    Fetch CFTC Commitments of Traders data.

    Args:
        report_type: 'legacy', 'disaggregated', 'financial', or 'supplementary'
        commodity: Filter by commodity code (e.g., "01" for wheat)

    Returns:
        DataFrame with COT positioning data

    Example:
        >>> df = fetch_cot()
        >>> print(df.head())
    """
    urls = {
        "legacy": "https://www.cftc.gov/dea/newcot/FinFutWk.txt",
        "disaggregated": "https://www.cftc.gov/dea/newcot/disaggfutures.htm",
        "financial": "https://www.cftc.gov/dea/newcot/financial_lf.txt",
        "supplementary": "https://www.cftc.gov/dea/newcot/DeaFinFut.htm",
    }

    url = urls.get(report_type)
    if not url:
        raise ValueError(f"Invalid report_type: {report_type}")

    response = requests.get(url, timeout=60)
    response.raise_for_status()

    # Handle different formats
    if url.endswith(".txt"):
        # Fixed-width format
        df = pd.read_fwf(StringIO(response.text), encoding="latin-1")
    else:
        # HTML format
        tables = pd.read_html(StringIO(response.text))
        df = tables[0] if tables else pd.DataFrame()

    df.columns = df.columns.str.strip()

    if commodity:
        # Filter by MOC code if available
        if "Market_and_Exchange_Names" in df.columns:
            df = df[df["Market_and_Exchange_Names"].str.contains(commodity, case=False, na=False)]

    return df
