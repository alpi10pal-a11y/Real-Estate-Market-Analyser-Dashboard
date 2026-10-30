from pathlib import Path

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


# ============================================================
# PAGE SETTINGS
# ============================================================

st.set_page_config(
    page_title="Real Estate Analytics Dashboard",
    page_icon="🏠",
    layout="wide"
)

st.markdown(
    """
    <style>
    :root {
        --realty-navy: #e7f4f3;
        --realty-ink: #c9dcdf;
        --realty-blue: #64b5d2;
        --realty-teal: #4fd1bd;
        --realty-mint: #b8f1e4;
        --realty-muted: #91abb3;
        --realty-surface: #162b3c;
        --realty-card: #1b3447;
        --realty-border: #2b4a5d;
        --realty-shadow: 0 14px 34px rgba(2, 13, 23, 0.28);
    }

    .stApp {
        background: #0a1724;
        color: var(--realty-navy);
    }

    .main .block-container {
        max-width: 1540px;
        padding: 2rem 3rem 3rem;
    }

    [data-testid="stHorizontalBlock"] {
        gap: 1.25rem;
    }

    .stApp h1,
    .stApp h2,
    .stApp h3,
    .stApp h4,
    .stApp h5,
    .stApp h6 {
        color: var(--realty-navy);
    }

    .stApp p,
    .stApp label,
    .stApp [data-testid="stMarkdownContainer"],
    .stApp [data-testid="stCaptionContainer"] {
        color: var(--realty-navy);
    }

    .stApp h1 {
        font-weight: 750;
        letter-spacing: -0.04em;
    }

    .stApp h2 {
        margin-top: 1.65rem;
        font-size: 1.45rem;
        letter-spacing: -0.025em;
    }

    .stApp h3 {
        margin-top: 1.25rem;
        font-size: 1.08rem;
        letter-spacing: -0.01em;
    }

    [data-testid="stHeader"] {
        background: rgba(10, 23, 36, 0.92);
    }

    [data-testid="stSidebar"] {
        background: #0e2233;
        border-right: 1px solid #244456;
    }

    [data-testid="stSidebar"] * {
        color: #f5f7fa;
    }

    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h2 {
        color: #ffffff;
        font-size: 1.18rem;
        margin: 0.25rem 0 0.2rem;
    }

    [data-testid="stSidebar"] [data-testid="stCaptionContainer"] {
        color: rgba(255, 255, 255, 0.78);
    }

    [data-testid="stSidebar"] [data-testid="stExpander"] {
        margin: 0.9rem 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 14px;
        background: rgba(255, 255, 255, 0.035);
        box-shadow: 0 8px 18px rgba(2, 13, 23, 0.2);
    }

    [data-testid="stSidebar"] [data-testid="stExpander"] details {
        padding: 0.35rem 0.9rem 0.85rem;
    }

    [data-testid="stSidebar"] [data-testid="stWidgetLabel"] {
        margin-top: 1rem;
        margin-bottom: 0.45rem;
        font-size: 0.82rem;
        font-weight: 650;
    }

    [data-testid="stSidebar"] [data-baseweb="select"] > div,
    [data-testid="stSidebar"] [data-baseweb="input"] > div {
        min-height: 2.65rem;
        background: #162f42;
        border-color: #376075;
        border-radius: 9px;
    }

    [data-testid="stSidebar"] [data-baseweb="select"]:focus-within > div {
        border-color: var(--realty-teal);
        box-shadow: 0 0 0 1px var(--realty-teal);
    }

    [data-testid="stSidebar"] [data-baseweb="select"] *,
    [data-testid="stSidebar"] [role="listbox"] * {
        color: var(--realty-navy);
    }

    /* Streamlit 1.64 selected values: span[data-tag] inside this container. */
    [data-testid="stMultiSelectTagsContainer"] [data-tag] {
        background-color: #2DD4BF !important;
        border: 1px solid #5EEAD4 !important;
        border-radius: 6px;
        color: #0B1120 !important;
        margin: 0.18rem 0.22rem 0.18rem 0;
    }

    [data-testid="stMultiSelectTagsContainer"] [data-tag] span,
    [data-testid="stMultiSelectTagsContainer"] [data-tag] button,
    [data-testid="stMultiSelectTagsContainer"] [data-tag] svg {
        color: #0B1120 !important;
    }

    [data-testid="stMultiSelectTagsContainer"] [data-tag] button {
        background: transparent !important;
        border: 0 !important;
        border-radius: 50%;
    }

    [data-testid="stMultiSelectTagsContainer"] [data-tag] button:hover {
        background-color: #5EEAD4 !important;
        color: #0B1120 !important;
    }

    [data-testid="stMultiSelectTagsContainer"] [data-tag] svg {
        fill: currentColor !important;
    }

    .realty-hero {
        position: relative;
        overflow: hidden;
        background:
            radial-gradient(circle at 88% 18%, rgba(79, 209, 189, 0.23), transparent 25%),
            linear-gradient(118deg, #10283b 0%, #153b50 57%, #126b69 100%);
        border: 1px solid #31576b;
        border-radius: 20px;
        padding: 2.25rem 2.6rem 2.35rem;
        margin: 0.15rem 0 1.8rem;
        color: white;
        box-shadow: 0 18px 38px rgba(16, 42, 67, 0.18);
    }

    .realty-hero:after {
        content: "";
        position: absolute;
        right: -5rem;
        bottom: -5rem;
        width: 17rem;
        height: 17rem;
        border: 1px solid rgba(217, 243, 238, 0.2);
        border-radius: 50%;
    }

    .realty-hero h1 {
        position: relative;
        z-index: 1;
        margin: 0.4rem 0 0;
        color: white;
        font-size: 2.35rem;
        letter-spacing: -0.045em;
    }

    .realty-hero p {
        position: relative;
        z-index: 1;
        color: rgba(255, 255, 255, 0.84);
        max-width: 720px;
        margin: 0.7rem 0 0;
        font-size: 1rem;
        line-height: 1.65;
    }

    .section-kicker {
        color: var(--realty-teal);
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        margin-bottom: -0.35rem;
    }

    [data-testid="stMetric"] {
        position: relative;
        background: linear-gradient(145deg, #1b3548 0%, #162b3c 100%);
        border: 1px solid var(--realty-border);
        border-radius: 16px;
        padding: 1.1rem 1.2rem;
        min-height: 116px;
        box-shadow: var(--realty-shadow);
        transition: transform 160ms ease, box-shadow 160ms ease;
    }

    [data-testid="stMetric"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 16px 34px rgba(2, 13, 23, 0.36);
    }

    [data-testid="stMetricLabel"] {
        color: var(--realty-muted);
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.02em;
    }

    [data-testid="stMetricValue"] {
        color: var(--realty-navy);
        font-size: 1.5rem;
        font-weight: 750;
        letter-spacing: -0.03em;
    }

    [data-testid="stDataFrame"] {
        border: 1px solid var(--realty-border);
        border-radius: 14px;
        overflow: hidden;
        box-shadow: 0 8px 22px rgba(16, 42, 67, 0.06);
        background: var(--realty-card);
    }

    [data-testid="stDataFrame"] [role="columnheader"] {
        background: #203f50;
        color: var(--realty-mint);
        font-weight: 700;
    }

    [data-testid="stDataFrame"] [role="gridcell"] {
        color: var(--realty-ink);
    }

    [data-testid="stImage"] {
        border-radius: 14px;
    }

    .stDivider {
        border-color: var(--realty-border);
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 0.2rem;
        padding: 0.35rem;
        border-bottom: 1px solid var(--realty-border);
        background: #112536;
        border-radius: 13px;
    }

    .stTabs [data-baseweb="tab"] {
        color: var(--realty-muted);
        font-weight: 600;
        padding: 0.72rem 1rem;
        border-radius: 9px;
    }

    .stTabs [data-baseweb="tab"] p,
    .stTabs [aria-selected="true"] p {
        color: inherit;
    }

    .stTabs [aria-selected="true"],
    .stTabs [aria-selected="true"] p {
        color: var(--realty-navy);
        font-weight: 750;
    }

    .stTabs [aria-selected="true"] {
        background: #1f4051;
        box-shadow: 0 3px 12px rgba(2, 13, 23, 0.3);
    }

    .stButton > button,
    .stDownloadButton > button {
        border-radius: 9px;
        border: 1px solid #b9ded7;
        background: #2b9d91;
        color: #071a27;
        font-weight: 700;
    }

    .stDownloadButton > button:hover {
        border-color: var(--realty-teal);
        color: var(--realty-navy);
        background: var(--realty-mint);
    }
    </style>
    """,
    unsafe_allow_html=True
)

plt.rcParams.update(
    {
        "text.color": "#c9dcdf",
        "axes.titlecolor": "#e7f4f3",
        "axes.labelcolor": "#b8f1e4",
        "xtick.color": "#91abb3",
        "ytick.color": "#91abb3",
        "axes.facecolor": "#162b3c",
        "figure.facecolor": "#162b3c",
        "axes.edgecolor": "#2b4a5d",
        "axes.grid": True,
        "grid.color": "#2b4a5d",
        "grid.linewidth": 0.8,
        "axes.prop_cycle": plt.cycler(
            color=["#4fd1bd", "#64b5d2", "#8ae3d3", "#d4eef1"]
        ),
    }
)


# ============================================================
# PROJECT PATHS
# ============================================================

DASHBOARD_DIR = Path(__file__).resolve().parent
PROJECT_DIR = DASHBOARD_DIR.parent
DATA_DIR = PROJECT_DIR / "dashboard_data"


# ============================================================
# DATA FILES
# ============================================================

PREDICTIONS_FILE = DATA_DIR / "real_estate_test_predictions.csv"
CITY_MARKET_FILE = DATA_DIR / "city_market_analysis.csv"
CITY_PRICE_FILE = DATA_DIR / "city_price_analysis.csv"
CITY_BHK_FILE = DATA_DIR / "city_bhk_analysis.csv"
LOCALITY_FILE = DATA_DIR / "locality_market_analysis.csv"
RELIABLE_LOCALITY_FILE = DATA_DIR / "reliable_locality_analysis.csv"
PROPERTY_TYPE_FILE = DATA_DIR / "property_type_analysis.csv"
BHK_FILE = DATA_DIR / "bhk_price_analysis.csv"
AMENITY_FILE = DATA_DIR / "amenity_price_analysis.csv"
CITY_SQFT_FILE = DATA_DIR / "city_price_per_sqft_analysis.csv"
VARIABILITY_FILE = DATA_DIR / "city_price_variability.csv"
PROPERTY_SQFT_FILE = DATA_DIR / "property_price_per_sqft_analysis.csv"
OVERALL_FILE = DATA_DIR / "overall_market_statistics.csv"
INSIGHTS_FILE = DATA_DIR / "market_insights.csv"


# ============================================================
# LOAD FUNCTION
# ============================================================

@st.cache_data
def load_csv(file_path):

    if not file_path.exists():
        st.error(
            f"Required file is missing:\n{file_path}"
        )
        st.stop()

    try:
        return pd.read_csv(file_path)

    except Exception as error:
        st.error(
            f"Unable to read:\n{file_path}\n\n"
            f"Error: {error}"
        )
        st.stop()


# ============================================================
# DATA SCHEMA NORMALIZATION
# ============================================================

def normalize_columns(df):
    """Clean column names without changing the dataset values."""
    df = df.copy()
    df.columns = (
        df.columns.astype(str)
        .str.replace("\ufeff", "", regex=False)
        .str.strip()
    )
    return df


def normalize_property_type_data(df):
    """Support both the old and current property-type export schemas."""
    df = normalize_columns(df)

    # Current notebook export uses INR column names.
    # The dashboard chart uses Lakhs, so derive Lakhs safely.
    if "Average_Price_Lakhs" not in df.columns and "Average_Price_INR" in df.columns:
        df["Average_Price_Lakhs"] = pd.to_numeric(
            df["Average_Price_INR"], errors="coerce"
        ) / 100000.0

    if "Median_Price_Lakhs" not in df.columns and "Median_Price_INR" in df.columns:
        df["Median_Price_Lakhs"] = pd.to_numeric(
            df["Median_Price_INR"], errors="coerce"
        ) / 100000.0

    if "Property_Count" not in df.columns and "Total_Listings" in df.columns:
        df["Property_Count"] = df["Total_Listings"]

    return df


def normalize_price_lakhs_data(df):
    """Normalize common price columns used by dashboard charts."""
    df = normalize_columns(df)

    if "Average_Price_Lakhs" not in df.columns and "Average_Price_INR" in df.columns:
        df["Average_Price_Lakhs"] = pd.to_numeric(
            df["Average_Price_INR"], errors="coerce"
        ) / 100000.0

    if "Median_Price_Lakhs" not in df.columns and "Median_Price_INR" in df.columns:
        df["Median_Price_Lakhs"] = pd.to_numeric(
            df["Median_Price_INR"], errors="coerce"
        ) / 100000.0

    return df


# ============================================================
# LOAD DATA
# ============================================================

predictions = load_csv(PREDICTIONS_FILE)

city_market = load_csv(CITY_MARKET_FILE)

city_price = load_csv(CITY_PRICE_FILE)

city_bhk = load_csv(CITY_BHK_FILE)

locality = load_csv(LOCALITY_FILE)

reliable_locality = load_csv(
    RELIABLE_LOCALITY_FILE
)

property_type = load_csv(
    PROPERTY_TYPE_FILE
)

bhk_data = load_csv(
    BHK_FILE
)

amenity = load_csv(
    AMENITY_FILE
)

city_sqft = load_csv(
    CITY_SQFT_FILE
)

variability = load_csv(
    VARIABILITY_FILE
)

property_sqft = load_csv(
    PROPERTY_SQFT_FILE
)

overall = load_csv(
    OVERALL_FILE
)

insights = load_csv(
    INSIGHTS_FILE
)


# Clean all imported column names and normalize the schemas that
# have changed between notebook export versions.
predictions = normalize_columns(predictions)
city_market = normalize_columns(city_market)
city_price = normalize_columns(city_price)
city_bhk = normalize_columns(city_bhk)
locality = normalize_columns(locality)
reliable_locality = normalize_columns(reliable_locality)
property_type = normalize_property_type_data(property_type)
bhk_data = normalize_price_lakhs_data(bhk_data)
amenity = normalize_price_lakhs_data(amenity)
city_sqft = normalize_columns(city_sqft)
variability = normalize_columns(variability)
property_sqft = normalize_columns(property_sqft)
overall = normalize_columns(overall)
insights = normalize_columns(insights)


# ============================================================
# CONVERT NUMERIC COLUMNS
# ============================================================

prediction_numeric_columns = [
    "BHK",
    "Bathrooms",
    "Balconies",
    "SuperBuiltUpArea_sqft",
    "BuiltUpArea_sqft",
    "CarpetArea_sqft",
    "TotalFloors",
    "YearBuilt",
    "AgeYears",
    "AmenitiesCount",
    "Latitude",
    "Longitude",
    "Predicted_Price_INR"
]

for column in prediction_numeric_columns:

    if column in predictions.columns:

        predictions[column] = pd.to_numeric(
            predictions[column],
            errors="coerce"
        )


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def format_lakhs(value):

    if pd.isna(value):
        return "N/A"

    return f"₹{value / 100000:,.2f} L"


def format_number(value):

    if pd.isna(value):
        return "N/A"

    return f"{value:,.2f}"


def clean_value(value):
    """
    Cleans values from the prepared insights CSV.

    The CSV may contain formatting characters from
    the previous dashboard generation. They are removed
    before the value is displayed.
    """

    if pd.isna(value):
        return ""

    value = str(value)

    # Remove markdown code fence characters
    value = value.replace("```html", "")
    value = value.replace("```HTML", "")
    value = value.replace("```text", "")
    value = value.replace("```", "")

    # Extract the actual text if the stored value
    # contains formatting markup.
    if ">" in value and "<" in value:

        parts = value.split(">")

        if len(parts) > 1:

            value = parts[1]

        if "<" in value:

            value = value.split("<")[0]

    # Remove any remaining formatting characters
    value = value.replace("\n", " ")
    value = value.replace("\r", " ")

    return value.strip()


# ============================================================
# TITLE
# ============================================================

st.markdown(
    """
    <div class="realty-hero">
        <div class="section-kicker" style="color: #b9f2e6;">
            Real estate intelligence
        </div>
        <h1>🏠 Real Estate Analytics Dashboard</h1>
        <p>
            Explore property prices, city markets, localities, BHK trends,
            amenities, price per square foot, and ML-based predictions.
        </p>
        <div style="position: relative; z-index: 1; margin-top: 1.25rem;">
            <span style="display: inline-block; padding: 0.38rem 0.75rem;
                border: 1px solid rgba(255,255,255,0.24); border-radius: 999px;
                color: #d9f3ee; font-size: 0.76rem; font-weight: 700;">
                LIVE MARKET VIEW
            </span>
            <span style="margin-left: 0.55rem; color: rgba(255,255,255,0.7);
                font-size: 0.82rem;">
                Filtered insights · predictive analytics · city-level trends
            </span>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown("## 🔎 Explore the market")
st.sidebar.caption("Filter the property prediction dataset.")
st.sidebar.markdown(
    '<div style="margin: 1.2rem 0 0.35rem; color: #b9f2e6; '
    'font-size: 0.7rem; font-weight: 700; letter-spacing: 0.12em;">'
    'FILTER CONTROLS</div>',
    unsafe_allow_html=True
)


# ============================================================
# CITY FILTER
# ============================================================

cities = sorted(
    predictions["City"]
    .dropna()
    .astype(str)
    .unique()
)

with st.sidebar.expander("🏙️ Location", expanded=True):

    selected_cities = st.multiselect(
        "City",
        options=cities,
        default=cities
    )


# ============================================================
# PROPERTY TYPE FILTER
# ============================================================

property_types = sorted(
    predictions["PropertyType"]
    .dropna()
    .astype(str)
    .unique()
)

with st.sidebar.expander("🏠 Property profile", expanded=True):

    selected_property_types = st.multiselect(
        "Property Type",
        options=property_types,
        default=property_types
    )

    bhk_values = sorted(
        predictions["BHK"]
        .dropna()
        .unique()
    )

    selected_bhks = st.multiselect(
        "BHK",
        options=bhk_values,
        default=bhk_values
    )

    furnishing_values = sorted(
        predictions["Furnishing"]
        .dropna()
        .astype(str)
        .unique()
    )

    selected_furnishing = st.multiselect(
        "Furnishing",
        options=furnishing_values,
        default=furnishing_values
    )


# ============================================================
# APPLY FILTERS
# ============================================================

filtered = predictions.copy()


if selected_cities:

    filtered = filtered[
        filtered["City"]
        .astype(str)
        .isin(selected_cities)
    ]


if selected_property_types:

    filtered = filtered[
        filtered["PropertyType"]
        .astype(str)
        .isin(selected_property_types)
    ]


if selected_bhks:

    filtered = filtered[
        filtered["BHK"]
        .isin(selected_bhks)
    ]


if selected_furnishing:

    filtered = filtered[
        filtered["Furnishing"]
        .astype(str)
        .isin(selected_furnishing)
    ]


# ============================================================
# NO RESULTS
# ============================================================

if filtered.empty:

    st.warning(
        "No properties match the selected filters."
    )

    st.stop()


# ============================================================
# MARKET OVERVIEW
# ============================================================

st.markdown('<div class="section-kicker">At a glance</div>', unsafe_allow_html=True)
st.header("📊 Market Overview")

total_properties = len(filtered)

average_price = filtered[
    "Predicted_Price_INR"
].mean()

median_price = filtered[
    "Predicted_Price_INR"
].median()

average_area = filtered[
    "CarpetArea_sqft"
].mean()

average_bhk = filtered[
    "BHK"
].mean()


# ============================================================
# KPI SECTION
# ============================================================

col1, col2, col3, col4, col5 = st.columns(5)


with col1:

    st.metric(
        "🏘️ Total Properties",
        f"{total_properties:,}"
    )


with col2:

    st.metric(
        "💰 Average Predicted Price",
        format_lakhs(average_price)
    )


with col3:

    st.metric(
        "📊 Median Predicted Price",
        format_lakhs(median_price)
    )


with col4:

    if pd.isna(average_area):

        area_text = "N/A"

    else:

        area_text = (
            f"{average_area:,.0f} sq.ft"
        )

    st.metric(
        "📐 Average Carpet Area",
        area_text
    )


with col5:

    st.metric(
        "🛏️ Average BHK",
        format_number(average_bhk)
    )


# ============================================================
# TABS
# ============================================================

overview_tab, market_tab, location_tab, insights_tab, ml_tab = st.tabs(
    [
        "📊 Overview",
        "🏙️ Market Analysis",
        "📍 Location Analysis",
        "💡 Market Insights",
        "🤖 ML Predictions"
    ]
)


# ============================================================
# OVERVIEW TAB
# ============================================================

with overview_tab:

    st.header(
        "📊 Property Overview"
    )

    left_column, right_column = st.columns(2)


    # --------------------------------------------------------
    # PROPERTY TYPE
    # --------------------------------------------------------

    with left_column:

        st.subheader(
            "🏠 Property Type Analysis"
        )

        type_chart = property_type.copy()

        type_chart[
            "Average_Price_Lakhs"
        ] = pd.to_numeric(
            type_chart[
                "Average_Price_Lakhs"
            ],
            errors="coerce"
        )

        type_chart = type_chart.dropna(
            subset=[
                "Average_Price_Lakhs"
            ]
        )

        if not type_chart.empty:

            fig, ax = plt.subplots(
                figsize=(8, 5)
            )

            ax.bar(
                type_chart[
                    "PropertyType"
                ].astype(str),
                type_chart[
                    "Average_Price_Lakhs"
                ]
            )

            ax.set_title(
                "Average Price by Property Type"
            )

            ax.set_xlabel(
                "Property Type"
            )

            ax.set_ylabel(
                "Average Price (₹ Lakhs)"
            )

            ax.tick_params(
                axis="x",
                rotation=35
            )

            fig.tight_layout()

            st.pyplot(
                fig,
                use_container_width=True
            )

            plt.close(fig)


    # --------------------------------------------------------
    # BHK
    # --------------------------------------------------------

    with right_column:

        st.subheader(
            "🛏️ BHK Analysis"
        )

        bhk_chart = bhk_data.copy()

        bhk_chart["BHK"] = pd.to_numeric(
            bhk_chart["BHK"],
            errors="coerce"
        )

        bhk_chart[
            "Average_Price_Lakhs"
        ] = pd.to_numeric(
            bhk_chart[
                "Average_Price_Lakhs"
            ],
            errors="coerce"
        )

        bhk_chart = bhk_chart.dropna(
            subset=[
                "BHK",
                "Average_Price_Lakhs"
            ]
        )

        bhk_chart = bhk_chart.sort_values(
            "BHK"
        )

        if not bhk_chart.empty:

            fig, ax = plt.subplots(
                figsize=(8, 5)
            )

            ax.bar(
                bhk_chart[
                    "BHK"
                ].astype(str),
                bhk_chart[
                    "Average_Price_Lakhs"
                ]
            )

            ax.set_title(
                "Average Price by BHK"
            )

            ax.set_xlabel(
                "BHK"
            )

            ax.set_ylabel(
                "Average Price (₹ Lakhs)"
            )

            fig.tight_layout()

            st.pyplot(
                fig,
                use_container_width=True
            )

            plt.close(fig)


    # --------------------------------------------------------
    # PRICE DISTRIBUTION
    # --------------------------------------------------------

    st.subheader(
        "💰 Price Distribution"
    )

    price_values = (
        filtered[
            "Predicted_Price_INR"
        ]
        .dropna()
        / 100000
    )

    if not price_values.empty:

        fig, ax = plt.subplots(
            figsize=(11, 5)
        )

        ax.hist(
            price_values,
            bins=30
        )

        ax.set_title(
            "Predicted Property Price Distribution"
        )

        ax.set_xlabel(
            "Predicted Price (₹ Lakhs)"
        )

        ax.set_ylabel(
            "Number of Properties"
        )

        fig.tight_layout()

        st.pyplot(
            fig,
            use_container_width=True
        )

        plt.close(fig)


# ============================================================
# MARKET ANALYSIS TAB
# ============================================================

with market_tab:

    st.header(
        "🏙️ Market Analysis"
    )


    # --------------------------------------------------------
    # CITY PRICE CHART
    # --------------------------------------------------------

    st.subheader(
        "🏙️ Average Predicted Price by City"
    )

    city_chart = (
        filtered
        .groupby("City", dropna=False)
        ["Predicted_Price_INR"]
        .mean()
        .reset_index()
    )

    city_chart["City"] = (
        city_chart["City"]
        .fillna("Unknown")
        .astype(str)
    )

    city_chart[
        "Average_Price_Lakhs"
    ] = (
        city_chart[
            "Predicted_Price_INR"
        ] / 100000
    )

    city_chart = city_chart.sort_values(
        "Average_Price_Lakhs"
    )

    if not city_chart.empty:

        fig, ax = plt.subplots(
            figsize=(10, 6)
        )

        ax.barh(
            city_chart["City"].astype(str),
            city_chart[
                "Average_Price_Lakhs"
            ]
        )

        ax.set_title(
            "Average Predicted Price by City"
        )

        ax.set_xlabel(
            "Average Predicted Price (₹ Lakhs)"
        )

        ax.set_ylabel(
            "City"
        )

        fig.tight_layout()

        st.pyplot(
            fig,
            use_container_width=True
        )

        plt.close(fig)


    # --------------------------------------------------------
    # CITY MARKET TABLE
    # --------------------------------------------------------

    st.subheader(
        "📋 City Market Data"
    )

    city_table = city_market.copy()

    if selected_cities:

        city_table = city_table[
            city_table["City"]
            .astype(str)
            .isin(selected_cities)
        ]

    st.dataframe(
        city_table,
        use_container_width=True,
        hide_index=True
    )


    # --------------------------------------------------------
    # CITY PRICE PER SQFT
    # --------------------------------------------------------

    st.subheader(
        "📐 City Price per Sq.ft"
    )

    sqft_chart = city_sqft.copy()

    sqft_chart[
        "Average_Price_per_sqft"
    ] = pd.to_numeric(
        sqft_chart[
            "Average_Price_per_sqft"
        ],
        errors="coerce"
    )

    if selected_cities:

        sqft_chart = sqft_chart[
            sqft_chart["City"]
            .astype(str)
            .isin(selected_cities)
        ]

    sqft_chart = sqft_chart.dropna(
        subset=[
            "Average_Price_per_sqft"
        ]
    )

    sqft_chart = sqft_chart.sort_values(
        "Average_Price_per_sqft"
    )

    if not sqft_chart.empty:

        fig, ax = plt.subplots(
            figsize=(10, 6)
        )

        ax.barh(
            sqft_chart["City"].astype(str),
            sqft_chart[
                "Average_Price_per_sqft"
            ]
        )

        ax.set_title(
            "Average Price per Sq.ft by City"
        )

        ax.set_xlabel(
            "Average Price per Sq.ft (₹)"
        )

        ax.set_ylabel(
            "City"
        )

        fig.tight_layout()

        st.pyplot(
            fig,
            use_container_width=True
        )

        plt.close(fig)


# ============================================================
# LOCATION TAB
# ============================================================

with location_tab:

    st.header(
        "📍 Location Analysis"
    )


    # --------------------------------------------------------
    # LOCALITY
    # --------------------------------------------------------

    st.subheader(
        "📍 Locality Market Analysis"
    )

    locality_table = locality.copy()

    if selected_cities:

        locality_table = locality_table[
            locality_table["City"]
            .astype(str)
            .isin(selected_cities)
        ]

    st.dataframe(
        locality_table,
        use_container_width=True,
        hide_index=True
    )


    # --------------------------------------------------------
    # RELIABLE LOCALITIES
    # --------------------------------------------------------

    st.subheader(
        "⭐ Reliable Localities"
    )

    reliable_table = reliable_locality.copy()

    if selected_cities:

        reliable_table = reliable_table[
            reliable_table["City"]
            .astype(str)
            .isin(selected_cities)
        ]

    st.dataframe(
        reliable_table,
        use_container_width=True,
        hide_index=True
    )


    # --------------------------------------------------------
    # PRICE VARIABILITY
    # --------------------------------------------------------

    st.subheader(
        "📈 City Price Variability"
    )

    variability_table = variability.copy()

    if selected_cities:

        variability_table = variability_table[
            variability_table["City"]
            .astype(str)
            .isin(selected_cities)
        ]

    st.dataframe(
        variability_table,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# MARKET INSIGHTS TAB
# ============================================================

with insights_tab:

    st.header(
        "💡 Market Insights"
    )

    st.write(
        "Key findings from the prepared analytical datasets."
    )


    # --------------------------------------------------------
    # INSIGHTS
    # --------------------------------------------------------

    insight_items = []

    for _, row in insights.iterrows():

        if "Insight" not in insights.columns:
            continue

        if "Value" not in insights.columns:
            continue

        name = clean_value(
            row["Insight"]
        )

        value = clean_value(
            row["Value"]
        )

        if name:

            insight_items.append(
                (name, value)
            )


    # --------------------------------------------------------
    # DISPLAY INSIGHTS
    # --------------------------------------------------------

    for start in range(
        0,
        len(insight_items),
        3
    ):

        current_items = insight_items[
            start:start + 3
        ]

        columns = st.columns(
            len(current_items)
        )

        for column, item in zip(
            columns,
            current_items
        ):

            name, value = item

            with column:

                st.metric(
                    label=name,
                    value=value
                )


    # --------------------------------------------------------
    # AMENITY ANALYSIS
    # --------------------------------------------------------

    st.divider()

    st.subheader(
        "✨ Amenity Analysis"
    )

    st.write(
        "Property price statistics grouped by amenity count."
    )

    amenity_chart = amenity.copy()

    amenity_chart[
        "AmenitiesCount"
    ] = pd.to_numeric(
        amenity_chart[
            "AmenitiesCount"
        ],
        errors="coerce"
    )

    amenity_chart[
        "Average_Price_Lakhs"
    ] = pd.to_numeric(
        amenity_chart[
            "Average_Price_Lakhs"
        ],
        errors="coerce"
    )

    amenity_chart = amenity_chart.dropna(
        subset=[
            "AmenitiesCount",
            "Average_Price_Lakhs"
        ]
    )

    amenity_chart = amenity_chart.sort_values(
        "AmenitiesCount"
    )

    if not amenity_chart.empty:

        fig, ax = plt.subplots(
            figsize=(10, 5)
        )

        ax.bar(
            amenity_chart[
                "AmenitiesCount"
            ].astype(str),
            amenity_chart[
                "Average_Price_Lakhs"
            ]
        )

        ax.set_title(
            "Average Price by Amenity Count"
        )

        ax.set_xlabel(
            "Number of Amenities"
        )

        ax.set_ylabel(
            "Average Price (₹ Lakhs)"
        )

        fig.tight_layout()

        st.pyplot(
            fig,
            use_container_width=True
        )

        plt.close(fig)


    # --------------------------------------------------------
    # PROPERTY PRICE PER SQFT
    # --------------------------------------------------------

    st.subheader(
        "📐 Property Type Price per Sq.ft"
    )

    st.dataframe(
        property_sqft,
        use_container_width=True,
        hide_index=True
    )


    # --------------------------------------------------------
    # OVERALL MARKET STATISTICS
    # --------------------------------------------------------

    st.subheader(
        "📋 Overall Market Statistics"
    )

    st.dataframe(
        overall,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# ML PREDICTIONS TAB
# ============================================================

with ml_tab:

    st.header(
        "🤖 Machine Learning Price Predictions"
    )

    st.write(
        "Property price predictions generated by the "
        "machine-learning model."
    )


    # --------------------------------------------------------
    # ML SUMMARY
    # --------------------------------------------------------

    ml1, ml2, ml3 = st.columns(3)


    with ml1:

        st.metric(
            "Properties",
            f"{len(filtered):,}"
        )


    with ml2:

        st.metric(
            "Average Prediction",
            format_lakhs(
                filtered[
                    "Predicted_Price_INR"
                ].mean()
            )
        )


    with ml3:

        st.metric(
            "Median Prediction",
            format_lakhs(
                filtered[
                    "Predicted_Price_INR"
                ].median()
            )
        )


    # --------------------------------------------------------
    # PREDICTION TABLE
    # --------------------------------------------------------

    st.subheader(
        "📋 Property-Level Predictions"
    )

    prediction_columns = [
        "ListingID",
        "City",
        "Locality",
        "PropertyType",
        "BHK",
        "Bathrooms",
        "Furnishing",
        "CarpetArea_sqft",
        "AmenitiesCount",
        "Predicted_Price_INR"
    ]

    available_columns = [
        column
        for column in prediction_columns
        if column in filtered.columns
    ]

    prediction_table = filtered[
        available_columns
    ].copy()


    if "Predicted_Price_INR" in prediction_table.columns:

        prediction_table[
            "Predicted_Price_Lakhs"
        ] = (
            prediction_table[
                "Predicted_Price_INR"
            ] / 100000
        ).round(2)


    st.dataframe(
        prediction_table,
        use_container_width=True,
        hide_index=True
    )


    # --------------------------------------------------------
    # DOWNLOAD
    # --------------------------------------------------------

    download_data = filtered.to_csv(
        index=False
    ).encode("utf-8")


    st.download_button(
        label="⬇️ Download Filtered Predictions",
        data=download_data,
        file_name="filtered_real_estate_predictions.csv",
        mime="text/csv"
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Real Estate Analytics Dashboard | "
    "Data Analysis | Machine Learning | Market Insights"
)