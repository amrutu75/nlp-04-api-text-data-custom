"""config.py.

(EDIT YOUR VERSION OF THIS FILE)

Purpose

  Store configuration values for the EVTL pipeline.

Analytical Questions

- Which countries reported the highest COVID-19 case counts??
- How do cases, recoveries, and deaths compare across countries?
- Which countries have the highest case rates per million people?

"""

from pathlib import Path

# ============================================================
# API CONFIGURATION
# ============================================================


API_URL: str = "https://disease.sh/v3/covid-19/countries"

# Custom User-Agent identifying the project
HTTP_REQUEST_HEADERS: dict[str, str] = {
    "User-Agent": "covid-country-analysis-agnes/1.0",
    "Accept": "application/json",
}

# ============================================================
# PATH CONFIGURATION
# ============================================================

ROOT_PATH: Path = Path.cwd()
DATA_PATH: Path = ROOT_PATH / "data"
RAW_PATH: Path = DATA_PATH / "raw"
PROCESSED_PATH: Path = DATA_PATH / "processed"

# ============================================================
# Output Files
# ============================================================
RAW_JSON_PATH: Path = RAW_PATH / "covid_country_analysis_agnes_raw.json"
PROCESSED_CSV_PATH: Path = PROCESSED_PATH / "covid_country_analysis_agnes_processed.csv"
