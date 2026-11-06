"""Download all BTS flight/weather year partitions, or a single selected year."""
import argparse
from pathlib import Path

from huggingface_hub import snapshot_download


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dataset", choices=["bts_flights_weather"], default="bts_flights_weather",
        help="Dataset used by the weather-delay EDA.",
    )
    parser.add_argument("--year", type=int, help="Download only this year (default: all years).")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    snapshot_download(
        repo_id="Arimancy/bts-flights-weather",
        repo_type="dataset",
        local_dir=root / "data" / "bts_flights_weather",
        allow_patterns=(
            f"flights_weather/year={args.year}/*.parquet"
            if args.year is not None
            else "flights_weather/year=*/*.parquet"
        ),
    )


if __name__ == "__main__":
    main()
