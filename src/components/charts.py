import plotly.graph_objects as go
import plotly.express as px

#def radar_chart(filtered_df):
#    fig = go.Figure()
#    
#    for country in filtered_df['Country']:
#        country_data = filtered_df[filtered_df['Country'] == country].drop(columns=['Country']).iloc[0]
#        fig.add_trace(go.Scatterpolar(
#            r=country_data.values,
#            theta=country_data.index,
#            fill='toself',
#            name=country
#        ))
#    
#    fig.update_layout(
#        polar=dict(
#            radialaxis=dict(
#                visible=True,
#                range=[0, 60]
#            )
#        ),
 #       showlegend=True,
  #  )
#
#    return fig

### Add function for line chart (Sepehr) ###
def line_chart(filtered_df, selected_feature):
    """
    Generate a line chart for the top 10 countries in a region, ranked by the selected feature.
    """
    # Find top 10 countries by feature in region
    top_10_countries = filtered_df.nlargest(10, selected_feature)
    # Find the Average Regional Column
    avg_column = "Average Regional " + selected_feature
    regional_avg = filtered_df[avg_column].iloc[0]

    # Create figure
    fig = px.line(
        top_10_countries,
        x="Country",
        y=selected_feature,
        title=f"Top 10 Countries by {selected_feature}",
        markers=True,
        hover_data={  
            "Country": True,
            selected_feature: True,
            "Region": True,
            "Year": True
        }
     )
    # Add average line
    fig.add_hline(y=regional_avg, line_dash="dash",
                   annotation_text="Regional Avg",
                     annotation_position="top left",
                       line_color = "red")
    return fig