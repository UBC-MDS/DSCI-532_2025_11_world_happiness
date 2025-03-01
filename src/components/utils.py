import altair as alt
import pandas as pd

from components.data import geo_countries, happiness_data

new_world_countries = pd.merge(geo_countries, happiness_data, on="Country", how="left")
new_world_countries = new_world_countries[new_world_countries["Year"] == 2024]

hover = alt.selection_point(fields=['Country'], on='pointerover', empty=False)

chart = alt.Chart(new_world_countries, width=600).mark_geoshape().encode(
    color=alt.Color('Happiness Score', scale=alt.Scale(scheme='redyellowgreen'), legend=alt.Legend(title='Happiness Score')),
    tooltip=['Country', alt.Tooltip('Happiness Score', format='.2f')],
    stroke=alt.condition(hover, alt.value('white'), alt.value('#222222'))
).configure(background='transparent').add_params(hover).interactive()

world_map = chart.to_dict(format='vega')
