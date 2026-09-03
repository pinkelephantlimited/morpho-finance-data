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
    def indicators(**kwargs):
        return fetch_indicators(**kwargs)


class IMF:
    """International Monetary Fund data."""

    @staticmethod
    def weo(**kwargs):
        return fetch_weo(**kwargs)


class CoinGecko:
    """Cryptocurrency market data."""

    @staticmethod
    def crypto(**kwargs):
        return fetch_crypto(**kwargs)
