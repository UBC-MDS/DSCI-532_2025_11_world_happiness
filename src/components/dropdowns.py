from dash import dcc, html
from components.data import all_features, all_countries, all_continents

dropdown_multi_cat = html.Div([
    dcc.Dropdown(
        id='dropdown_multi_cat',
        options=all_features,
        multi=True,
        placeholder='Select 3 to 5 categories...',
        value=['GDP per Capita', 'Social Support', 'Freedom to Make Life Choices', 'Perceptions of Corruption', 'Healthy Life Expectancy'],  # Initially no options selected
        style={"font-size": "1em", 'color': 'dimgray'}
    )
])

dropdown_countries = html.Div([
    dcc.Dropdown(
        id='dropdown_countries',
        options=all_countries,
        multi=True,
        placeholder='Select up to 3 countries...',
        value=['Canada', 'Australia', 'France'],  # Initially no options selected
        style={"font-size": "1em", 'color': 'dimgray'}
    )
])

dropdown_feature_line_chart = html.Div([
    dcc.Dropdown(
    id="line-chart-feature-dropdown",
    options = all_features,
    value="Happiness Score",
    clearable = False,
    style={"font-size": "12px", 'color': 'dimgray'}
    )
])

dropdown_continents = html.Div([
        dcc.Dropdown(
        id="continent-dropdown",
        options = all_continents,
        value='All Continents',
        clearable = False,
        style={"font-size": "12px", 'color': 'dimgray'}
    )
])