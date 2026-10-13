“”“Run the InsightIQ commercial intelligence analysis pipeline.”””

from pathlib import Path
import sys

import pandas as pd

Make the src package importable when running this script directly.

PROJECT_ROOT = Path(file).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / “src”))

from insightiq.quality import summarize_quality  # noqa: E402

DATA_DIR = PROJECT_ROOT / “data”
RAW_DIR = DATA_DIR / “raw”
PROCESSED_DIR = DATA_DIR / “processed”
REPORTS_DIR = DATA_DIR / “reports”

def find_dataset() -> Path:
“”“Find a CSV dataset in data/raw.”””
files = list(RAW_DIR.glob(”*.csv”))

if not files:
    raise FileNotFoundError(
        f"No CSV found in {RAW_DIR}. "
        "Place your Seoul commercial-sales CSV there first."
    )
if len(files) > 1:
    raise ValueError(
        f"Found multiple CSV files in {RAW_DIR}: {files}. "
        "Keep one dataset there or update the script to select one."
    )
return files[0]

def main() -> None:
“”“Load the dataset, assess quality, and export basic reports.”””
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

dataset_path = find_dataset()
print(f"Loading dataset: {dataset_path.name}")
df = pd.read_csv(dataset_path, low_memory=False)
print(f"Dataset shape: {df.shape[0]:,} rows × {df.shape[1]:,} columns")
quality_report = summarize_quality(df)
if isinstance(quality_report, pd.DataFrame):
    quality_report.to_csv(
        REPORTS_DIR / "data_quality_report.csv",
        index=False,
        encoding="utf-8-sig",
    )
else:
    raise TypeError(
        "summarize_quality(df) must return a pandas DataFrame. "
        "Check src/insightiq/quality.py."
    )
print(f"Quality report saved to: {REPORTS_DIR / 'data_quality_report.csv'}")
print("InsightIQ pipeline completed successfully.")

if name == “main”:
main()
