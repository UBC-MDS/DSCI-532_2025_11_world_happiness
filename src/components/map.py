import geopandas as gpd
import altair as alt
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
from dash import Dash, html, dcc, Input, Output, callback
import pandas as pd
from data_map import happiness_data, world_countries


# Initiatlize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

alt.data_transformers.enable('vegafusion')

# Layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(dcc.Dropdown(id='year_select', 
                             options=[2020, 2021, 2022, 2023, 2024], 
                             value = 2020,
                             placeholder='Select a Year...'), 
                md=2)]),
    dbc.Row([
        dbc.Col(dcc.Dropdown(id='continent_select', 
                             options=happiness_data['Continent'].unique(), 
                             value = None,
                             placeholder='Select a Continent...'), 
                md=2),

        dbc.Col([
            dvc.Vega(id='scatter', spec={}),  
        ], md=10)
    ])
], fluid=True)


@callback(
    Output('scatter', 'spec'),
    Input('year_select', 'value'),
    Input('continent_select', 'value')
)

def map(year_select, continent_select):
    new_happiness = happiness_data[happiness_data['Year'] == year_select]
    
    if continent_select is not None:
        new_happiness = new_happiness[new_happiness['Continent'] == continent_select]
    
    new_world_countries = world_countries.merge(new_happiness)

    hover = alt.selection_point(fields=['Country'], on='pointerover', empty=False)
    chart = alt.Chart(new_world_countries, width=600).mark_geoshape().encode(
        color=alt.Color('Ladder Score', scale=alt.Scale(scheme='redyellowgreen'), legend=alt.Legend(title='Happiness Score')),
        tooltip=['Country', alt.Tooltip('Ladder Score', format='.2f')],
        stroke=alt.condition(hover, alt.value('white'), alt.value('#222222'))
    ).configure(
        background='transparent'
    ).add_params(
        hover
    ).interactive()
    
    return chart.to_dict(format='vega')


# Run the app/dashboard
if __name__ == '__main__':
    app.run(debug=True)