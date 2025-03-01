from dash import html, dcc
import dash_bootstrap_components as dbc

from components.dropdowns import dropdown_multi_cat, dropdown_countries, dropdown_year, dropdown_feature_line_chart, dropdown_continents
from components.data import happiness_data

import pandas as pd

features = ["Happiness Score", "GDP per Capita", "Social Support", "Healthy Life Expectancy", "Freedom to Make Life Choices",
            "Generosity", "Perceptions of Corruption"]


layout = html.Div([
    dbc.Container([
        # Step 1 - top level filters
        dbc.Row([
            dbc.Col(dropdown_year, width=6),
            dbc.Col(dropdown_continents, width=6),
            ]),
        # Step 1 - map
        dbc.Row([
            # map - TODO!!
            ]),
        dbc.Row([
            # Column 1: Feature Trend Line Chart
            dbc.Col(
                html.Div([
                    html.H3("Regional Statistics"),
                    dropdown_feature_line_chart,
                    # dropdown_region,
                    dcc.Graph(id="line-chart")
                ]),
                width=6
            ),

            # Column 2: Steps 3, 4, 5
            dbc.Col(
                html.Div([
                    html.H3("Compare Your Favourite Countries"),
                    dropdown_multi_cat,
                    dropdown_countries,
                    html.Div(id='radar-chart-container'),
                    html.Div(id='message-container')
                ]),
                width=6
            )
        ])
    ])
])