import pandas as pd
import geopandas as gpd
import os

# happiness data
file_path = os.path.join(os.path.dirname(__file__), "../../data/processed/reporting_happiness_dataset.csv")
happiness_data = pd.read_csv(os.path.abspath(file_path))

cols = ['Happiness Score', 'GDP per Capita', 'Social Support', 'Healthy Life Expectancy', 'Freedom to Make Life Choices', 'Generosity', 'Perceptions of Corruption']
all_features = [{'label': feature, 'value': feature} for feature in cols]
all_countries = [{'label': country, 'value': country} for country in sorted(happiness_data['Country'].unique())]
all_continents = [{'label': 'All Continents', 'value': 'All Continents'}] + [{'label': continent, 'value': continent} for continent in happiness_data['Continent'].unique()]
all_years = [{"label": year, "value": year} for year in sorted(happiness_data["Year"].unique())]

# world country data 
url = "https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip"
geo_countries = gpd.read_file(url)

geo_countries = geo_countries[
    ["NAME", "CONTINENT", 'geometry']
].rename(
    columns = {'NAME': 'Country', 'CONTINENT':'Continent'}
).replace(
    {'Continent': ['North America', 'South America']}, 'Americas'
).query(
    'Continent != "Antarctica"'
)
