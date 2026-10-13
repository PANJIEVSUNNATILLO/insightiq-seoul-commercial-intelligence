“”“Run the InsightIQ commercial intelligence analysis pipeline.”””

from pathlib import Path
import sys

import pandas as pd

PROJECT_ROOT = Path(file).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / “src”))

from insightiq.quality import summarize_quality  # noqa: E402

RAW_DIR = PROJECT_ROOT / “data” / “raw”
REPORTS_DIR = PROJECT_ROOT / “data” / “reports”

def find_dataset() -> Path:
“”“Find exactly one CSV dataset in data/raw.”””
files = sorted(RAW_DIR.glob(”*.csv”))

if not files:
    raise FileNotFoundError(
        f"No CSV found in {RAW_DIR}. "
        "Place your commercial-sales dataset there first."
    )
if len(files) > 1:
    raise ValueError(
        f"Expected one CSV file in {RAW_DIR}, found {len(files)}."
    )
return files[0]

def main() -> None:
“”“Load the dataset and export a basic data-quality report.”””
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

dataset_path = find_dataset()
print(f"Loading dataset: {dataset_path.name}")
df = pd.read_csv(dataset_path, low_memory=False)
print(f"Dataset shape: {df.shape[0]:,} rows × {df.shape[1]:,} columns")
quality_report = summarize_quality(df)
report_path = REPORTS_DIR / "data_quality_report.csv"
pd.DataFrame([quality_report]).to_csv(
    report_path,
    index=False,
    encoding="utf-8-sig",
)
print("\nData quality summary")
for metric, value in quality_report.items():
    print(f"  {metric}: {value:,}")
print(f"\nReport saved to: {report_path}")
print("InsightIQ pipeline completed successfully.")

if name == “main”:
main()
