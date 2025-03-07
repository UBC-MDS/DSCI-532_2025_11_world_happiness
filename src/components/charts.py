import plotly.graph_objects as go
import plotly.express as px
import altair as alt

def radar_chart(filtered_df):
   fig = go.Figure()
   
   for country in filtered_df['Country'].unique():
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

   return fig

### Add function for line chart (Sepehr) ###
def line_chart(filtered_df, selected_feature, selected_continent):
    """
    Generate a line chart for the top 10 countries in a region, ranked by the selected feature.
    """
    # Find top 10 countries by feature in region
    top_10_countries = filtered_df.nlargest(10, selected_feature)
    # Find the Average Regional Column
    avg_column = "Average Continent " + selected_feature
    continent_avg = filtered_df[avg_column].iloc[0]

    # Create figure
    fig = px.line(
        top_10_countries,
        x="Country",
        y=selected_feature,
        title=f"Top Countries by {selected_feature} in {selected_continent}",
        markers=True,
        hover_data={  
            "Country": True,
            selected_feature: True,
            "Continent": True,
            "Year": True
        }
     )
    # Add average line
    fig.add_hline(y=continent_avg, line_dash="dash",
                   annotation_text=f"Continent Avg: {continent_avg:.2f}",
                     annotation_position="top left",
                       line_color = "red")
    return fig

def map_viz(base_df, filtered_df):
    hover = alt.selection_point(fields=['Country'], on='pointerover', empty=False)
    
    #full world map
    full_map = alt.Chart(base_df, width=1100).mark_geoshape().encode(
        color = alt.value("lightgrey")
    )

    #filtered map based on continent and year
    filtered_map = alt.Chart(filtered_df, width=1100).mark_geoshape().encode(
        color=alt.Color('Happiness Score', scale=alt.Scale(scheme='redyellowgreen'), legend=alt.Legend(title='Happiness Score')),
        tooltip=['Country', alt.Tooltip('Happiness Score', format='.2f')],
        stroke=alt.condition(hover, alt.value('white'), alt.value('#222222'))
        ).add_params(hover).interactive()
    
    map = full_map + filtered_map

    return map.to_dict(format='vega')