"""stage03_transform.py.

(EDIT YOUR VERSION OF THIS FILE)

Source: validated JSON object
Sink: Polars DataFrame

Purpose

  Transform validated JSON data into a structured format.

Analytical Questions

- Which countries reported the highest COVID-19 case counts??
- How do cases, recoveries, and deaths compare across countries?
- Which countries have the highest case rates per million people?


Edited Python file to:
- extract the fields needed for your analysis,
- normalize records into a consistent structure,
- create any derived fields required.
"""

# ============================================================
# Section 1. Setup and Imports
# ============================================================

import logging
from typing import Any

import polars as pl

# ============================================================
# Section 2. Define Run Transform Function
# ============================================================


def run_transform(
    json_data: list[dict[str, Any]],
    LOG: logging.Logger,
) -> pl.DataFrame:
    """Transform JSON into a structured DataFrame.

    Args:
        json_data (list[dict[str, Any]]): Validated JSON data.
        LOG (logging.Logger): The logger instance.

    Returns:
        pl.DataFrame: The transformed dataset.
    """
    LOG.info("========================")
    LOG.info("STAGE 03: TRANSFORM starting...")
    LOG.info("========================")

    records: list[dict[str, Any]] = []

    for record in json_data:
        records.append(
            {
                "country": record.get("country"),
                "continent": record.get("continent"),
                "cases": record.get("cases"),
                "deaths": record.get("deaths"),
                "recovered": record.get("recovered"),
                "active": record.get("active"),
                "population": record.get("population"),
                "cases_per_million": record.get("casesPerOneMillion"),
                "deaths_per_million": record.get("deathsPerOneMillion"),
            }
        )

    df = pl.DataFrame(records)

    LOG.info("Transformation complete.")
    LOG.info(f"DataFrame preview:\n{df.head()}")
    LOG.info("Sink: Polars DataFrame created")

    # Return the transformed DataFrame for use in the next stage.
    return df
