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
            dbc.Col(html.H1('World Happiness Dashboard',
                            style={
                                "text-align": "center",
                                "color": "midnightblue",
                                "font-weight": "bold"
                            }), width=15),
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
            
        # Side column
        dbc.Row([
            dbc.Col(
                html.Div([
                    html.H4("Filters"),
                    html.Label("Select Year"),
                    dropdown_year,
                    html.Label("Select Continent"),
                    dropdown_continents,
                    html.Label("Select Feature"),
                    dropdown_feature_line_chart,
                    html.Div(
                        html.Label(
                            'The World Happiness Dashboard provides an overview of countries and continents on economical, '
                            'political factors that contribute to life quality and satisfaction. Additionally,'
                            'an overall "Happiness Score" is provided for each country. '
                            'You can apply filtering criteria such as GDP, Perception of Corruption or other factors that '
                            'matter to you and see how countries compare to each other over the past 5 years. '
                            'This app is developed by Yuhan Fan, Sepehr Heydarian, Jessica Kuo, and Susannah Sun, and deployed on Mar 1, 2025.',
                            style={"font-size": "13px", "color": "dimgray", "margin-top": "50px"}
                        )
                    )
                ],style={'background-color': 'whitesmoke'}),
                width=2
            ),
            # Main column
            dbc.Col(
                html.Div([
                    dbc.Row([
                        dbc.Col(dvc.Vega(id='map', spec={}), width=12, className="p-0")
                    ], justify="center"),

                    dbc.Row([
                        dbc.Col(
                            html.Div([
                                html.H4("Continental Statistics"),
                                dcc.Graph(id="line-chart")
                            ]),
                            width=7
                        ),
                        dbc.Col(
                            html.Div([
                                html.H4("Compare Your Favorite Countries"),
                                dropdown_multi_cat,
                                dropdown_countries,
                                html.Div(id="radar-chart-container"),
                                html.Div(id="message-container")
                            ]),
                            width=5
                        ),
                    ]),
                ]),
                width=10
            )
        ])
    ], fluid=True)
], style={"background-color": "ghostwhite"})
