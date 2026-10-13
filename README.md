InsightIQ AI — Seoul Commercial Intelligence

A reproducible Python analytics project exploring estimated sales across Seoul’s commercial areas and business categories.

Objectives

* Profile and validate the source dataset.
* Analyze estimated sales by industry and commercial area.
* Create interactive Plotly visualizations.
* Export reusable analytical summaries.
* Establish automated tests and reproducible workflows.

Technology stack

Python · pandas · Plotly · pytest · Google Colab · GitHub

Data source

Seoul Open Data Plaza — Commercial Area Estimated Sales

The dataset contains estimated sales figures. These values are not profit or audited point-of-sale revenue. Aggregated totals must be interpreted in light of the source’s reporting grain, methodology, and geographic definitions.

Project status

The exploratory notebook and interactive charts have been developed in Google Colab. The next stage separates reusable analytics from the notebook and adds automated validation and reproducible execution.

Reproducibility

1. Download the source dataset from the official portal.
2. Place the CSV in data/raw/.
3. Install the dependencies listed in requirements.txt.
4. Run the analysis script and automated tests.

Limitations

* Estimated sales should not be interpreted as profit.
* Aggregations across overlapping dimensions may double-count records.
* Comparisons across reporting periods require consistent definitions and spatial units.
* Conclusions should be validated against the official data dictionary.

Future work

* Add automated schema and data-quality validation.
* Build a Streamlit dashboard.
* Add continuous integration with GitHub Actions.
* Explore demographic and time-of-day patterns after validating field definitions.
