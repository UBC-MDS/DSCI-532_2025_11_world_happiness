import pandas as pd

radar_dummy = pd.read_csv('data/dummy.csv')

all_cats = options=[{'label': cat, 'value': cat} for cat in list(radar_dummy)[1:]]
all_countries = options=[{'label': country, 'value': country} for country in radar_dummy['Country']]