import pandas as pd


def get_market_kpis(df):
    """
    Calculate main market KPIs from the property prediction dataset.
    """

    total_properties = len(df)

    average_predicted_price = df["Predicted_Price_INR"].mean()

    median_predicted_price = df["Predicted_Price_INR"].median()

    average_area = df["CarpetArea_sqft"].mean()

    average_bhk = df["BHK"].mean()

    return {
        "total_properties": total_properties,
        "average_predicted_price": average_predicted_price,
        "median_predicted_price": median_predicted_price,
        "average_area": average_area,
        "average_bhk": average_bhk
    }


def filter_properties(
    df,
    cities=None,
    property_types=None,
    bhks=None,
    furnishing=None
):
    """
    Apply dashboard filters to the property dataset.
    """

    filtered_df = df.copy()

    if cities:
        filtered_df = filtered_df[
            filtered_df["City"].isin(cities)
        ]

    if property_types:
        filtered_df = filtered_df[
            filtered_df["PropertyType"].isin(property_types)
        ]

    if bhks:
        filtered_df = filtered_df[
            filtered_df["BHK"].isin(bhks)
        ]

    if furnishing:
        filtered_df = filtered_df[
            filtered_df["Furnishing"].isin(furnishing)
        ]

    return filtered_df


def city_prediction_summary(df):
    """
    Calculate city-wise predicted price summary.
    """

    return (
        df.groupby("City", dropna=False)
        .agg(
            Property_Count=("ListingID", "count"),
            Average_Predicted_Price_INR=(
                "Predicted_Price_INR",
                "mean"
            ),
            Median_Predicted_Price_INR=(
                "Predicted_Price_INR",
                "median"
            )
        )
        .reset_index()
        .sort_values(
            "Average_Predicted_Price_INR",
            ascending=False
        )
    )


def property_type_prediction_summary(df):
    """
    Calculate property-type-wise predicted price summary.
    """

    return (
        df.groupby("PropertyType", dropna=False)
        .agg(
            Property_Count=("ListingID", "count"),
            Average_Predicted_Price_INR=(
                "Predicted_Price_INR",
                "mean"
            ),
            Median_Predicted_Price_INR=(
                "Predicted_Price_INR",
                "median"
            )
        )
        .reset_index()
        .sort_values(
            "Average_Predicted_Price_INR",
            ascending=False
        )
    )


def bhk_prediction_summary(df):
    """
    Calculate BHK-wise predicted price summary.
    """

    return (
        df.groupby("BHK", dropna=False)
        .agg(
            Property_Count=("ListingID", "count"),
            Average_Predicted_Price_INR=(
                "Predicted_Price_INR",
                "mean"
            ),
            Median_Predicted_Price_INR=(
                "Predicted_Price_INR",
                "median"
            )
        )
        .reset_index()
        .sort_values("BHK")
    )


def locality_prediction_summary(df):
    """
    Calculate locality-wise predicted price summary.
    """

    return (
        df.groupby(
            ["City", "Locality"],
            dropna=False
        )
        .agg(
            Property_Count=("ListingID", "count"),
            Average_Predicted_Price_INR=(
                "Predicted_Price_INR",
                "mean"
            ),
            Median_Predicted_Price_INR=(
                "Predicted_Price_INR",
                "median"
            )
        )
        .reset_index()
        .sort_values(
            "Average_Predicted_Price_INR",
            ascending=False
        )
    )