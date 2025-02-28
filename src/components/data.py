import pandas as pd
import geopandas as gpd


#radar_dummy = pd.read_csv('data/dummy.csv')

#all_cats = options=[{'label': cat, 'value': cat} for cat in list(radar_dummy)[1:]]
#all_countries = options=[{'label': country, 'value': country} for country in radar_dummy['Country']]

# load processed dataset
df = pd.read_csv("data/processed/reporting_world_happiness_dataset.csv")

all_cats = [{"label": col, "value": col} for col in df.columns if col not in ["Country", "Year", "Region", "Continent"]]
all_countries = [{"label": country, "value": country} for country in df["Country"].unique()]

# world country data 
url = "https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip"
world_countries = gpd.read_file(url)

world_countries = world_countries[
    ["NAME", "CONTINENT", 'geometry']
].rename(
    columns = {'NAME': 'Country', 'CONTINENT':'Continent'}
).replace(
    {'Continent': ['North America', 'South America']}, 'Americas'
).query(
    'Continent != "Antarctica"'
)

# happiness data
happiness_data = pd.read_csv("../../data/processed/reporting_world_happiness_dataset.csv")

