from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

from components.callbacks import register_callbacks
from components.layout import layout

# Initialize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Expose the Flask server for Flask commands
server = app.server  

# Layout
app.layout = layout

register_callbacks(app)


# Run the app/dashboard
if __name__ == '__main__':
    app.enable_dev_tools(debug=True, dev_tools_hot_reload=True)
    app.run(debug=True, host="127.0.0.1", port=8050, dev_tools_hot_reload=True)