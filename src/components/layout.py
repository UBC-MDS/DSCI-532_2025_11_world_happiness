from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_vega_components as dvc

from components.dropdowns import dropdown_multi_cat, dropdown_countries, dropdown_feature_line_chart, dropdown_continents
from components.sliders import year_slider

features = ["Happiness Score", "GDP per Capita", "Social Support", "Healthy Life Expectancy", "Freedom to Make Life Choices",
            "Generosity", "Perceptions of Corruption"]

layout = html.Div([
    dbc.Container([
        # App title
        dbc.Row([
            dbc.Col(html.H1('World Happiness Dashboard',
                            style={
                                "text-align": "center",
                                "font-weight": "bold",
                            }), width=15, style={'padding': '10px'}),
            ]),

        # Side column
        dbc.Row([
            dbc.Col(
                html.Div([
                    # html.H4("Filters"),
                    html.Label("Year", className='select'),
                    year_slider,
                    html.Label("Continent", className='select'),
                    dropdown_continents,
                    html.Label("Category", className='select'),
                    dropdown_feature_line_chart,
                    html.Div(
                        html.Label([
                            'The World Happiness Dashboard provides an overview of countries and continents on economical, ',
                            'political factors that contribute to life quality and satisfaction. Additionally,',
                            'an overall "Happiness Score" is provided for each country.', html.Br(), html.Br(),
                            'You can apply filtering criteria such as GDP, Perception of Corruption or other factors that ',
                            'matter to you and see how countries compare to each other over the past 5 years. ', html.Br(), html.Br(),
                            'This app is developed by Yuhan Fan, Sepehr Heydarian, Jessica Kuo, and Susannah Sun, and deployed on Mar 1, 2025.'],
                            style={"font-size": "13px", "margin-top": "3em", 'color': 'dimgray'}
                        )
                    )
                ]),
                width=2,
                style={
                    "position": "fixed",  # Stays in place while scrolling
                    "top": "30px",  # Distance from the top
                    "right": "10px",  # Distance from the right
                    "padding": "10px",
                    "z-index": "1000",  # Ensures it stays on top
                }
            ),
            # Main column
            dbc.Col(
                html.Div([
                    dbc.Row([
                        dbc.Col(dvc.Vega(id='map', spec={}), width=10, className="p-0")
                    ]),

                    dbc.Row([
                        dbc.Col(
                            html.Div([
                                dcc.Graph(id="line-chart")
                            ]), width=10
                        )
                    ]),

                    dbc.Row([
                        dbc.Col(
                            html.Div([
                                html.H4("Compare Countries from Any Continent"),
                                html.Div(id="message-container", style={'color': '#3182bd'}),
                            ]), width=10, style={'margin-bottom': '2em'}
                        )
                    ]),
                    dbc.Row([
                        dbc.Col(dropdown_multi_cat, width=5),  # 50% width for the first dropdown
                        dbc.Col(dropdown_countries, width=5)    # 50% width for the second dropdown
                    ]),
                    dbc.Row([
                        dbc.Col(
                            html.Div(id="radar-chart-container"),
                            width=10, style={'min-height': '150px'}
                        )
                    ])
        ])
            )
            ])
    ], fluid=True, style={"background-color": "white", 'padding': '10px', 'textAlign': 'center'})
])