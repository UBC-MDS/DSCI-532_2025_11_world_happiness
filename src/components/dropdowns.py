from dash import dcc, html
from components.data import all_cats, all_countries

dropdown_multi_cat = html.Div([
    dcc.Dropdown(
        id='dropdown_multi_cat',
        options=all_cats,
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
        placeholder='Select multiple countries...',
        value=[],  # Initially no options selected
    )
])