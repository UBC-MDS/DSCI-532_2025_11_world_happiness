import pandas as pd
import geopandas as gpd


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