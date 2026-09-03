# Morpho Finance Data

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Downloads](https://img.shields.io/pypi/dm/morpho-finance-data)](https://pypi.org/project/morpho-finance-data/)

> **40+ truly free financial data sources. No API keys. No registration. No restrictions.**

A curated, open-source collection of **free financial data sources** from around the globe. Every source can be accessed immediately with standard HTTP requests — no signup, no paywall, no rate limit abuse.

Perfect for: researchers, quants, analysts, data scientists, and developers building financial applications.

---

## Quick Start

```python
from morpho import Treasury, Zillow, SEC

# US Treasury yields (all maturities, no auth)
df = Treasury.yields()
print(df.head())

# Zillow housing data (ZIP-level)
df = Zillow.zhvi()
print(df.head())

# SEC EDGAR company filings
filings = SEC.search("Apple", form="10-K")
print(filings.head())
```

Or use individual modules directly:

```python
from morpho.sources.treasury import fetch_yields
from morpho.sources.zillow import fetch_zhvi
from morpho.sources.sec import search_filings

df_treasury = fetch_yields()
df_housing = fetch_zhvi()
df_filings = search_filings("Apple", form="10-K")
```

---

## Data Catalog

### Equities

| Source | Region | Description | Access |
|--------|--------|-------------|--------|
| [SEC EDGAR XBRL](https://data.sec.gov/api/xbrl/companyfacts/) | US | All public company financials (10-K, 10-Q, 8-K, XBRL) | REST (no auth) |
| [SEC EDGAR Submissions](https://data.sec.gov/submissions/) | US | Full filing index, all companies | REST (no auth) |
| [CBOE Delayed Quotes](https://cdn.cboe.com/api/global/delayed_quotes/) | US | Options chains with Greeks | JSON (no auth) |
| [World Bank WDI](https://data.worldbank.org/) | Global | GDP, market cap, 1400+ indicators | CSV/API (no auth) |

### Fixed Income & Rates

| Source | Region | Description | Access |
|--------|--------|-------------|--------|
| [US Treasury Daily Rates](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/) | US | All maturities, daily since 1990 | CSV (no auth) |
| [US Treasury Yield Curve](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/) | US | Monthly, weekly, daily yield curves | CSV (no auth) |
| [CFTC Commitments of Traders](https://www.cftc.gov/dea/newcot/FinFutWk.txt) | US | Futures positioning data, weekly | TXT (no auth) |

### Real Estate

| Source | Region | Description | Access |
|--------|--------|-------------|--------|
| [Zillow ZHVI](https://files.zillowstatic.com/research/public_csvs/zhvi/) | US | Home Value Index (26K ZIPs, monthly) | CSV (no auth) |
| [Zillow ZORI](https://files.zillowstatic.com/research/public_csvs/zori/) | US | Observed Rent Index | CSV (no auth) |
| [Zillow Inventory](https://files.zillowstatic.com/research/public_csvs/inventory/) | US | For-sale inventory | CSV (no auth) |
| [FHFA House Price Index](https://www.fhfa.gov/DataTools/Tools/Pages/HPI-Downloader.aspx) | US | Repeat-sales HPI (quarterly, metro/state) | CSV (no auth) |

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
| [HMDA Dataset](https://www.consumerfinance.gov/data-research/) | US | Mortgage lending (4700+ institutions, loan-level) | CSV (no auth) |

### Crypto

| Source | Region | Description | Access |
|--------|--------|-------------|--------|
| [CoinGecko](https://www.coingecko.com/api/documentation) | Global | Prices, market cap, volume, historical | REST (no auth) |
| [CoinMarketCap Historical](https://coinmarketcap.com/api/documentation/v1/) | Global | Historical OHLCV | REST (no auth) |

### Commodities

| Source | Region | Description | Access |
|--------|--------|-------------|--------|
| [EIA Open Data](https://www.eia.gov/opendata/) | US | Oil, gas, electricity, renewables | API (no auth) |
| [IMF Primary Commodity Prices](https://www.imf.org/en/Research/commodity-prices) | Global | Commodity price projections | CSV (no auth) |

### Macro & Economic

| Source | Region | Description | Access |
|--------|--------|-------------|--------|
| [World Bank Open Data](https://data.worldbank.org/) | Global | 1400+ indicators, 217 countries | CSV/API (no auth) |
| [IMF Data](https://data.imf.org/) | Global | WEO, BOP, IFS, Government Finance | API/CSV (no auth) |
| [OECD Data](https://data.oecd.org/) | OECD | GDP, trade, employment, inflation | CSV/API (no auth) |
| [BIS Statistics](https://data.bis.gov/) | Global | Banking, payments, FX reserves | API (no auth) |
| [ECB SDW](https://sdw.ecb.europa.eu/) | Euro | Monetary & financial data | API (no auth) |
| [UN Comtrade](https://comtradeplus.un.org/) | Global | Bilateral trade flows | API (no auth, 500/day) |

### Alternative Data

| Source | Region | Description | Access |
|--------|--------|-------------|--------|
| [GDELT Project](https://www.gdeltproject.org/data.html) | Global | News events, sentiment, 100+ languages | API/CSV (no auth) |

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
│       ├── sec.py
│       ├── treasury.py
│       ├── zillow.py
│       ├── fema.py
│       ├── fdic.py
│       ├── eia.py
│       ├── worldbank.py
│       ├── imf.py
│       ├── bcs.py
│       ├── coingecko.py
│       └── ...
├── scripts/
│   ├── fetch_all.py
│   └── update_cache.py
├── examples/
│   ├── 01_treasury_yields.py
│   ├── 02_housing_analysis.py
│   └── 03_sec_filings.py
├── data/                      # local cache (gitignored)
└── tests/
    └── test_sources.py
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

## Usage Examples

```python
# Fetch all US Treasury yields (no API key needed)
from morpho.sources.treasury import fetch_yields

df = fetch_yields()  # Returns DataFrame with all maturities
print(df.tail())     # Most recent rates
```

```python
# Fetch Zillow home value data by ZIP code
from morpho.sources.zillow import fetch_zhvi

df = fetch_zhvi()
manhattan = df[df["RegionName"].str.contains("Manhattan")]
print(manhattan.head())
```

```python
# Fetch SEC company financials via XBRL
from morpho.sources.sec import fetch_xbrl

facts = fetch_xbrl("AAPL")  # All Apple financial facts
print(facts.head())
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. All sources must be:
- **Truly free**: No registration, no API key, no paywall
- **Publicly accessible**: Direct HTTP endpoint (CSV, JSON, XML)
- **Reproducible**: Include example usage and data format

## License

[MIT](LICENSE)
