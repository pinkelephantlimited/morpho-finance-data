"""
Federal Reserve Bank Data
Source: https://www.federalreserve.gov/data.htm
Auth: None
"""

import pandas as pd
import requests
from typing import Optional


def fetch_h8() -> pd.DataFrame:
    """
    Fetch H.8 Assets and Liabilities of Commercial Banks data.

    Returns:
        DataFrame with bank balance sheet data
    """
    url = "https://www.federalreserve.gov/releases/h8/Current/h8.csv"
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    from io import StringIO
    df = pd.read_csv(StringIO(response.text))
    df.columns = df.columns.str.strip()
    return df


def fetch_z1() -> pd.DataFrame:
    """
    Fetch Z.1 Financial Accounts (Flow of Funds) data.

    Returns:
        DataFrame with financial flow data
    """
    url = "https://www.federalreserve.gov/releases/z1/datadownload/z1_csv.zip"
    response = requests.get(url, timeout=60)
    response.raise_for_status()

    import zipfile
    import io
    with zipfile.ZipFile(io.BytesIO(response.content)) as zf:
        csv_files = [f for f in zf.namelist() if f.endswith('.csv')]
        if csv_files:
            with zf.open(csv_files[0]) as f:
                return pd.read_csv(f)
    return pd.DataFrame()
