# Morpho Finance Data

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Downloads](https://img.shields.io/pypi/dm/morpho-finance-data)](https://pypi.org/project/morpho-finance-data/)

> **50+ truly free financial data sources. No API keys. No registration. No restrictions.**

A curated, open-source collection of **free financial data sources** from around the globe. Every source can be accessed immediately with standard HTTP requests — no signup, no paywall, no rate limit abuse.

Perfect for: researchers, quants, analysts, data scientists, and developers building financial applications.

---

## Quick Start

```python
from morpho import Treasury, Zillow, SEC, CoinGecko, FRED

# US Treasury yields (all maturities, no auth)
df = Treasury.yields()
print(df.head())

# Zillow housing data (ZIP-level)
df = Zillow.zhvi()
print(df.head())

# SEC EDGAR company filings
filings = SEC.search("Apple", form="10-K")
print(filings.head())

# FRED time series (no API key needed)
df = FRED.series("DGS10")
print(df.tail())

# Crypto prices
df = CoinGecko.crypto(per_page=10)
print(df[['id', 'current_price', 'market_cap']].head())
```

---

## Data Catalog

### Fixed Income & Rates

| Source | Region | Description | Access |
|--------|--------|-------------|--------|
| [US Treasury Daily Rates](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/) | US | All maturities, daily since 1990 | CSV (no auth) |
| [FRED Series](https://fred.stlouisfed.org/) | US | 800K+ economic time series, direct CSV | CSV (no auth) |
| [CFTC Commitments of Traders](https://www.cftc.gov/dea/newcot/FinFutWk.txt) | US | Futures positioning data, weekly | TXT (no auth) |
| [CBOE Options](https://www.cboe.com/) | US | Options chains with Greeks, delayed | JSON (no auth) |

### Real Estate

| Source | Region | Description | Access |
|--------|--------|-------------|--------|
| [Zillow ZHVI](https://files.zillowstatic.com/research/public_csvs/zhvi/) | US | Home Value Index (26K ZIPs, monthly) | CSV (no auth) |
| [Zillow ZORI](https://files.zillowstatic.com/research/public_csvs/zori/) | US | Observed Rent Index | CSV (no auth) |
| [Zillow Inventory](https://files.zillowstatic.com/research/public_csvs/inventory/) | US | For-sale inventory | CSV (no auth) |

### Insurance

| Source | Region | Description | Access |
|--------|--------|-------------|--------|
| [OpenFEMA NFIP Policies](https://www.fema.gov/openfema-data-page/fima-nfip-redacted-policies-v2) | US | 73M+ flood insurance policy records | API/CSV (no auth) |
| [OpenFEMA NFIP Claims](https://www.fema.gov/openfema-data-page/fima-nfip-redacted-claims-v2) | US | Flood insurance claims data | API/CSV (no auth) |
| [FEMA Disaster Declarations](https://www.fema.gov/openfema-data-page/disaster-declarations-datasets-v2) | US | All disaster declarations since 1953 | API/CSV (no auth) |

### Banking & Lending

| Source | Region | Description | Access |
|--------|--------|-------------|--------|
| [FDIC Bank Find](https://www.fdic.gov/about/open-data-fdic) | US | All FDIC-insured institutions, branch locations | API/CSV (no auth) |
| [FDIC Summary of Deposits](https://www.fdic.gov/about/open-data-fdic) | US | Branch-level deposit data | API/CSV (no auth) |
| [Federal Reserve H.8](https://www.federalreserve.gov/releases/h8/) | US | Commercial bank balance sheets | CSV (no auth) |
| [Federal Reserve Z.1](https://www.federalreserve.gov/releases/z1/) | US | Financial accounts (flow of funds) | CSV (no auth) |

### Crypto

| Source | Region | Description | Access |
|--------|--------|-------------|--------|
| [CoinGecko](https://www.coingecko.com/api/documentation) | Global | Prices, market cap, volume, historical | REST (no auth) |

### Macro & Economic

| Source | Region | Description | Access |
|--------|--------|-------------|--------|
| [World Bank Open Data](https://data.worldbank.org/) | Global | 1400+ indicators, 217 countries | CSV/API (no auth) |
| [IMF Data](https://data.imf.org/) | Global | WEO, BOP, IFS, Government Finance | API/CSV (no auth) |
| [OECD Data](https://data.oecd.org/) | OECD | GDP, trade, employment, inflation | CSV/API (no auth) |
| [BIS Statistics](https://data.bis.gov/) | Global | Banking, payments, FX reserves | API (no auth) |
| [ECB SDW](https://sdw.ecb.europa.eu/) | Euro | Monetary & financial data | API (no auth) |
| [SEC EDGAR XBRL](https://data.sec.gov/api/xbrl/companyfacts/) | US | All public company financials | REST (no auth) |

---

## Project Structure

```
morpho-finance-data/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── setup.py
├── morpho/
│   ├── __init__.py
│   └── sources/
│       ├── __init__.py
│       ├── sec.py           # SEC EDGAR XBRL + filings
│       ├── treasury.py      # US Treasury yields
│       ├── fred.py          # FRED time series (no key)
│       ├── zillow.py        # Zillow ZHVI/ZORI
│       ├── fema.py          # FEMA flood insurance + disasters
│       ├── fdic.py          # FDIC banks + deposits
│       ├── eia.py           # US energy data
│       ├── worldbank.py     # World Bank indicators
│       ├── imf.py           # IMF WEO + commodity prices
│       ├── coingecko.py     # Crypto market data
│       ├── cftc.py          # CFTC COT reports
│       ├── oecd.py          # OECD statistics
│       ├── bis.py           # BIS banking stats
│       ├── federal_reserve.py  # H.8 + Z.1 data
│       ├── cboe.py          # CBOE options chains
│       └── ecb.py           # ECB SDW data
├── examples/
│   ├── 01_treasury_yields.py
│   ├── 02_housing_analysis.py
│   └── 03_sec_filings.py
├── scripts/
│   └── fetch_all.py
├── tests/
│   └── test_sources.py
└── .gitignore
```

## Installation

```bash
pip install morpho-finance-data
```

Or install from source:

```bash
git clone https://github.com/pinkelephantlimited/morpho-finance-data.git
cd morpho-finance-data
pip install -e .
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. All sources must be:
- **Truly free**: No registration, no API key, no paywall
- **Publicly accessible**: Direct HTTP endpoint (CSV, JSON, XML)
- **Reproducible**: Include example usage and data format

## License

[MIT](LICENSE)
