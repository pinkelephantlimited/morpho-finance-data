"""
Example: Zillow Housing Market Analysis

Fetches ZHVI data and analyzes housing market trends.
"""

import sys
sys.path.insert(0, "..")

from morpho.sources.zillow import fetch_zhvi


def main():
    # Fetch national ZHVI data
    print("Fetching Zillow Home Value Index data...")
    df = fetch_zhvi()

    print(f"\nDataset shape: {df.shape}")
    print(f"Regions: {df['RegionName'].nunique()}")

    # Filter for major metros
    major_metros = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
    filtered = df[df["RegionName"].isin(major_metros)]

    print("\nZHVI for major metros:")
    print(filtered[["RegionName", "SizeRank"]].head())

    # Show all columns
    print(f"\nAll columns: {list(df.columns)}")


if __name__ == "__main__":
    main()
