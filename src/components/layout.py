from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_vega_components as dvc

from components.dropdowns import dropdown_multi_cat, dropdown_countries, dropdown_year, dropdown_feature_line_chart, dropdown_continents

features = ["Happiness Score", "GDP per Capita", "Social Support", "Healthy Life Expectancy", "Freedom to Make Life Choices",
            "Generosity", "Perceptions of Corruption"]


layout = html.Div([
    dbc.Container([
        # App title
        dbc.Row([
            dbc.Col(html.H1('World Happiness Dashboard'), width=10),
            ]),
        # Step 1 - top level filters
        dbc.Row([
            dbc.Col(dropdown_year, width=6),
            dbc.Col(dropdown_continents, width=6),
            ]),
        # Step 1 - map
        dbc.Row([
            dbc.Col(dvc.Vega(id='map', spec={}), width=12, className="p-0")
        ], justify="center"),
        dbc.Row([
            # Step 2 - Line Chart
            dbc.Col(
                html.Div([
                    html.H3("Regional Statistics"),
                    dropdown_feature_line_chart,
                    dcc.Graph(id="line-chart")
                ]),
                width=6
            ),

            # Step 3, 4, 5 - Radar Chart
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
    ], fluid=True)
])
