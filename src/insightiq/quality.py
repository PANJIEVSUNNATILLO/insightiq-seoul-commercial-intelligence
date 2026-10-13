
"""Data quality checks for InsightIQ."""

import pandas as pd


def summarize_quality(df: pd.DataFrame) -> dict:
    """Summarize basic data quality indicators."""
    return {
        "rows": len(df),
        "columns": len(df.columns),
        "duplicate_rows": int(df.duplicated().sum()),
        "missing_cells": int(df.isna().sum().sum()),
    }
