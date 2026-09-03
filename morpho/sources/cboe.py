"""
CBOE Options Data
Source: https://www.cboe.com/
Auth: None (delayed data)
"""

import pandas as pd
import requests


def fetch_options_chain(symbol: str) -> pd.DataFrame:
    """
    Fetch delayed options chain for a symbol from CBOE CDN.

    Args:
        symbol: Stock symbol (e.g., "AAPL", "SPY")

    Returns:
        DataFrame with options chain data

    Example:
        >>> df = fetch_options_chain("SPY")
        >>> print(df.head())
    """
    url = f"https://cdn.cboe.com/api/global/delayed_quotes/options/{symbol.upper()}.json"
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    data = response.json()

    records = []
    options = data.get("data", {}).get("options", [])
    for option in options:
        records.append({
            "option": option.get("option"),
            "bid": option.get("bid"),
            "ask": option.get("ask"),
            "mid": option.get("midpoint"),
            "volume": option.get("volume"),
            "open_interest": option.get("open_interest"),
            "volatility": option.get("volatility"),
            "delta": option.get("delta"),
            "gamma": option.get("gamma"),
            "theta": option.get("theta"),
            "vega": option.get("vega"),
            "rho": option.get("rho"),
        })

    return pd.DataFrame(records)
