from dash import html
import dash_bootstrap_components as dbc

from components.dropdowns import dropdown_multi_cat, dropdown_countries
from components.slider import slider


layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(
                # Step 2
                html.Div(
                    children=[
                        html.Label('Top Results'),
                        slider
                    ]
                ),
                width=4
            ),
            dbc.Col(
                # Step 3, 4, 5
                html.Div(
                    children=[
                        html.Label('Step 3: Choose 5 categories that matter most'),
                        dropdown_multi_cat,
                        html.Label('Step 4: Choose your favorite countries'),
                        dropdown_countries,
                        html.Label('Step 5: See results'),
                        html.Div(id='radar-chart-container'),
                        html.Div(id='message-container')
                    ]
                ),
                width=4
            )
        ])
])
])