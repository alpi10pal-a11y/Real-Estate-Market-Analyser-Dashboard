# Real Estate Market Analyzer

A Streamlit dashboard for exploring prepared real-estate market analysis and
machine-learning property price predictions.

## Features

- Property overview KPIs, including listing count, predicted prices, area, and
  average BHK.
- Filters for city, property type, BHK, and furnishing.
- Market analysis by city, property type, BHK, amenities, and price per square
  foot.
- Location analysis using locality and city-level datasets.
- Market insights and summary statistics.
- Property-level prediction tables with filtered CSV download.
- Matplotlib charts rendered in the Streamlit interface.

The dashboard uses prepared CSV outputs. It does not train a model at runtime
and does not load `model/best_model.pkl`.

## Setup

1. Use Python 3.10 or newer.
2. Create and activate a virtual environment.
3. Install the dashboard dependencies:

   ```text
   pip install -r requirements.txt
   ```

4. Start the dashboard from the project root:

   ```text
   streamlit run Dashboard/app.py
   ```

The app expects its required data files in `dashboard_data/` relative to the
project root.

## Files required by the deployed dashboard

Include these files in the GitHub repository:

- `.gitignore`
- `README.md`
- `requirements.txt`
- `Dashboard/app.py`
- `Dashboard/analysis.py`
- `Dashboard/charts.py`
- `Dashboard/data_loader.py`
- `Dashboard/utils.py`
- `dashboard_data/real_estate_test_predictions.csv`
- `dashboard_data/city_market_analysis.csv`
- `dashboard_data/city_price_analysis.csv`
- `dashboard_data/city_bhk_analysis.csv`
- `dashboard_data/locality_market_analysis.csv`
- `dashboard_data/reliable_locality_analysis.csv`
- `dashboard_data/property_type_analysis.csv`
- `dashboard_data/bhk_price_analysis.csv`
- `dashboard_data/amenity_price_analysis.csv`
- `dashboard_data/city_price_per_sqft_analysis.csv`
- `dashboard_data/city_price_variability.csv`
- `dashboard_data/property_price_per_sqft_analysis.csv`
- `dashboard_data/overall_market_statistics.csv`
- `dashboard_data/market_insights.csv`

Do not omit or rename any of the 14 required CSV files: the app loads them
using those exact paths and filenames.

## Files not required by the deployed dashboard

These existing files are not loaded by `Dashboard/app.py` and should be
excluded from the GitHub upload unless they are intentionally being preserved
as project research or source material:

- `model/best_model.pkl` (empty and unused)
- `Dataset/test_part1.csv`
- `Dataset/test_part2.csv`
- `Dataset/train_part1.csv`
- `Dataset/train_part2.csv`
- `dashboard_data/dashboard_property_data.csv`
- `dashboard_data/test_predictions.csv` (duplicate prediction export)
- `dashboard_data/House Price Prediction dataset.csv`
- `dashboard_data/Real Estate Data V21.csv`
- `dashboard_data/test_part1.csv`
- `dashboard_data/test_part2.json`
- `dashboard_data/test_part2.xlsx`
- `dashboard_data/test_part1.json`
- `dashboard_data/train_part1.json`
- `dashboard_data/train_part1.xlsx`
- `dashboard_data/train_part2.json`
- `dashboard_data/train_part2.xlsx`
- `dashboard_data/age_analysis.csv`
- `dashboard_data/amenities_analysis.csv`
- `dashboard_data/building_type_analysis.csv`
- `dashboard_data/city_analysis.csv`
- `dashboard_data/city_property_analysis.csv`
- `dashboard_data/feature_importance.csv`
- `dashboard_data/furnishing_analysis.csv`
- `dashboard_data/locality_analysis.csv`
- `dashboard_data/model_comparison.csv`
- `dashboard_data/parking_analysis.csv`
- `dashboard_data/project_structure.txt`
- `dashboard_data/rera_analysis.csv`
- `notebook/Real Estate.ipynb`
- `notebook/basic.ipynb`
- `inside file/Real Estate.ipynb`
- `inside file/basic.ipynb`

The following checkpoint files are excluded by `.gitignore` through the
`.ipynb_checkpoints/` rule:

- `.ipynb_checkpoints/House Price Prediction dataset-checkpoint.csv`
- `.ipynb_checkpoints/Mumbai_property_details-checkpoint.csv`
- `.ipynb_checkpoints/Real Estate Data V21-checkpoint.csv`
- `.ipynb_checkpoints/Real Estate-checkpoint.ipynb`
- `.ipynb_checkpoints/amenity_price_analysis-checkpoint.csv`
- `.ipynb_checkpoints/basic-checkpoint.ipynb`
- `.ipynb_checkpoints/test_part1-checkpoint.csv`
- `.ipynb_checkpoints/train_part1-checkpoint.csv`
- `.ipynb_checkpoints/train_part2-checkpoint.csv`
- `Dashboard/.ipynb_checkpoints/dataloader-checkpoint.py`

The checkpoint CSVs are duplicate copies of source or analysis files; they are
not needed by the deployed dashboard.
