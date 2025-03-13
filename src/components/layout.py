from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_vega_components as dvc

from components.dropdowns import dropdown_multi_cat, dropdown_countries, dropdown_feature_line_chart, dropdown_continents
from components.sliders import year_slider_tab1, year_slider_tab2

features = ["Happiness Score", "GDP per Capita", "Social Support", "Healthy Life Expectancy", "Freedom to Make Life Choices",
            "Generosity", "Perceptions of Corruption"]


layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1('World Happiness Dashboard',
                            style={
                                "text-align": "center",
                                "font-weight": "bold",
                            }), width=15, style={'padding': '10px'}),
            ]),
        
        dbc.Row([
            dbc.Col([
                html.Div([
                    dbc.Tabs([
                        dbc.Tab([
                            dbc.Row([
                                dbc.Col(
                                    html.Div([
                                        html.Label("Year", className='select'),
                                        year_slider_tab1,
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
                                    ]), width = 3, className='side-bar'
                                ),
                                dbc.Col(
                                    html.Div([
                                        dbc.Row([
                                            dbc.Col(dvc.Vega(id='map', spec={}), width=12, className="p-0")
                                        ]),
                                        dbc.Row([
                                            dbc.Col(
                                                html.Div([
                                                    dcc.Graph(id = "line-chart")
                                                ]), width = 12,
                                            )
                                        ])
                                    ]), width = 9
                                )
                            ])
                        ], label = "Overview", tab_id="tab1", active_label_style={"color": "#3182bd"}, label_style={"color": "dimgray"}),
                        
                        dbc.Tab([
                            dbc.Row([                         
                                dbc.Col(
                                    html.Div([
                                        html.Label("Year", className='select'),
                                        year_slider_tab2,
                                        html.Label("Countries", className='select'),
                                        dropdown_countries,
                                        html.Label("Category", className='select'),
                                        dropdown_multi_cat,
                                        html.Div(
                                            html.Label([
                                                'A radar chart is generated to illustrate ',
                                                'the differences among the selected attributes ',
                                                'across the chosen countries.', html.Br(), html.Br(),
                                                'No continent constraints. '
                                                'Users can compare countries across all continents.'
                                            ], style={"font-size": "13px", "margin-top": "3em", 'color': 'dimgray'})
                                        )
                                    ]), width = 3, className='side-bar'
                                ),
                                
                                dbc.Col(
                                    html.Div([
                                        #html.H4("Compare Countries from Any Continent"),
                                        html.Div(id="message-container", 
                                                 style={'color': '#3182bd',
                                                        'position': 'fixed',
                                                        'top': '50%',
                                                        'left': '50%',
                                                        'transform': 'translate(-50%, -50%)',
                                                        'text-align': 'center'}),
                                        
                                        html.Div(id="radar-chart-container"),
                                        
                                    ]), 
                                    width = 9, 
                                    style = {'margin-bottom': '2em'}
                                )
                            ]),
                        ], label = "Compare Countries", tab_id="tab2", active_label_style={"color": "#3182bd"}, label_style={"color": "dimgray"})
                    ],
                    id="tabs",
                    active_tab="tab1",
                    className="justify-content-center" 
                )
                ])
            ])
        ])
    ], fluid=True)
])