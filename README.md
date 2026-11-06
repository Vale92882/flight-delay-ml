# Flight delay analysis

Explore recorded weather delays using DuckDB and SQL. The analysis covers
missing values, weather measurements at origin and destination airports,
delay durations, airport comparisons, and monthly patterns.

## Setup

Install `uv` using pip:

```bash
python -m pip install uv
```

Move into the project directory, then install the notebook dependencies:

```bash
cd flight-delay-ml
uv sync
```
## Data

Download the [BTS flights and weather dataset](https://huggingface.co/datasets/Arimancy/bts-flights-weather):

```bash
uv run python scripts/download_datasets.py --dataset bts_flights_weather
```

By default, this downloads all available year partitions under
`data/bts_flights_weather/flights_weather/`. The notebook selects its analysis
year using `YEAR` (2023 by default).
To download a single year instead, add `--year 2024`.

## Exploratory data analysis

Open [notebooks/weather_delay_eda.ipynb](notebooks/weather_delay_eda.ipynb)
and run the cells in order using the project's Python environment. Write SQL
in the query strings and record your observations in the analysis notes.
Keep the specified result variable names and column aliases: the plotting
cells use these names and are ready to run.
