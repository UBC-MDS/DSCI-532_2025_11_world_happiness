from dash import dcc, html
from components.data import all_features, all_countries, all_years, all_continents

dropdown_multi_cat = html.Div([
    dcc.Dropdown(
        id='dropdown_multi_cat',
        options=all_features,
        multi=True,
        placeholder='Select 3 to 5 categories...',
        value=[],  # Initially no options selected
    )
])

dropdown_countries = html.Div([
    dcc.Dropdown(
        id='dropdown_countries',
        options=all_countries,
        multi=True,
        placeholder='Select up to 3 countries...',
        value=[],  # Initially no options selected
    )
])

dropdown_year = html.Div([
    dcc.Dropdown(
    id="year-dropdown",
    options = all_years,
    value=2024,
    clearable = False
    )
])

dropdown_feature_line_chart = html.Div([
    dcc.Dropdown(
    id="line-chart-feature-dropdown",
    options = all_features,
    value="Happiness Score",
    clearable = False
    )
])

dropdown_continents = html.Div([
        dcc.Dropdown(
        id="continent-dropdown",
        options = all_continents,
        value='All Continents',
        clearable = False
    )
])