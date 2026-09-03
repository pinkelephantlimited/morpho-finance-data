"""Morpho Finance Data — Free financial data, no restrictions."""

__version__ = "0.1.0"

from morpho.sources.treasury import fetch_yields
from morpho.sources.sec import fetch_xbrl, search_filings
from morpho.sources.zillow import fetch_zhvi, fetch_zori
from morpho.sources.fema import fetch_nfip_policies, fetch_disasters
from morpho.sources.fdic import fetch_banks, fetch_deposits
from morpho.sources.eia import fetch_energy
from morpho.sources.worldbank import fetch_indicators
from morpho.sources.imf import fetch_weo
from morpho.sources.coingecko import fetch_crypto
from morpho.sources.fred import fetch_series as fetch_fred
from morpho.sources.cftc import fetch_cot
from morpho.sources.oecd import fetch_indicator as fetch_oecd
from morpho.sources.bis import fetch_reserve_data, fetch_credit_to_gdp
from morpho.sources.federal_reserve import fetch_h8, fetch_z1
from morpho.sources.cboe import fetch_options_chain
from morpho.sources.ecb import fetch_series as fetch_ecb


class Treasury:
    """US Treasury yield data."""

    @staticmethod
    def yields(**kwargs):
        return fetch_yields(**kwargs)


class Zillow:
    """Zillow housing market data."""

    @staticmethod
    def zhvi(**kwargs):
        return fetch_zhvi(**kwargs)

    @staticmethod
    def zori(**kwargs):
        return fetch_zori(**kwargs)


class SEC:
    """SEC EDGAR company filings."""

    @staticmethod
    def xbrl(cik: str, **kwargs):
        return fetch_xbrl(cik, **kwargs)

    @staticmethod
    def search(company: str, form: str = None, **kwargs):
        return search_filings(company, form=form, **kwargs)


class FEMA:
    """FEMA flood insurance and disaster data."""

    @staticmethod
    def nfip_policies(**kwargs):
        return fetch_nfip_policies(**kwargs)

    @staticmethod
    def disasters(**kwargs):
        return fetch_disasters(**kwargs)


class FDIC:
    """FDIC bank and deposit data."""

    @staticmethod
    def banks(**kwargs):
        return fetch_banks(**kwargs)

    @staticmethod
    def deposits(**kwargs):
        return fetch_deposits(**kwargs)


class EIA:
    """US Energy Information Administration data."""

    @staticmethod
    def energy(**kwargs):
        return fetch_energy(**kwargs)


class WorldBank:
    """World Bank Open Data."""

    @staticmethod
    def indicators(indicator: str = "NY.GDP.MKTP.CD", **kwargs):
        return fetch_indicators(indicator=indicator, **kwargs)


class IMF:
    """International Monetary Fund data."""

    @staticmethod
    def weo(country: str = None, indicator: str = None, **kwargs):
        return fetch_weo(country=country, indicator=indicator, **kwargs)


class CoinGecko:
    """Cryptocurrency market data."""

    @staticmethod
    def crypto(vs_currency: str = "usd", per_page: int = 100, page: int = 1):
        return fetch_crypto(vs_currency=vs_currency, per_page=per_page, page=page)


class FRED:
    """Federal Reserve Economic Data."""

    @staticmethod
    def series(series_id: str = "DGS10", **kwargs):
        return fetch_fred(series_id=series_id, **kwargs)


class CFTC:
    """CFTC Commitments of Traders."""

    @staticmethod
    def cot(report_type: str = "legacy", **kwargs):
        return fetch_cot(report_type=report_type, **kwargs)


class OECD:
    """OECD Data."""

    @staticmethod
    def indicator(indicator: str = "B1GQ", **kwargs):
        return fetch_oecd(indicator=indicator, **kwargs)


class BIS:
    """Bank for International Settlements."""

    @staticmethod
    def reserves(**kwargs):
        return fetch_reserve_data(**kwargs)

    @staticmethod
    def credit_to_gdp(**kwargs):
        return fetch_credit_to_gdp(**kwargs)


class FederalReserve:
    """Federal Reserve Bank Data."""

    @staticmethod
    def h8(**kwargs):
        return fetch_h8(**kwargs)

    @staticmethod
    def z1(**kwargs):
        return fetch_z1(**kwargs)


class CBOE:
    """CBOE Options Data."""

    @staticmethod
    def chain(symbol: str, **kwargs):
        return fetch_options_chain(symbol=symbol, **kwargs)


class ECB:
    """ECB Statistical Data Warehouse."""

    @staticmethod
    def series(flow_ref: str = "FM", key: str = "D.U2.EUR.4F.KR.MRR_FR.LEV", **kwargs):
        return fetch_ecb(flow_ref=flow_ref, key=key, **kwargs)
