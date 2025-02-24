from dash import dcc

slider = dcc.Slider(
    min=5, 
    max=15,         
    step=None,
    value=5,    # Default value
    marks={5: '5', 10: '10', 15: '15'},
)