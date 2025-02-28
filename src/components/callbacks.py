from dash.dependencies import Input, Output
from dash import html, dcc

#from components.data import all_cats, radar_dummy
from components.charts import line_chart
import pandas as pd
import plotly.express as px

def register_callbacks(app):
   # # No more than 5 categories can be selected
   # @app.callback(
   # [Output('dropdown_multi_cat', 'value'),
   #  Output('dropdown_multi_cat', 'options')],
   # [Input('dropdown_multi_cat', 'value')]  # Listen to changes in the dropdown's selected values
   # )
   # def limit_selected_values(selected_values):
   #     if len(selected_values) == 5:        
   #         updated_options = [option for option in all_cats if option['value'] in selected_values]
   #     else:
   #         updated_options = all_cats
   #     
   #     return selected_values, updated_options  # Return both the updated values and options
   # 
   # # Create radar chart
   # @app.callback(
   #     [Output('radar-chart-container', 'children'),
   #     Output('message-container', 'children')],
   #     [Input('dropdown_multi_cat', 'value'),
   #     Input('dropdown_countries', 'value')]
   #)
    #def update_radar_chart(selected_categories, selected_countries):
    #    
    #    # If not 3-5 categories or more than 1 country selected, display message
    #    if len(selected_categories) < 3 or len(selected_countries) < 2:
    #        return None, html.Label('Choose 3-5 categories and more than 1 country')
    #        # return go.Figure()
    #    
    #    # Filter the data based on selected categories
    #    selected_categories.append('Country')
    #    filtered_df = radar_dummy.loc[:, radar_dummy.columns.isin(selected_categories)]
    #    filtered_df = filtered_df[filtered_df['Country'].isin(selected_countries)]
    #    
    #    return dcc.Graph(id='radar-chart', figure=radar_chart(filtered_df)), None
    
    # Line chart added (Sepehr)
    @app.callback(
        [Output('line-chart', 'figure')],
        [Input('feature-dropdown', 'value'),
        Input('region-dropdown', 'value'),
        Input('year-dropdown', 'value')])
    
    def update_line_chart(selected_feature, selected_region, selected_year):
        df = pd.read_csv("data/processed/reporting_world_happiness_dataset.csv")
        filter_df = df[(df["Region"] == selected_region) & (df["Year"] == selected_year)]

        fig = line_chart(filter_df, selected_feature)

        return [fig]

