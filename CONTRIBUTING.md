# Contributing to Morpho Finance Data

Thank you for your interest in contributing! This project collects truly free financial data sources — no API keys, no registration, no restrictions.

## Requirements for New Sources

Every source added must meet ALL criteria:

1. **Truly free** — No signup, no API key, no paywall, no credit card
2. **Publicly accessible** — Direct HTTP endpoint (CSV, JSON, XML, TXT)
3. **Reproducible** — Include working example code and expected output format
4. **Stable** — Source should be maintained and not likely to disappear soon
5. **Financially relevant** — Data must be directly related to finance, markets, or the financial industry

## How to Contribute

### Adding a New Source

1. Fork the repository
2. Create a branch: `git checkout -b add-source-name`
3. Add the source to the appropriate category in `README.md`
4. Create a module in `morpho/sources/` with:
   - A `fetch_*()` function that returns a pandas DataFrame
   - Docstring with source URL, description, and example output
   - Type hints
5. Add an example in `examples/`
6. Run tests: `python -m pytest tests/`
7. Submit a pull request

### Module Template

```python
"""
[Source Name] - [Brief Description]

Source: [URL]
Access: [CSV/JSON/XML]
Auth: None
"""

import pandas as pd
import requests
from typing import Optional


def fetch_[name](**kwargs) -> pd.DataFrame:
    """
    Fetch [description] from [source].

    Returns:
        pd.DataFrame with [columns description]

    Example:
        >>> df = fetch_[name]()
        >>> print(df.columns)
        Index(['date', 'value', ...])
    """
    url = "https://..."
    response = requests.get(url, **kwargs)
    response.raise_for_status()
    # Parse and return DataFrame
    return pd.DataFrame(...)
```

### Code Style

- Python 3.9+
- Type hints on all public functions
- Google-style docstrings
- Tests for each source module
- No external dependencies beyond `pandas` and `requests`

## Reporting Issues

Open an issue with:
- Source name and URL
- What data it provides
- Why it should be included (or removed)

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
