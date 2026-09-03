"""
FEMA Flood Insurance & Disaster Data
Source: https://www.fema.gov/openfema-data-page
Auth: None
"""

import pandas as pd
import requests
from typing import Optional


BASE_URL = "https://www.fema.gov/api/open/v2"


def fetch_nfip_policies(limit: int = 1000) -> pd.DataFrame:
    """
    Fetch FEMA National Flood Insurance Program policy records.

    Args:
        limit: Number of records (max per request)

    Returns:
        DataFrame with policy records

    Example:
        >>> df = fetch_nfip_policies(limit=500)
        >>> print(df.head())
    """
    url = f"{BASE_URL}/FimaNfipPolicies"
    params = {
        "$top": min(limit, 1000),
        "$format": "json",
    }
    response = requests.get(url, params=params, timeout=60)
    response.raise_for_status()
    data = response.json()
    return pd.DataFrame(data.get("data", []))


def fetch_disasters(limit: int = 1000) -> pd.DataFrame:
    """
    Fetch FEMA disaster declarations.

    Args:
        limit: Number of records (max per request)

    Returns:
        DataFrame with disaster declarations

    Example:
        >>> df = fetch_disasters()
        >>> print(df.head())
    """
    url = f"{BASE_URL}/DisasterDeclarationsSummaries"
    params = {
        "$top": min(limit, 1000),
        "$format": "json",
    }
    response = requests.get(url, params=params, timeout=60)
    response.raise_for_status()
    data = response.json()
    return pd.DataFrame(data.get("data", []))


def fetch_nfip_claims(limit: int = 1000) -> pd.DataFrame:
    """
    Fetch FEMA flood insurance claims.

    Args:
        limit: Number of records (max per request)

    Returns:
        DataFrame with claims data
    """
    url = f"{BASE_URL}/FimaNfipClaims"
    params = {
        "$top": min(limit, 1000),
        "$format": "json",
    }
    response = requests.get(url, params=params, timeout=60)
    response.raise_for_status()
    data = response.json()
    return pd.DataFrame(data.get("data", []))
