import pandas as pd
import geopandas as gpd
from sklearn.preprocessing import MinMaxScaler
import os

file_path = os.path.join(os.path.dirname(__file__), "../../data/processed/World_Happiness_processed_data.csv")

# app data
happiness_data = pd.read_csv(os.path.abspath(file_path))

cols = ['Happiness Score', 'GDP per Capita', 'Social Support', 'Healthy Life Expectancy', 'Freedom to Make Life Choices', 'Generosity', 'Perceptions of Corruption']
all_features = [{'label': feature, 'value': feature} for feature in cols]
all_countries = [{'label': country, 'value': country} for country in sorted(happiness_data['Country'].unique())]
all_continents = [{'label': 'All Continents', 'value': 'All Continents'}] + [{'label': continent, 'value': continent} for continent in happiness_data['Continent'].unique()]
all_years = [{"label": year, "value": year} for year in sorted(happiness_data["Year"].unique())]

# map data 
file_path_geo = os.path.join(os.path.dirname(__file__), "../../data/processed/world_countries.parquet")
geo_countries = gpd.read_parquet(os.path.abspath(file_path_geo))

geo_countries = geo_countries[
    ["Country", "Continent", 'geometry']
].replace(
    {'Continent': ['North America', 'South America']}, 'Americas'
).query(
    'Continent != "Antarctica"'
)