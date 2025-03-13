from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_vega_components as dvc

from components.sidebars import side_bar_overview, side_bar_compare_countries


features = ["Happiness Score", "GDP per Capita", "Social Support", "Healthy Life Expectancy", "Freedom to Make Life Choices",
            "Generosity", "Perceptions of Corruption"]


layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1('World Happiness Dashboard',
                            style={
                                "text-align": "center",
                                "font-weight": "bold",
                            }), width=15, style={'padding': '2em'})
            ]),
        
        dbc.Row([
            dbc.Col([
                html.Div([
                    dbc.Tabs([
                        dbc.Tab([
                            dbc.Row([
                                dbc.Col(side_bar_overview, width = 3, className='side-bar'),
                                dbc.Col(
                                    html.Div([
                                        dbc.Row([
                                            dcc.Loading(  
                                                id="loading-map",
                                                type="circle",  
                                                children=[dbc.Col(dvc.Vega(id='map', spec={}), width=12, className="p-1")]
                                            )
                                        ]),
                                        dbc.Row([
                                            dcc.Loading(  
                                                id="loading-line-chart",
                                                type="circle",  
                                                children=[dcc.Graph(id = "line-chart")]
                                            )
                                        ]),
                                        dbc.Row([
                                            dbc.Col(
                                                html.Div(
                                                    html.Label([
                                                        'This app is developed by Yuhan Fan, Sepehr Heydarian, Jessica Kuo, and Susannah Sun, and deployed on Mar 1, 2025. Data from Gallup World Poll.'],
                                                        style={"font-size": "13px", 'color': 'dimgray', 'padding': '3em'}
                                                    )
                                                ), width = 12,
                                            )
                                        ])
                                    ]), width = 9
                                )
                            ])
                        ], label = "Overview", tab_id="tab1", active_label_style={"color": "#3182bd"}, label_style={"color": "dimgray"}),
                        
                        dbc.Tab([
                            dbc.Row([                         
                                dbc.Col(side_bar_compare_countries, width = 3, className='side-bar'
                                ),
                                dcc.Loading(  
                                    id="loading-radar-chart",
                                    type="circle",  
                                    children=[
                                        dbc.Col(
                                            html.Div([
                                                html.Div(id="message-container", 
                                                        style={'color': '#3182bd',
                                                                'position': 'fixed',
                                                                'top': '50%',
                                                                'left': '40%',
                                                                'transform': 'translate(-50%, -50%)',
                                                                'text-align': 'center'}),
                                                
                                                html.Div(id="radar-chart-container"),
                                                
                                            ]), 
                                            width = 9, 
                                            style = {'margin-bottom': '2em'}
                                        )
                                    ]
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