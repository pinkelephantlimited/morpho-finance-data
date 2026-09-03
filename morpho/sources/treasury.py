"""
US Treasury Yield Data
Source: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/
Auth: None
"""

import pandas as pd
import requests
from typing import Optional


def fetch_yields(
    period: str = "daily",
    year: Optional[int] = None,
) -> pd.DataFrame:
    """
    Fetch US Treasury yields across all maturities.

    Args:
        period: 'daily', 'monthly', or 'weekly'
        year: Specific year (None = current year)

    Returns:
        DataFrame with columns: Date, 1 Mo, 2 Mo, 3 Mo, 4 Mo, 6 Mo,
        1 Yr, 2 Yr, 3 Yr, 5 Yr, 7 Yr, 10 Yr, 20 Yr, 30 Yr

    Example:
        >>> df = fetch_yields()
        >>> print(df.tail())
    """
    import datetime

    if year is None:
        year = datetime.datetime.now().year

    urls = {
        "daily": f"https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/{year}/all?type=daily_treasury_yield_curve&field_tdr_date_value={year}&page&_format=csv",
        "monthly": f"https://home.treasury.gov/resource-center/data-chart-center/interest-rates/monthly-treasury-rates.csv/{year}/all?type=monthly_treasury_yield_curve&field_tdr_date_value={year}&page&_format=csv",
        "weekly": f"https://home.treasury.gov/resource-center/data-chart-center/interest-rates/weekly-treasury-rates.csv/{year}/all?type=weekly_treasury_yield_curve&field_tdr_date_value={year}&page&_format=csv",
    }

    url = urls.get(period)
    if not url:
        raise ValueError(f"Invalid period: {period}. Use 'daily', 'monthly', or 'weekly'.")

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    df = pd.read_csv(pd.io.common.StringIO(response.text))
    df.columns = df.columns.str.strip()
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date").reset_index(drop=True)
    return df
