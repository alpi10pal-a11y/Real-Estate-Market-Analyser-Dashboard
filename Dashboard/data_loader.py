from pathlib import Path
import pandas as pd


# ---------------------------------------------------------
# Project paths
# ---------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "dashboard_data"


# ---------------------------------------------------------
# Helper function
# ---------------------------------------------------------

def load_csv(filename):
    """
    Load a CSV file from dashboard_data.
    """

    file_path = DATA_DIR / filename

    if not file_path.exists():
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    return pd.read_csv(file_path)


# ---------------------------------------------------------
# Main property prediction data
# ---------------------------------------------------------

def load_test_predictions():
    return load_csv(
        "real_estate_test_predictions.csv"
    )


# ---------------------------------------------------------
# Market analysis datasets
# ---------------------------------------------------------

def load_city_market():
    return load_csv(
        "city_market_analysis.csv"
    )


def load_city_price():
    return load_csv(
        "city_price_analysis.csv"
    )


def load_city_bhk():
    return load_csv(
        "city_bhk_analysis.csv"
    )


def load_locality_market():
    return load_csv(
        "locality_market_analysis.csv"
    )


def load_reliable_localities():
    return load_csv(
        "reliable_locality_analysis.csv"
    )


def load_property_type():
    return load_csv(
        "property_type_analysis.csv"
    )


def load_bhk_price():
    return load_csv(
        "bhk_price_analysis.csv"
    )


def load_amenity_price():
    return load_csv(
        "amenity_price_analysis.csv"
    )


def load_city_price_per_sqft():
    return load_csv(
        "city_price_per_sqft_analysis.csv"
    )


def load_city_price_variability():
    return load_csv(
        "city_price_variability.csv"
    )


def load_property_price_per_sqft():
    return load_csv(
        "property_price_per_sqft_analysis.csv"
    )


def load_overall_statistics():
    return load_csv(
        "overall_market_statistics.csv"
    )


def load_market_insights():
    return load_csv(
        "market_insights.csv"
    )