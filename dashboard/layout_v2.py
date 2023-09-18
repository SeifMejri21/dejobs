import dash
import dash_ag_grid as dag
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import pandas as pd
from dash import Output, State, dcc, no_update, html
from dash_iconify import DashIconify

app = dash.Dash(
    __name__,
    external_stylesheets=[
        "https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;900&display=swap",
    ],
    title="DeJobs.",
    update_title="DeJobs. | Loading...",
    assets_folder="assets",
    include_assets_files=True,
)
server = app.server


def job_component(title="", firm_image="", firm_name="", location="", job_type=""):
    component = dash.html.Div(children=[
        html.Div([dmc.Image(
            src="https://assets-global.website-files.com/6364e65656ab107e465325d2/637aeee74d38a6e43415e6b3_vq8xBrkijMAgDZQi0-rEeQIceQhL2PwuO9vYWSU5OQ0.png",
            width=50, title='Opensea'),
            dmc.Image(
                src="https://i.postimg.cc/90fzNFxT/logo.png",
                alt="DeJobs. Logo",
                width=150,
                m=20,
                # caption="The best web3 job board",
            )],
        ),  # firm image
        html.Div(children=[
            # html.H4(title="Senior Data Engineer, Infrastructure",),
            # html.H4(title="at Opensea",),
            html.H4("Senior Data Engineer, Infrastructure",
                    style={'font-size': '26px', 'font-weight': 'bold', "color": "blue"}),
            html.H4("at Opensea", style={'font-size': '16px', 'font-weight': 'bold', "color": "yellow"})],
        ),  # job title and firm name
        html.Div(dmc.Center(
            dmc.Button(
                dmc.Anchor("Apply here", href="https://jobs.ashbyhq.com/OpenSea/66dd92c8-5075-45fb-81f9-8e43a053211a",
                           target="_blank", style={"textDecoration": "none", "color": "white", }, ), fullWidth=False,
                rightIcon=html.A(DashIconify(icon="material-symbols:open-in-new"),
                                 href="https://jobs.ashbyhq.com/OpenSea/66dd92c8-5075-45fb-81f9-8e43a053211a",
                                 target="_blank"),
                # color="#FE1356",
                color="red",
                size="md",
            ),
        ), ),  # apply button
    ])
    return component


def job_component_v2(title="", firm_image="", firm_name="", location="", job_type=""):
    component = dbc.Row([
        dbc.Col([dmc.Image(
            src="https://assets-global.website-files.com/6364e65656ab107e465325d2/637aeee74d38a6e43415e6b3_vq8xBrkijMAgDZQi0-rEeQIceQhL2PwuO9vYWSU5OQ0.png",
            alt="DeJobs. Logo", width=40, m=20, ), ], width=3,
            style={"margin-bottom": "30px"}),  # firm image),
        dbc.Col([
            html.H4("Senior Data Engineer, Infrastructure",
                    style={'font-size': '20px', 'font-weight': 'bold', "color": "blue"}),
            html.H4("at Opensea", style={'font-size': '16px', 'font-weight': 'bold', "color": "green"})]
            , width=3, style={"margin-bottom": "30px"}),
        dbc.Col(dmc.Button(
            dmc.Anchor("Apply here", href="https://jobs.ashbyhq.com/OpenSea/66dd92c8-5075-45fb-81f9-8e43a053211a",
                       target="_blank", style={"textDecoration": "none", "color": "white", }, ), fullWidth=False,
            rightIcon=html.A(DashIconify(icon="material-symbols:open-in-new"),
                             href="https://jobs.ashbyhq.com/OpenSea/66dd92c8-5075-45fb-81f9-8e43a053211a",
                             target="_blank"),
            # color="#FE1356",
            color="red",
            size="md",
        ), width=3, style={"margin-bottom": "30px"},
        ),
    ])
    return component


def job_card():
    card_sales = dbc.Card(
        dbc.CardBody(
            [
                html.H1([html.I(className="bi bi-currency-dollar me-2"), "Sales"], className="text-nowrap"),
                html.H3("$106.7M"),
                html.Div(
                    [
                        html.I("5.8%", className="bi bi-caret-up-fill text-success"),
                        " vs LY",
                    ]
                ),
            ], className="border-start border-success border-5"
        ),
        className="text-center m-4"
    )
    return card_sales


def job_card2():
    card = dbc.Card(
        [
            dbc.Row(
                [
                    dbc.Col(
                        dbc.CardImg(
                            src="https://assets-global.website-files.com/6364e65656ab107e465325d2/637aeee74d38a6e43415e6b3_vq8xBrkijMAgDZQi0-rEeQIceQhL2PwuO9vYWSU5OQ0.png",
                            className="img-fluid rounded-start",
                            style={"width": "40px", }
                        ),
                        className="col-md-4", align='center'
                    ),
                    dbc.Col(
                        dbc.CardBody(
                            [
                                html.H4("Senior Data Engineer, Infrastructure", className="card-title"),
                                html.P("at Opensea", className="card-text", ),
                                html.Small("San Francisco, Silicon Valley, New York or Remote US",
                                           className="card-text text-muted", ),
                            ]
                        ),
                        className="col-md-12", style={"color": "light"}, align='center',
                    ),
                    dbc.Col(
                        dmc.Button(
                            dmc.Anchor("Apply here",
                                       href="https://jobs.ashbyhq.com/OpenSea/66dd92c8-5075-45fb-81f9-8e43a053211a",
                                       target="_blank", style={"textDecoration": "none", "color": "white", }, ),
                            fullWidth=False,
                            rightIcon=html.A(DashIconify(icon="material-symbols:open-in-new"),
                                             href="https://jobs.ashbyhq.com/OpenSea/66dd92c8-5075-45fb-81f9-8e43a053211a",
                                             target="_blank"),
                            # color="#FE1356",
                            color="red",
                            size="md",
                        ),
                        className="col-md-4", style={"color": "light"}, align='end',
                    ),

                ],
                className="g-0 d-flex align-items-center",
            )
        ],
        className="mb-3",
        style={"maxWidth": "1000px"}, color='yellow'
    )
    return card


body = dmc.Stack(
    [
        dmc.Stepper(
            id="stepper",
            contentPadding=30,
            active=0,
            size="md",
            breakpoint="sm",
            children=[
                dmc.StepperStep(
                    children=[
                        dmc.Stack(
                            [
                                # dmc.Stack(
                                #     [
                                #         dmc.Blockquote(
                                #             """Welcome to DeJobs! Your best and most complete job board for WEB3 jobs seekers 🥳""",
                                #             # icon=DashIconify(
                                #             #     icon="material-symbols:work"
                                #             # ),
                                #         ),
                                #
                                #     ],
                                # ),

                                # job_card(),
                                # job_card(),
                                job_card2(),
                                job_card2(),
                                # job_component_v2(),
                                # job_component_v2(),
                            ]
                        )
                    ],
                ),
            ],
        ),
        dmc.Group(
            [
                dmc.Button(
                    "Back",
                    id="stepper-back",
                    display="none",
                    size="md",
                    variant="outline",
                    radius="xl",
                    leftIcon=DashIconify(icon="ic:round-arrow-back"),
                ),
                dmc.Button(
                    "Next",
                    id="stepper-next",
                    size="md",
                    radius="xl",
                    rightIcon=DashIconify(
                        icon="ic:round-arrow-forward", id="icon-next"
                    ),
                ),
            ],
            position="center",
            mb=20,
        ),
    ]
)

header = dmc.Center(
    html.A(
        dmc.Image(
            src="https://i.postimg.cc/90fzNFxT/logo.png",
            alt="DeJobs. Logo",
            width=150,
            m=20,
            # caption="The best web3 job board",
        ),
        href="https://github.com/SeifMejri21/dejobs",
        target="_blank",
        style={"textDecoration": "none"},
    )
)

socials = dmc.Affix(
    dmc.Stack(
        [
            dmc.ActionIcon(
                html.A(
                    DashIconify(icon="mdi:github", width=25),
                    href="https://github.com/SeifMejri21/dejobs",
                    target="_blank",
                    style={"color": "black"},
                ),
            ),
            dmc.ActionIcon(
                html.A(
                    DashIconify(icon="mdi:linkedin", width=25),
                    href="https://www.linkedin.com/in/seif-eddine-mejri-5436b5195/",
                    target="_blank",
                    style={"color": "#0B65C2"},
                ),
            ),
        ],
        spacing="sm",
    ),
    position={"top": 10, "left": 10},
)


def show_graph_card(graph, code):
    return dmc.Card(
        dmc.Stack(
            [
                html.Div(graph),
                dmc.Accordion(
                    variant="separated",
                    chevronPosition="right",
                    radius="md",
                    children=[
                        dmc.AccordionItem(
                            [
                                dmc.AccordionControl(
                                    "Show code",
                                    icon=DashIconify(icon="solar:code-bold"),
                                ),
                                dmc.AccordionPanel(
                                    dmc.Prism(
                                        code,
                                        language="python",
                                        id="output-code",
                                        withLineNumbers=True,
                                    ),
                                ),
                            ],
                            value="customization",
                        )
                    ],
                ),
            ]
        )
    )


jobs = html.Div([
    html.H4('Jobzzzzzzzzzzzzzzzzzzzzz'),
    job_card2(),
    job_card2(),
    job_card2(),
])

page = [
    dcc.Store(id="dataset-store", storage_type="local"),
    dmc.Container(
        [
            dmc.Stack(
                [
                    header,
                    body, socials,

                ]
            ),
        ]
    ),
]

app.layout = dmc.MantineProvider(
    id="mantine-provider",
    theme={
        "fontFamily": "'Inter', sans-serif",
        "colorScheme": "light",
        "primaryColor": "dark",
        "defaultRadius": "md",
        "white": "#fff",
        "black": "#404040",
    },
    withGlobalStyles=True,
    withNormalizeCSS=True,
    children=page,
    inherit=True,
)


def load_data(dataset):
    if dataset is not None:
        df = pd.read_json(dataset, orient="split")
        table_preview = dag.AgGrid(
            id="data-preview",
            rowData=df.to_dict("records"),
            style={"height": "275px"},
            columnDefs=[{"field": i} for i in df.columns],
        )
        return (
            table_preview,
            table_preview,
            {
                "borderWidth": "1px",
                "borderStyle": "dashed",
                "borderRadius": "5px",
                "textAlign": "center",
                "padding": "7px",
                "backgroundColor": "#fafafa",
            },
            dmc.Group(
                [
                    html.Div(
                        [
                            "Drag and Drop or",
                            dmc.Button(
                                "Replace file",
                                ml=10,
                                leftIcon=DashIconify(icon="mdi:file-replace"),
                            ),
                        ]
                    )
                ],
                position="center",
                align="center",
                spacing="xs",
            ),
        )
    return no_update


@app.callback(
    # Output("input-text-retry", "value"),
    Output("output-card", "children"),
    # Input("stepper-next", "n_clicks"),
    State("stepper", "active"),
    State("dataset-store", "data"),
    State("input-text", "value"),
    # State("input-text-retry", "value"),
    prevent_initial_call=True,
)
def update_graph(n_clicks, active, df, prompt, prompt_retry):
    return 1, 2


if __name__ == "__main__":
    app.run_server(debug=True
                   )
