import matplotlib.pyplot as plt


def city_price_chart(city_data):
    """
    Average predicted property price by city.
    """

    data = city_data.sort_values(
        "Average_Predicted_Price_INR",
        ascending=True
    )

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.barh(
        data["City"],
        data["Average_Predicted_Price_INR"]
    )

    ax.set_xlabel("Average Predicted Price (INR)")
    ax.set_ylabel("City")
    ax.set_title("Average Predicted Property Price by City")

    fig.tight_layout()

    return fig


def property_type_price_chart(property_data):
    """
    Average predicted property price by property type.
    """

    data = property_data.sort_values(
        "Average_Predicted_Price_INR",
        ascending=True
    )

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.barh(
        data["PropertyType"],
        data["Average_Predicted_Price_INR"]
    )

    ax.set_xlabel("Average Predicted Price (INR)")
    ax.set_ylabel("Property Type")
    ax.set_title("Average Predicted Price by Property Type")

    fig.tight_layout()

    return fig


def bhk_price_chart(bhk_data):
    """
    Average predicted property price by BHK.
    """

    data = bhk_data.sort_values(
        "BHK",
        ascending=True
    )

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.bar(
        data["BHK"].astype(str),
        data["Average_Predicted_Price_INR"]
    )

    ax.set_xlabel("BHK")
    ax.set_ylabel("Average Predicted Price (INR)")
    ax.set_title("Average Predicted Price by BHK")

    fig.tight_layout()

    return fig


def price_distribution_chart(df):
    """
    Distribution of predicted property prices.
    """

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.hist(
        df["Predicted_Price_INR"].dropna(),
        bins=30
    )

    ax.set_xlabel("Predicted Property Price (INR)")
    ax.set_ylabel("Number of Properties")
    ax.set_title("Predicted Property Price Distribution")

    fig.tight_layout()

    return fig


def price_per_sqft_city_chart(city_data):
    """
    Average price per square foot by city.
    """

    data = city_data.sort_values(
        "Average_Price_per_sqft",
        ascending=True
    )

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.barh(
        data["City"],
        data["Average_Price_per_sqft"]
    )

    ax.set_xlabel("Average Price per Sq.ft")
    ax.set_ylabel("City")
    ax.set_title("Average Price per Sq.ft by City")

    fig.tight_layout()

    return fig