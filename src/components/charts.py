import plotly.graph_objects as go
import plotly.express as px
import altair as alt
import functools
from components.data import filter_happiness_data
from components.chart_utils import split_label, convert_legend

def radar_chart(filtered_df):
   fig = go.Figure()
   
   for country in filtered_df['Country'].unique():
       country_data = filtered_df[filtered_df['Country'] == country].drop(columns=['Country']).iloc[0]
       fig.add_trace(go.Scatterpolar(
           r=country_data.values,
           theta=[split_label(label) for label in country_data.index],
           fill='toself',
           name=split_label(convert_legend(country)),
           hovertemplate="<b>%{text}</b><br>%{theta}: %{r:.2f}",
           text=[country] * len(country_data), 
       ))

   # Reorder traces to ensure smaller countries' traces are on top
   fig.data = sorted(fig.data, key=lambda trace: max(trace['r']), reverse=True)
   
   fig.update_layout(
       showlegend=True,
       width=1000,  # Set the width of the chart
       height=800,  # Set the height of the chart
       polar=dict(
           bgcolor='#F2F0EF',
           radialaxis=dict(
               visible=True,
               tickfont=dict(
                   size=12,  # Size of the axis labels
                   color='dimgray'  # Color of the axis labels
               ),
           ),
           angularaxis=dict(
               showline=True,  # Show line for axis
               tickfont=dict(
                   size=14,  # Size of the axis labels
                   color='dimgray'  # Color of the axis labels
               ),
               tickvals=[i for i in range(len(filtered_df.columns) - 1)]  # Adjust this to match your number of categories
           )
       )
   )

   return fig

@functools.lru_cache(maxsize=10)
def get_top_10_countries(year, continent, feature):
    """Return top 10 countries for selected feature"""
    df = filter_happiness_data(year, continent)
    return df.nlargest(10, feature)


def line_chart(filtered_df, selected_feature, selected_continent):
    """
    Generate a line chart for the top 10 countries in a region, ranked by the selected feature.
    """
    # Find top 10 countries by feature in region
    year = filtered_df["Year"].iloc[0]
    top_10_countries = get_top_10_countries(year, selected_continent, selected_feature)
    # Find the Average Regional Column
    avg_column = "Average Continent " + selected_feature
    continent_avg = filtered_df[avg_column].iloc[0]

    # Create figure
    fig = px.bar(
        top_10_countries,
        x="Country",
        y=selected_feature,
        title=f"Top Countries by {selected_feature} in {selected_continent}",
        #markers=True,
        hover_data={  
            "Country": False,  # Set to False to avoid the default format
            selected_feature: False,  # Set to False to avoid the default format
            "Continent": False,  # Set to False to avoid the default format
            "Year": False  # Set to False to avoid the default format
        }
     )
    average_line_text = (
        f"Global Average: {continent_avg:.2f}"
        if selected_continent == "All Continents"
        else f"Continent Average: {continent_avg:.2f}"
    )

    # Add average line
    fig.add_hline(
        y=continent_avg, 
        line_dash="dash",
        annotation_text=average_line_text,
        annotation_position="top",  # Keep the position at the top
        line_color="#f1a835",
        annotation=dict(
            x=0.5,  # Set the x position to 50% for center alignment
            xanchor="center",  # Center align the annotation
            showarrow=False,
            font=dict(color="#f1a835", size=14)
        )
                  )
    
    fig.update_layout(
        title={
            'text': f"Top Countries by {selected_feature} in {selected_continent}",
            'x': 0.5,  
            'xanchor': 'center',  
            'yanchor': 'top',  
            'font': {
                'size': 25, 
                'family': 'Helvetica',
                'color': '#f1a835'
            }
        },
            xaxis=dict(
                title='',
                tickfont=dict(color='dimgray'),  # Change x-axis tick font color
                showline=True,  # Show axis line
                linewidth=2,  # Line width of the axis
                linecolor='dimgray',  # Change axis line color
                showgrid=False
            ),
            yaxis=dict(
                title='',
                tickfont=dict(color='dimgray'),  # Change y-axis tick font color
                showline=True,  # Show axis line
                linewidth=2,  # Line width of the axis
                linecolor='dimgray',  # Change axis line color
                ticks='inside',  # Set ticks to be inside the plot
                tickcolor='dimgray',  # Change tick marks color
                showgrid=False
            ),
            plot_bgcolor='white',  # Set the background color of the plot area
            paper_bgcolor='white'  # Set the background color of the whole chart
    )
    customdata=top_10_countries[[selected_feature, "Continent", "Year"]].values
    fig.update_traces(
        marker=dict(color='#3182bd'),
        hovertemplate=(
            "<b>%{x}</b><br>"  # Country
            + f"{selected_feature}: "
            + "<b>%{customdata[0]:.2f}</b><br>"   # Selected feature value
            + "<extra></extra>"  # Removes extra info
            ),
        customdata=customdata
        )

    return fig

def map_viz(base_df, filtered_df, selected_feature):
    hover = alt.selection_point(fields=['Country'], on='pointerover', empty=False)
    
    #full world map
    full_map = alt.Chart(base_df, width=1000, height=800).mark_geoshape().encode(
        color = alt.value("#F2F0EF")
    )

    #filtered map based on continent and year
    filtered_map = alt.Chart(filtered_df, width=1000, height=800).mark_geoshape().encode(
        color=alt.Color(selected_feature, scale=alt.Scale(scheme='blues'),
                        legend=alt.Legend(
                            title=selected_feature,
                                orient='top-right',             
                                titleAnchor='middle',     
                                titleOrient='right',
                                labelAlign='center',     
                                titleColor='dimgray',
                                labelColor='dimgray',    
                                symbolSize=150,           
                                offset=20,
                                zindex=1                
                            )
                        ),
        tooltip=['Country', alt.Tooltip(selected_feature, format='.2f')],
        stroke=alt.condition(hover, alt.value('white'), alt.value('#222222'))
    ).add_params(hover).interactive()
    
    map = full_map + filtered_map

    return map.to_dict(format='vega')