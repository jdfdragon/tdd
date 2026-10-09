
import argparse
import sys
from pathlib import Path

from fire_gdp import get_fire_gdp_year_data
from scatter import create_plot, save_plot


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"


def parse_arguments():
    
    parser = argparse.ArgumentParser(
        description="Plot GDP against forest fires."
    )

    parser.add_argument(
        "--out",
        type=Path,
        default=Path("fire_gdp.png"),
        help="Output image filename."
    )

    parser.add_argument(
        "--co2",
        type=Path,
        default=DATA_DIR / "testAgroFood.csv",
        help="Forest fire data CSV."
    )

    parser.add_argument(
        "--gdp",
        type=Path,
        default=DATA_DIR / "testIMF.csv",
        help="GDP data CSV."
    )

    parser.add_argument(
        "--country",
        default="Afghanistan",
        help="Country to plot."
    )

    return parser.parse_args()


def prepare_data(rows):
    """Convert year, fire, GDP rows into plot coordinates."""
    gdp_values = []
    fire_values = []

    for year, fires, gdp in rows:
        gdp_values.append(float(gdp))
        fire_values.append(float(fires))

    if not gdp_values:
        raise ValueError("No data available to plot.")

    return gdp_values, fire_values


def main():
    """Generate the GDP vs forest fires plot."""
    args = parse_arguments()

    try:
        rows = get_fire_gdp_year_data(
            args.co2,
            args.gdp,
            args.country
        )

        x_values, y_values = prepare_data(rows)

        fig = create_plot(
            x_values,
            y_values,
            f"GDP vs Forest Fires: {args.country}",
            "GDP",
            "Forest Fires"
        )

        save_plot(fig, args.out)

    except (OSError, ValueError, IndexError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
