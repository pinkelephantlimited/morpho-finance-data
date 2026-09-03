#!/usr/bin/env python3
"""
Fetch all available data sources and cache locally.

Usage:
    python scripts/fetch_all.py [--output-dir data]
"""

import argparse
import os
import pandas as pd


def main():
    parser = argparse.ArgumentParser(description="Fetch all finance data sources")
    parser.add_argument("--output-dir", default="data", help="Output directory")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    sources = [
        ("treasury_yields", "morpho.sources.treasury", "fetch_yields"),
        ("zhvi", "morpho.sources.zillow", "fetch_zhvi"),
        ("zori", "morpho.sources.zillow", "fetch_zori"),
        ("crypto", "morpho.sources.coingecko", "fetch_crypto"),
        ("worldbank_gdp", "morpho.sources.worldbank", "fetch_indicators"),
    ]

    for name, module_path, func_name in sources:
        print(f"Fetching {name}...")
        try:
            module = __import__(module_path, fromlist=[func_name])
            func = getattr(module, func_name)

            if name == "worldbank_gdp":
                df = func("NY.GDP.MKTP.CD")
            else:
                df = func()

            output_path = os.path.join(args.output_dir, f"{name}.csv")
            df.to_csv(output_path, index=False)
            print(f"  Saved {len(df)} rows to {output_path}")
        except Exception as e:
            print(f"  Error: {e}")

    print("\nDone!")


if __name__ == "__main__":
    main()
