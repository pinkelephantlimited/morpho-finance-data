"""
Example: US Treasury Yields Analysis

Fetches daily Treasury yields and visualizes the yield curve.
"""

import sys
sys.path.insert(0, "..")

from morpho.sources.treasury import fetch_yields


def main():
    # Fetch daily yields for current year
    print("Fetching US Treasury yields...")
    df = fetch_yields(period="daily")

    # Display basic info
    print(f"\nDataset shape: {df.shape}")
    print(f"Date range: {df['Date'].min()} to {df['Date'].max()}")
    print(f"\nColumns: {list(df.columns)}")

    # Show last 5 rows
    print("\nLatest yields:")
    print(df.tail())

    # Summary statistics
    print("\nSummary statistics:")
    print(df.describe())


if __name__ == "__main__":
    main()
