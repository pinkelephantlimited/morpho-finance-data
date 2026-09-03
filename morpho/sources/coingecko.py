"""
CoinGecko Cryptocurrency Data
Source: https://www.coingecko.com/api/documentation
Auth: None (public API)
"""

import pandas as pd
import requests
from typing import Optional


BASE_URL = "https://api.coingecko.com/api/v3"


def fetch_crypto(
    vs_currency: str = "usd",
    per_page: int = 100,
    page: int = 1,
) -> pd.DataFrame:
    """
    Fetch cryptocurrency market data from CoinGecko.

    Args:
        vs_currency: Currency for prices (e.g., "usd", "eur", "btc")
        per_page: Results per page (max 250)
        page: Page number

    Returns:
        DataFrame with crypto market data

    Example:
        >>> df = fetch_crypto()
        >>> print(df.head())
    """
    url = f"{BASE_URL}/coins/markets"
    params = {
        "vs_currency": vs_currency,
        "order": "market_cap_desc",
        "per_page": min(per_page, 250),
        "page": page,
        "sparkline": "false",
    }
    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    return pd.DataFrame(response.json())


def fetch_coin_history(
    coin_id: str,
    date: str,
    vs_currency: str = "usd",
) -> pd.DataFrame:
    """
    Fetch historical price data for a specific coin.

    Args:
        coin_id: CoinGecko coin ID (e.g., "bitcoin")
        date: Date in DD-MM-YYYY format
        vs_currency: Currency for prices

    Returns:
        DataFrame with historical data
    """
    url = f"{BASE_URL}/coins/{coin_id}/history"
    params = {"date": date, "localization": "false"}
    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    data = response.json()

    market_data = data.get("market_data", {})
    return pd.DataFrame({
        "coin": [coin_id],
        "date": [date],
        "price": [market_data.get("current_price", {}).get(vs_currency)],
        "market_cap": [market_data.get("market_cap", {}).get(vs_currency)],
        "volume": [market_data.get("total_volume", {}).get(vs_currency)],
    })


def fetch_global() -> pd.DataFrame:
    """
    Fetch global cryptocurrency market overview.

    Returns:
        DataFrame with global crypto stats
    """
    url = f"{BASE_URL}/global"
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    data = response.json().get("data", {})
    return pd.DataFrame([data])
