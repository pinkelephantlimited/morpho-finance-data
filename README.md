# Morpho Finance Data

A comprehensive collection of **free, real-world financial data sources** from around the globe. Curated for researchers, analysts, quants, and developers building financial applications.

## Data Sources

### US Markets

| Source | Description | Asset Classes | Access |
|--------|-------------|---------------|--------|
| [SEC EDGAR](https://www.sec.gov/edgar) | Company filings (10-K, 10-Q, 8-K, etc.) | Equities, ETFs | API |
| [FRED](https://fred.stlouisfed.org/) | 800k+ US economic time series | Macro, Rates, employment | API |
| [Yahoo Finance](https://finance.yahoo.com/) | Historical prices, dividends, splits | Equities, ETFs, Indices | API |
| [Alpha Vantage](https://www.alphavantage.co/) | Realtime & historical market data | Equities, Forex, Crypto | API |
| [IEX Cloud](https://iexcloud.io/) | Realtime market data | Equities, ETFs | API |
| [Quandl (Nasdaq)](https://www.nasdaq.com/market-activity/data) | Financial & alternative datasets | Multi-asset | API |
| [US Treasury](https://home.treasury.gov/) | Yield curves, rates, auctions | Fixed Income, Rates | CSV |
| [FDIC](https://www.fdic.gov/bank-failures) | Bank failure data, financial institution info | Banking | API |
| [Federal Reserve](https://www.federalreserve.gov/data.htm) | Banking data, H.8, Z.1 | Banking, Macro | CSV |
| [CFTC](https://www.cftc.gov/MarketReports/CommitmentofTraders/index.htm) | Commitments of Traders reports | Futures, Options | CSV |
| [Nasdaq Data Link](https://data.nasdaq.com/) | Aggregated financial datasets | Multi-asset | API |

### European Markets

| Source | Description | Asset Classes | Access |
|--------|-------------|---------------|--------|
| [ECB Statistical Data Warehouse](https://sdw.ecb.europa.eu/) | Euro area monetary & financial data | Rates, Macro, FX | API |
| [Euronext](https://live.euronext.com/) | Official prices, volumes, trading data | Equities, Bonds, Derivatives | CSV |
| [Deutsche Bundesbank](https://www.bundesbank.de/en) | German financial statistics | Rates, Macro | API |
| [Banque de France](https://www.banque-france.fr/en/statistics) | French financial statistics | Rates, Macro | API |
| [OpenFIGI](https://openfigi.com/) | Bloomberg-sourced security identifiers | Equities, Bonds, Funds | API |

### Asia-Pacific

| Source | Description | Asset Classes | Access |
|--------|-------------|---------------|--------|
| [Bank of Japan](https://www.boj.or.jp/en/statistics/) | Japanese financial statistics | Rates, Macro | API |
| [Reserve Bank of Australia](https://www.rba.gov.au/statistics/) | Australian financial data | Rates, Macro | CSV |
| [Singapore Exchange](https://www.sgx.com/securities) | SGX market data | Equities, Derivatives | CSV |
| [NSE India](https://www.nseindia.com/market-data) | National Stock Exchange data | Equities, Derivatives | API |

### Global / Multi-Region

| Source | Description | Asset Classes | Access |
|--------|-------------|---------------|--------|
| [World Bank Open Data](https://data.worldbank.org/) | Development indicators, GDP, inflation | Macro, ESG | API |
| [IMF Data](https://data.imf.org/) | International financial statistics | Macro, Rates, Trade | API |
| [BIS Statistics](https://data.bis.gov/) | Banking, payments, FX reserves | Banking, Rates | API |
| [Open Exchange Rates](https://openexchangerates.org/) | 170+ currency exchange rates | FX | API |
| [CoinGecko](https://www.coingecko.com/) | Cryptocurrency market data | Crypto | API |
| [CoinMarketCap](https://coinmarketcap.com/) | Crypto prices, market cap, volume | Crypto | API |
| [Commodity Prices](https://www.imf.org/en/Research/commodity-prices) | IMF primary commodity prices | Commodities | CSV |

### Alternative & ESG

| Source | Description | Asset Classes | Access |
|--------|-------------|---------------|--------|
| [SEC XBRL](https://www.sec.gov/edgar/company-and-rss-feeds) | Structured financial filings | Equities | API |
| [Quandl NLP](https://www.quandl.com/) | News sentiment, NLP datasets | Alternative | API |
| [GDELT](https://www.gdeltproject.org/) | Global news events, sentiment | Alternative | API |
| [SASB](https://www.sasb.org/) | Sustainability accounting standards | ESG | CSV |
| [Trucost (S&P)](https://www.spglobal.com/esg/indices/) | Environmental data | ESG | API |
| [MSCI ESG](https://www.msci.com/esg-ratings) | ESG ratings & research | ESG | API |

### Fixed Income & Rates

| Source | Description | Asset Classes | Access |
|--------|-------------|---------------|--------|
| [Treasury.gov](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/) | Daily Treasury rates | Fixed Income | CSV |
| [FRED - Treasury Yields](https://fred.stlouisfed.org/series/DGS10) | US Treasury yields | Fixed Income | API |
| [European Bond Yields](https://www.worldgovernmentbonds.com/) | Government bond yields | Fixed Income | CSV |

### Commodities & Energy

| Source | Description | Asset Classes | Access |
|--------|-------------|---------------|--------|
| [EIA](https://www.eia.gov/opendata/) | US energy data, oil, gas, electricity | Commodities | API |
| [World Gold Council](https://www.gold.org/goldhub/data) | Gold prices, demand, supply | Commodities | CSV |
| [LME](https://www.lme.com/Metals) | London Metal Exchange prices | Commodities | CSV |

## Quick Start

```python
import pandas as pd
import requests

# Example: Fetch US Treasury yield curve from FRED
fred_url = "https://api.stlouisfed.org/fred/series/observations"
params = {
    "series_id": "DGS10",
    "api_key": "YOUR_API_KEY",
    "file_type": "json"
}
response = requests.get(fred_url, params=params)
data = response.json()
```

## Contributing

Contributions welcome! Please add new free data sources to the appropriate category.

## License

MIT
