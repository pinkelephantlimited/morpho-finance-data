"""
SEC EDGAR XBRL Financial Data
Source: https://data.sec.gov/api/xbrl/companyfacts/
Auth: None (User-Agent header required)
"""

import pandas as pd
import requests
from typing import Optional


HEADERS = {
    "User-Agent": "MorphoFinanceData/0.1 (contact@morpho-finance.dev)",
    "Accept": "application/json",
}


def fetch_xbrl(cik: str, concept: Optional[str] = None) -> pd.DataFrame:
    """
    Fetch all XBRL financial facts for a company.

    Args:
        cik: CIK number (e.g., "0000320193" for Apple)
        concept: Specific XBRL concept (e.g., "us-gaap:Revenues")

    Returns:
        DataFrame with financial facts

    Example:
        >>> df = fetch_xbrl("0000320193")
        >>> print(df.head())
    """
    cik = cik.strip().zfill(10)
    url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"

    response = requests.get(url, headers=HEADERS, timeout=30)
    response.raise_for_status()
    data = response.json()

    records = []
    facts = data.get("facts", {})
    for taxonomy in facts.values():
        for concept_name, concept_data in taxonomy.items():
            units = concept_data.get("units", {})
            for unit_key, entries in units.items():
                for entry in entries:
                    records.append({
                        "concept": concept_name,
                        "unit": unit_key,
                        "value": entry.get("val"),
                        "start_date": entry.get("start"),
                        "end_date": entry.get("end"),
                        "form": entry.get("form"),
                        "filed": entry.get("filed"),
                    })

    df = pd.DataFrame(records)
    if concept:
        df = df[df["concept"] == concept]
    return df


def search_filings(
    company: str,
    form: Optional[str] = None,
    limit: int = 10,
) -> pd.DataFrame:
    """
    Search SEC EDGAR for company filings.

    Args:
        company: Company name or ticker
        form: Form type filter (e.g., "10-K", "10-Q", "8-K")
        limit: Max results

    Returns:
        DataFrame with filing metadata

    Example:
        >>> df = search_filings("Apple", form="10-K")
        >>> print(df.head())
    """
    # First get company tickers
    tickers_url = "https://www.sec.gov/files/company_tickers.json"
    resp = requests.get(tickers_url, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    tickers = resp.json()

    # Find matching company
    cik = None
    for entry in tickers.values():
        if company.upper() in str(entry).upper():
            cik = str(entry.get("cik_str", "")).zfill(10)
            break

    if not cik:
        raise ValueError(f"Company not found: {company}")

    # Fetch submissions
    url = f"https://data.sec.gov/submissions/CIK{cik}.json"
    resp = requests.get(url, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    data = resp.json()

    recent = data.get("filings", {}).get("recent", {})
    df = pd.DataFrame({
        "form": recent.get("form", []),
        "filing_date": recent.get("filingDate", []),
        "accession": recent.get("accessionNumber", []),
        "primary_doc": recent.get("primaryDocument", []),
    })

    if form:
        df = df[df["form"].str.upper() == form.upper()]
    return df.head(limit).reset_index(drop=True)
