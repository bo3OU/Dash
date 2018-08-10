import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
from pyspark.sql import SparkSession
from cassandra.cluster import Cluster
from dash.dependencies import Input, Output
import pandas as pd

app = dash.Dash()

def gen_rows(length):

    return [
        {'a': 'AA', 'b': i} for i in range(length)
    ]


app.layout = html.Div([
    html.Div([
            html.Div([
                html.Button("home", className="btn btn-primary")
            ], className="header-right")
    ], className="header"),

    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.Div([
                            html.Div([
                                html.Div([
                                    html.H4(u'Autorisations suspectees', style={'display': 'inline'}),
                                    html.Button('Fraud', className="btn btn-danger", style={
                                                                                'float': 'right',
                                                                                'margin-right': '15px'
                                                                            }),
                                    html.Button('Valider', className="btn btn-primary", style={
                                                                                'float': 'right',
                                                                                'margin-right': '15px'
                                                                            }),
                                    html.Button('Valider Tous', className="btn btn-primary", style={
                                                                                'float': 'right',
                                                                                'margin-right': '15px'
                                                                            }),
                                ], className="card-header"),

                                html.Div([
                                    dt.DataTable(
                                        rows=gen_rows(50),  # initialise the rows
                                        row_selectable=True,
                                        filterable=False,
                                        sortable=True,
                                        selected_row_indices=[],
                                        id='datatable'
                                    )
                                ], className="card-body", style={'margin-right': '55px'})
                            ], className="card")
                        ], className="col-12")
                    ], className="row"),

                    html.Div([
                        html.Div([
                            html.Div([
                                html.Div([
                                    dcc.Graph(
                                        id='graph1',
                                        figure={
                                            'data': [
                                                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                                                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montreal'},
                                            ],
                                            'layout': {
                                                'title': 'Dash Data Visualization'
                                            }
                                        }
                                    )
                                ], className="card-body")
                            ], className="card")
                        ], className="col-6"),

                        html.Div([
                            html.Div([
                                html.Div([
                                    dcc.Graph(
                                        id='graph2',
                                        figure={
                                            'data': [
                                                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'line', 'name': 'SF'},
                                                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'line', 'name': u'Montreal'},
                                            ],
                                            'layout': {
                                                'title': 'Dash Data Visualization'
                                            }
                                        }
                                    )
                                ], className="card-body")
                            ], className="card")
                        ], className="col-6")
                    ], className="row")
                ], className="animated faceIn")
            ], className="container-fluid")
        ], className="main")
    ], className="app-body")
], className="app header-fixed pace-done pace-done")


if __name__ == '__main__':
    app.run_server(debug=True, port=9050)
