"""
Example: SEC EDGAR Company Financials

Fetches XBRL data for Apple Inc.
"""

import sys
sys.path.insert(0, "..")

from morpho.sources.sec import fetch_xbrl, search_filings


def main():
    # Search for Apple filings
    print("Searching SEC EDGAR for Apple...")
    filings = search_filings("Apple", form="10-K", limit=5)
    print(f"\nRecent 10-K filings:")
    print(filings)

    # Fetch XBRL facts for Apple (CIK: 0000320193)
    print("\nFetching XBRL facts for Apple...")
    facts = fetch_xbrl("0000320193")
    print(f"\nTotal facts: {len(facts)}")
    print(f"Unique concepts: {facts['concept'].nunique()}")
    print("\nSample data:")
    print(facts.head())


if __name__ == "__main__":
    main()
