from dash import html

from components.sliders import year_slider_tab1, year_slider_tab2
from components.dropdowns import dropdown_multi_cat, dropdown_countries, dropdown_feature_line_chart, dropdown_continents

side_bar_overview = html.Div([
    html.Label("Year", className='select'),
    year_slider_tab1,
    html.Label("Continent", className='select'),
    dropdown_continents,
    html.Label("Category", className='select'),
    dropdown_feature_line_chart,
    html.Div(
        html.Label([
            'The World Happiness Dashboard provides an overview of countries and continents on economical, political factors that contribute to life quality and satisfaction.', html.Br(), html.Br(),
            'Each category is valued between 0 and 1 using Min-Max Scaling. This normalization allows for comparison between categories on the same scale.', html.Br(), html.Br(),
            'Example: Perception of Corruption represents how corrupt people perceive the government or institutions to be:',
            html.Br(), html.Br(),
            '0: Country with least corruption.', html.Br(),
            '1: Country with most corruption.'],
            style={"font-size": "13px", "margin-top": "3em", 'color': 'dimgray'}
        )
    ),
])

side_bar_compare_countries = html.Div([
    html.Div(
        html.Label([
            'The radar chart illustrates ',
            ' differences among different categories ',
            'for selected countries.', html.Br(), html.Br(),
        ], style={"font-size": "13px", "margin-top": "3em", 'color': 'dimgray'})
    ),
    html.Label("Year", className='select'),
    year_slider_tab2,
    html.Label("Countries", className='select'),
    dropdown_countries,
    html.Label("Category", className='select'),
    dropdown_multi_cat
])