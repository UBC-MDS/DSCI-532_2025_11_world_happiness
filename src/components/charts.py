import plotly.graph_objects as go

def radar_chart(filtered_df):
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

    return fig