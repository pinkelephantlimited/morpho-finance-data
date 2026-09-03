"""
Zillow Housing Market Data
Source: https://files.zillowstatic.com/research/public_csvs/
Auth: None
"""

import pandas as pd
import requests
from typing import Optional


ZHVI_URL = "https://files.zillowstatic.com/research/public_csvs/zhvi/Metro_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_monthly.csv"
ZORI_URL = "https://files.zillowstatic.com/research/public_csvs/zori/Metro_ZORI_AllHomesPlusMultifamily_SSA.csv"
INVENTORY_URL = "https://files.zillowstatic.com/research/public_csvs/inventory/Metro_invt_fs_uc_sfrcondo_sm_month.csv"


def fetch_zhvi(region: Optional[str] = None) -> pd.DataFrame:
    """
    Fetch Zillow Home Value Index (ZHVI).

    Args:
        region: Filter by region name (e.g., "Manhattan", "San Francisco")

    Returns:
        DataFrame with home values by region over time

    Example:
        >>> df = fetch_zhvi()
        >>> print(df.tail())
    """
    df = pd.read_csv(ZHVI_URL, storage_options=None)
    df.columns = df.columns.str.strip()
    if region:
        df = df[df["RegionName"].str.contains(region, case=False, na=False)]
    return df


def fetch_zori(region: Optional[str] = None) -> pd.DataFrame:
    """
    Fetch Zillow Observed Rent Index (ZORI).

    Args:
        region: Filter by region name

    Returns:
        DataFrame with rent index by region over time
    """
    df = pd.read_csv(ZORI_URL)
    df.columns = df.columns.str.strip()
    if region:
        df = df[df["RegionName"].str.contains(region, case=False, na=False)]
    return df


def fetch_inventory(region: Optional[str] = None) -> pd.DataFrame:
    """
    Fetch Zillow housing inventory data.

    Args:
        region: Filter by region name

    Returns:
        DataFrame with for-sale inventory by region
    """
    df = pd.read_csv(INVENTORY_URL)
    df.columns = df.columns.str.strip()
    if region:
        df = df[df["RegionName"].str.contains(region, case=False, na=False)]
    return df
