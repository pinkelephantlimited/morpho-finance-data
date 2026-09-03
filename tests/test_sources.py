"""Tests for morpho-finance-data sources."""

import pytest
import pandas as pd


class TestTreasury:
    def test_fetch_yields_daily(self):
        from morpho.sources.treasury import fetch_yields
        df = fetch_yields(period="daily")
        assert isinstance(df, pd.DataFrame)
        assert "Date" in df.columns
        assert len(df) > 0

    def test_fetch_yields_monthly(self):
        from morpho.sources.treasury import fetch_yields
        df = fetch_yields(period="monthly")
        assert isinstance(df, pd.DataFrame)
        assert len(df) > 0


class TestSEC:
    def test_search_filings(self):
        from morpho.sources.sec import search_filings
        df = search_filings("Apple", form="10-K", limit=5)
        assert isinstance(df, pd.DataFrame)
        assert "form" in df.columns
        assert len(df) <= 5


class TestZillow:
    def test_fetch_zhvi(self):
        from morpho.sources.zillow import fetch_zhvi
        df = fetch_zhvi()
        assert isinstance(df, pd.DataFrame)
        assert "RegionName" in df.columns
        assert len(df) > 0

    def test_fetch_zori(self):
        from morpho.sources.zillow import fetch_zori
        df = fetch_zori()
        assert isinstance(df, pd.DataFrame)
        assert len(df) > 0


class TestFEMA:
    def test_fetch_disasters(self):
        from morpho.sources.fema import fetch_disasters
        df = fetch_disasters(limit=100)
        assert isinstance(df, pd.DataFrame)
        assert len(df) > 0


class TestWorldBank:
    def test_fetch_indicators(self):
        from morpho.sources.worldbank import fetch_indicators
        df = fetch_indicators("NY.GDP.MKTP.CD")
        assert isinstance(df, pd.DataFrame)
        assert len(df) > 0


class TestCoinGecko:
    def test_fetch_crypto(self):
        from morpho.sources.coingecko import fetch_crypto
        df = fetch_crypto(per_page=10)
        assert isinstance(df, pd.DataFrame)
        assert len(df) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
