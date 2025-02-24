import pandas as pd

from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
from dash.dependencies import Input, Output

# Initialize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Expose the Flask server for Flask commands
server = app.server  

# Data
radar_dummy = pd.read_csv('dummy.csv')

# Layout
all_cats = options=[{'label': cat, 'value': cat} for cat in list(radar_dummy)[1:]]
all_countries = options=[{'label': country, 'value': country} for country in radar_dummy['Country']]
app.layout = dbc.Container([
        dbc.Row([
            dbc.Col(
                # Step 2
                html.Div(
                    children=[
                        html.Label('Top Results'),
                        dcc.Slider(min=5, 
                                max=15,         
                                step=None,
                                value=5,    # Default value
                                marks={5: '5', 10: '10', 15: '15'},
                                #    tooltip={'placement': 'top', 'always_visible': True}  # Optional: show tooltip
                        )
                    ]
                ),
                width=4
            ),
            dbc.Col(
                # Step 3, 4, 5
                html.Div(
                    children=[
                        html.Label('Step 3: Choose 5 categories that matter most'),
                        dcc.Dropdown(
                            id='dropdown_multi_cat',
                            options=all_cats,
                            multi=True,
                            placeholder='Select 3 to 5 categories...',
                            value=[],  # Initially no options selected
                        ),
                        # html.Div(id='output')  # Display selected items (optional)
                        html.Label('Step 4: Choose your favorite countries'),
                        dcc.Dropdown(
                            id='dropdown_countries',
                            options=all_countries,
                            multi=True,
                            placeholder='Select multiple countries...',
                            value=[],  # Initially no options selected
                        ),
                        html.Label('Step 5: See results'),
                        html.Div(id='radar-chart-container'),
                        html.Div(id='message-container')
                    ]
                ),
                width=4
            )
        ])

])

@app.callback(
    [Output('dropdown_multi_cat', 'value'),
     Output('dropdown_multi_cat', 'options')],
    [Input('dropdown_multi_cat', 'value')]  # Listen to changes in the dropdown's selected values
)
def limit_selected_values(selected_values):
    if len(selected_values) == 5:        
        updated_options = [option for option in all_cats if option['value'] in selected_values]
    else:
        updated_options = all_cats
    
    return selected_values, updated_options  # Return both the updated values and options

@app.callback(
    [Output('radar-chart-container', 'children'),
     Output('message-container', 'children')],
    [Input('dropdown_multi_cat', 'value'),
     Input('dropdown_countries', 'value')]
)
def update_radar_chart(selected_categories, selected_countries):
    
    # If not 3-5 categories or more than 1 country selected, display message
    if len(selected_categories) < 3 or len(selected_countries) < 2:
        return None, html.Label('Choose 3-5 categories and more than 1 country')
        # return go.Figure()
    
    # Filter the data based on selected categories
    selected_categories.append('Country')
    filtered_df = radar_dummy.loc[:, radar_dummy.columns.isin(selected_categories)]
    filtered_df = filtered_df[filtered_df['Country'].isin(selected_countries)]
    
    # Create radar chart
    fig = go.Figure()
    
    for country in filtered_df['Country']:
        country_data = filtered_df[filtered_df['Country'] == country].drop(columns=['Country']).iloc[0]
        fig.add_trace(go.Scatterpolar(
            r=country_data.values,
            theta=country_data.index,
            fill='toself',
            name=country
        ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 60]
            )
        ),
        showlegend=True,
    )
    return dcc.Graph(id='radar-chart', figure=fig), None


# Run the app/dashboard
if __name__ == '__main__':
    app.enable_dev_tools(debug=True, dev_tools_hot_reload=True)
    app.run(debug=True, host="127.0.0.1", port=8050, dev_tools_hot_reload=True)