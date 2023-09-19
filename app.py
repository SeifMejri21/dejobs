import sys

import dash_bootstrap_components as dbc
from dash import dash

from dashboard.app import front_page_layout

app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.BOOTSTRAP],
                suppress_callback_exceptions=True,
                title="DeJobs.",
                update_title="DeJobs. | Loading...",
                assets_folder="assets",
                include_assets_files=True,
                )
app._favicon = "dj2.png"
server = app.server
app.layout = front_page_layout

if __name__ == "__main__":
    app.run_server(debug=sys.platform == "win32")
