
import argparse
import sys
from pathlib import Path

from fire_gdp import get_fire_gdp_year_data
from scatter import create_plot, save_plot


PROJECT_ROOT = Path(__file__).resolve().parent.parent


def parse_arguments():
    
    parser = argparse.ArgumentParser(
        description="Plot any of GDP, CO2 from Fires, and Year."
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
        default=PROJECT_ROOT / "data" / "AgroFood_co2_emission",
        help="Forest fire data CSV."
    )

    parser.add_argument(
        "--gdp",
        type=Path,
        default=PROJECT_ROOT / "data" / "IMF_GDP.csv",
        help="GDP data CSV."
    )

    parser.add_argument(
        "--country",
        default="Afghanistan",
        help="Country to plot."
    )

    parser.add_argument(
            "--axisX",
            choices=["year", "fires", "gdp"],
            default="year",
            help="X Axis to plot."
        )

    parser.add_argument(
                "--axisY",
                choices=["year", "fires", "gdp"],
                default="fires",
                help="Y Axis to plot."
            )

    return parser.parse_args()


def prepare_data(rows):
    """Convert year, fire, GDP rows into plot coordinates."""
    years = []
    fires = []
    gdps = []

    for year, fire, gdp in rows:
        years.append(year)
        fires.append(fire)
        gdps.append(gdp)

    if not gdps:
        raise ValueError("No data available to plot.")

    return [years, fires, gdps]


def main():
    """Generate plot."""
    args = parse_arguments()

    column_indices = {
    "year": 0,
    "fires": 1,
    "gdp": 2
    }

    titles = ["Year", "CO2 Due To Fires", "GDP"]

    x_axis = column_indices[args.axisX]
    y_axis = column_indices[args.axisY]

    try:
        rows = get_fire_gdp_year_data(
            args.co2,
            args.gdp,
            args.country
        )

        data = prepare_data(rows)

        x_vals = data[x_axis]
        y_vals = data[y_axis]



        fig = create_plot(
            x_vals,
            y_vals,
            f"{titles[x_axis]} vs {titles[y_axis]}: {args.country}",
            titles[x_axis],
            titles[y_axis]
        )

        save_plot(fig, args.out)

    except (OSError, ValueError, IndexError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
