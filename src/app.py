from dash import Dash
import dash_bootstrap_components as dbc

import sys
import os

# Ensure the 'src' directory is in the Python path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

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
    app.run()
    #app.run(debug=False)
    #app.enable_dev_tools(debug=True, dev_tools_hot_reload=True)

    #port = int(os.environ.get('PORT', 8050))
    #app.run(host='0.0.0.0', port=port, debug=False)