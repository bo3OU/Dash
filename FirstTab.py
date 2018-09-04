import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dte


from DashFunctions import *

df = get_Data()
dfss = getPercentCountries()

Tab1 =   html.Div([
                html.Div([
                    html.Div([
                        html.Div([
                            html.Div([
                                html.Div([
                                    html.Div([
                                        html.Div([
                                            html.Div([
                                                html.H4(u'Autorisations suspectees', style={'display': 'inline'}),
                                                html.Button('Fraud', id="BTN_Fraud", className="btn btn-danger", style={
                                                                                            'float': 'right',
                                                                                            'margin-right': '15px'
                                                                                        }),
                                                html.Button('Valider', id="BTN_Validate", className="btn btn-primary", style={
                                                                                            'float': 'right',
                                                                                            'margin-right': '15px'
                                                                                        }),
                                                html.Button('Valider Tous', id="BTN_Validate_all",className="btn btn-primary", style={
                                                                                            'float': 'right',
                                                                                            'margin-right': '15px'
                                                                                        }),
                                            ], className="card-header"),

                                            html.Div([
                                                dte.DataTable(
                                                    rows=df.to_dict('records'),
                                                    row_selectable=True,
                                                    columns =  df.columns,
                                                    filterable=True,
                                                    sortable=True,
                                                    editable=False,
                                                    selected_row_indices=[],
                                                    id='fraudtable'
                                                )
                                            ], className="card-body", style={'margin-right': '55px'})
                                        ], className="card")
                                    ], className="col-12")
                                ], className="row"),

                                html.Div([
                                    html.Div([
                                        dcc.DatePickerSingle(
                                            id='date-picker',
                                            min_date_allowed=dt(2015, 1, 1),
                                            max_date_allowed=dt.now(),
                                            initial_visible_month=dt(2017, 8, 5),
                                            date=dt(2017, 8, 25)
                                        ),
                                        html.Button('Change', id="DateChange", className="btn btn-primary",style={'margin-left':'30px'}),
                                    ], className="col-12"),
                                ], className="row"),
                                html.Div([
                                    html.Div([
                                        html.Div([
                                            html.Div([

                                                dcc.Graph(
                                                    id='graph1',
                                                    figure={
                                                        'data': [
                                                            {
                                                                'type': 'violin',
                #                                                     'x': df['classe'],
                                                                'y': get_violin()['aut_bill_amou_f006'],
                                                                'text': get_violin()['aut_code'],
                                                                'jitter': 1
                                                            }
                                                        ],
                                                        'layout': {
                                                            'title': "violin plot of models prediction by class"
                                                        }
                                                    }
                                                ),

                                                dcc.Slider(
                                                    id='ModelSlider',
                                                    min=0,
                                                    max=11,
                                                    step=None,
                                                    marks={
                                                        1: 'Modele 1', 2: 'Modele 2', 3: 'Modele 3', 4: 'Modele 4', 5: 'Modele 5', 6: 'Modele 6', 7: 'Modele 7', 8: 'Modele 8', 9: 'Modele 9', 10: 'Modele 10'
                                                    },
                                                    value=1
                                                )
                                            ], className="card-body", id="graph1-holder")
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
                                ], className="row"),

                                html.Div([
                                    html.Div([
                                        html.Div([
                                            html.Div([
                                                dcc.Graph(
                                                    id='graph3',
                                                    figure={
                                                        'data': [
                                                            {'values': getPercentCountries()['percent'], 'type': 'pie', 'name': 'General behavior'},
                                                        ],
                                                        'layout': {
                                                            'title': 'Dash Data Visualization'
                                                        }
                                                    }
                                                )
                                            ], className="card-body")
                                        ], className="card")
                                    ], className="col-5"),

                                    html.Div([
                                        html.Div([
                                            html.Div([

                                                
                                            ], className="card-body")
                                        ], className="card")
                                    ], className="col-4"),
                                    html.Div([
                                        html.Div([
                                            html.Div([
                                                #last auts table
                                            ], className="card-body",id = 'tableLastAuts')
                                        ], className="card")
                                    ], className="col-3"),                        
                                ], className="row"),

                                html.Div([
                                    html.Div(id='output'),
                                    html.Div(id='output1'),
                                    html.Div(id='output2'), 
                                    html.Div(id='global_var'),
                                ]),

                            ], className="animated faceIn")
                        ], className="container-fluid")
                    ], className="main")
                ], className="app-body",style={'margin-top':'0px'})
            ], className="app header-fixed pace-done pace-done")

