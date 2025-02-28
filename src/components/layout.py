from dash import html, dcc
import dash_bootstrap_components as dbc

from components.dropdowns import dropdown_multi_cat, dropdown_countries
from components.slider import slider


# Load df
import pandas as pd
df = pd.read_csv("data/processed/reporting_world_happiness_dataset.csv")
features = ["Ladder Score", "GDP per Capita", "Social Support", "Healthy Life Expectancy", "Freedom to Make Life Choices",
            "Generosity", "Perceptions of Corruption"]


layout = html.Div([
    dbc.Container([
    #    dbc.Row([
    #        dbc.Col(
    #            # Step 2
    #            html.Div(
    #                children=[
    #                    html.Label('Top Results'),
    #                    slider
    #                ]
    #            ),
    #            width=4
    #        ),
    #        dbc.Col(
    #            # Step 3, 4, 5
    #           html.Div(
    #                children=[
    #                    html.Label('Step 3: Choose 5 categories that matter most'),
    #                    dropdown_multi_cat,
    #                    html.Label('Step 4: Choose your favorite countries'),
    #                    dropdown_countries,
    #                    html.Label('Step 5: See results'),
    #                    html.Div(id='radar-chart-container'),
    #                    html.Div(id='message-container')
    #                ]
    #            ),
    #            width=4
    #        )
     #   ]),
        # Dropdown for line chart (Sepehr)
        dbc.Row([
            dbc.Col(
                html.Div([
                    html.H3("Feature Trend Line Chart"),
                    # Dropdown for features
                    dcc.Dropdown(
                        id="feature-dropdown",
                        options = [{"label": col, "value": col} for col in features],
                        value="Ladder Score",
                        clearable = False
                    ),
                    # Dropdown for region
                    dcc.Dropdown(
                        id="region-dropdown",
                        options = [{"label": region, "value": region} for region in df["Region"].unique()],
                        value=df["Region"].unique()[0],
                        clearable = False
                    ),
                    # Dropdown for year
                    dcc.Dropdown(
                        id="year-dropdown",
                        options = [{"label": year, "value": year} for year in sorted(df["Year"].unique())],
                        value=2024,
                        clearable = False
                    ),
                    dcc.Graph(id="line-chart")
                ]),
            )
        ])
])
])