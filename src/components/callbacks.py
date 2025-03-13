from dash.dependencies import Input, Output
from dash import html, dcc
from components.charts import line_chart, radar_chart, map_viz
from components.data import happiness_data, radar_data, all_features, all_countries, geo_countries, load_happiness_data, filter_happiness_data
import pandas as pd
import altair as alt
alt.data_transformers.enable('vegafusion')


def register_callbacks(app):
   # No more than 5 categories can be selected
   @app.callback(
   [Output('dropdown_multi_cat', 'value'),
    Output('dropdown_multi_cat', 'options')],
   [Input('dropdown_multi_cat', 'value')]  # Listen to changes in the dropdown's selected values
   )
   def limit_selected_values(selected_values):
       if len(selected_values) == 5:        
           updated_options = [option for option in all_features if option['value'] in selected_values]
       else:
           updated_options = all_features
       
       return selected_values, updated_options  # Return both the updated values and options
   
    # No more than 3 countries can be selected
   @app.callback(
   [Output('dropdown_countries', 'value'),
    Output('dropdown_countries', 'options')],
   [Input('dropdown_countries', 'value')]  # Listen to changes in the dropdown's selected values
   )
   def limit_selected_values(selected_values):
       if len(selected_values) == 3:        
           updated_options = [option for option in all_countries if option['value'] in selected_values]
       else:
           updated_options = all_countries
       
       return selected_values, updated_options  # Return both the updated values and options   
   
   # Create radar chart
   @app.callback(
       [Output('radar-chart-container', 'children'),
       Output('message-container', 'children')],
       [Input('dropdown_multi_cat', 'value'),
       Input('dropdown_countries', 'value'),
       Input('year_slider_2', 'value')]
   )
   def update_radar_chart(selected_categories, selected_countries, selected_year):
    
    # If not 3-5 categories or more than 1 country selected, display message
    if len(selected_categories) < 3 or len(selected_countries) < 2:
        return None, html.Label('Please select 3-5 categories and up to 3 countries to see the radar chart.')
    
    # Filter the data based on selected categories
    selected_categories.append('Country')
    filtered_df = happiness_data.loc[:, happiness_data.columns.isin(selected_categories)]
    filtered_df = filtered_df[(filtered_df['Country'].isin(selected_countries)) & (happiness_data["Year"] == selected_year)]
    
    return dcc.Graph(id='radar-chart', figure=radar_chart(filtered_df)), None
   
   # Create line chart 
   @app.callback(
    [Output('line-chart', 'figure')],
    [Input('line-chart-feature-dropdown', 'value'),
    Input('continent-dropdown', 'value'),
    Input('year_slider_1', 'value')])   
   def update_line_chart(selected_feature, selected_continent, selected_year):
    filtered_df = filter_happiness_data(selected_year, selected_continent)
    fig = line_chart(filtered_df, selected_feature, selected_continent)
    return [fig]
   
   # Display map
   @app.callback(
    Output('map', 'spec'),
    [Input('line-chart-feature-dropdown', 'value'),
    Input('continent-dropdown', 'value'),
    Input('year_slider_1', 'value')]
    )
   def map(selected_feature, selected_continent, selected_year):
    filter_df = filter_happiness_data(selected_year, selected_continent)
    filtered_df = pd.merge(geo_countries, filter_df, on="Country", how="left")

    return map_viz(geo_countries, filtered_df, selected_feature)