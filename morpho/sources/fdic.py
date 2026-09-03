"""
FDIC Bank & Deposit Data
Source: https://www.fdic.gov/about/open-data-fdic
Auth: None
"""

import pandas as pd
import requests


BASE_URL = "https://www.fdic.gov/bank-failures/failed-bank-list/bulk_data.json"


def fetch_banks() -> pd.DataFrame:
    """
    Fetch list of FDIC-insured banks.

    Returns:
        DataFrame with bank information

    Example:
        >>> df = fetch_banks()
        >>> print(df.head())
    """
    url = "https://www.fdic.gov/bank-failures/failed-bank-list/bulk_data.json"
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    data = response.json()
    return pd.DataFrame(data)


def fetch_deposits() -> pd.DataFrame:
    """
    Fetch FDIC Summary of Deposits data.

    Returns:
        DataFrame with branch-level deposit data
    """
    url = "https://www.fdic.gov/analysis/sod/sodDownloadAllSvc.asp"
    response = requests.get(url, timeout=120)
    response.raise_for_status()

    from io import StringIO
    return pd.read_csv(StringIO(response.text))
