from dash import dcc, html
from components.data import all_years

year_values = [int(option["value"]) for option in all_years]

min_year = min(year_values)
max_year = max(year_values)

year_slider_tab1 = html.Div([
    dcc.Slider(
        id="year_slider_1",
        min=min_year,
        max=max_year,
        step=1,
        value=max_year,  # Default selected year
        marks={int(year): str(year) for year in year_values},
        included=False
    )
])

year_slider_tab2 = html.Div([
    dcc.Slider(
        id="year_slider_2",
        min=min_year,
        max=max_year,
        step=1,
        value=max_year,  # Default selected year
        marks={int(year): str(year) for year in year_values},
        included=False
    )
])