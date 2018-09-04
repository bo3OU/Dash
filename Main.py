#disable "useless" warnings
import warnings
warnings.filterwarnings('ignore')

#imports packages 
import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dte
from cassandra.cluster import Cluster
from dash.dependencies import State, Event, Input, Output
import pandas as pd
from datetime import datetime as dt
import base64
import timeago

#creates the dash app
# VALID_USERNAME_PASSWORD_PAIRS = [['hello', 'world']]
app = dash.Dash() # app = dash.Dash('auth')
app.config['suppress_callback_exceptions']=True
# auth = dash_auth.BasicAuth(app, VALID_USERNAME_PASSWORD_PAIRS)

image_filename = 's2m.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

#connects directly to the cassandra database
#this is here because spark can't update the database, thus, changing database's class is only possible through cassandra's python driver
cluster = Cluster(['127.0.0.1'])
session = cluster.connect('projet')

from DashFunctions import *


from FirstTab import Tab1
from SecondTab import Tab2

#wrapper function that takes 4 kinds of parameters ( States, Input, Output, Event) => see Dash docs
@app.callback(
    Output('output', 'children'),
    [
        Input('BTN_Fraud', 'n_clicks')
    ],
    state=[
        State('fraudtable', 'rows'),
        State('fraudtable', 'selected_row_indices')
    ])
def on_click(n_clicks,rows,selected_row_indices):
    if n_clicks > 0:
        selected_rows=[rows[i] for i in selected_row_indices]
        return 'update autorisations SET VALIDE = TRUE, CLASSE = 1 where aut_code in ({}) '.format(','.join(str(rows[e]['Aut_Code']) for e in selected_row_indices))
        
        
@app.callback(
    Output('output1', 'children'),
    [
        Input('DateChange', 'n_clicks'),
        Input('date-picker', 'date')
    ],
    )
def on_data_change(n_clicks, date):
    if n_clicks > 0:
        date = dt.strptime(date, '%Y-%m-%d')
        date_string = date.strftime('%B %d, %Y')
        return 'please : {}'.format(date_string)
        
@app.callback(
    Output('tableLastAuts', 'children'),
    [
        Input('graph1', 'clickData')
    ],)
def selected_point_table(clickData):
    if clickData is not None: 
        return  generate_table(getLastAuts(clickData['points'][0]['text']))

# @app.callback(
#     Output('graph2', 'figure'),
#     [ Input('graph1', 'clickData'), Input('graph1', 'hoverData'),]
# )
# def selected_point_graph2(clickData,hoverData):
#     print(clickData)
#     dff = getBehavior(clickData['points'][0]['text'])
#     return  {
#                     'data': [
#                         {'x': getX(dff), 'y': getY(dff), 'type': 'line', 'name': 'Mouthly behavior'},
#                       # {'x': ['lundi', 'mardi', 'mercredi','jeudi','venredi','samedi','dimanche'], 'y': [2, 4, 5,5,6,7,9], 'type': 'line', 'name': u'Week behavior'},
#                     ],
#                     'layout': {
#                         'title': 'Moyenne montant par mois'
#                     }
#                 }

# @app.callback(
#     Output('output', 'children'), 
#     [Input('input-2', 'value')])
# def update_output(input1, input2):
#     return u'Input 1 is "{}" and Input 2 is "{}"'.format(input1, input2)

app.layout = html.Div([
                            html.Div([
                                                            html.Div([
                                                                html.Img(src='data:image/png;base64,{}'.format(encoded_image),style={'height':'80px'}),
                                                            ], className="header"),
                                html.Div([
                                    html.Div([

                                                
                                                                        dcc.Tabs(id="tabs", children=[
                                                                            dcc.Tab(label='Generale', children=[
                                                                                html.Div([
                                                                                    html.Div([
                                                                                        Tab2
                                                                                    ], className="animated faceIn")
                                                                                ], className="container-fluid")
                                                                            ]),
                                                                            dcc.Tab(label='Fraude', children=[
                                                                                html.Div([
                                                                                    html.Div([
                                                                                        Tab1
                                                                                    ], className="animated faceIn")
                                                                                ], className="container-fluid")
                                                                            ]),
                                                                        ],
                                                                            content_style={
#                                                                             'borderLeft': '1px solid #d6d6d6',
#                                                                             'borderRight': '1px solid #d6d6d6',
#                                                                             'borderBottom': '1px solid #d6d6d6',
                                                                            'padding': '44px'
                                                                        }
                                                                        )

                ], className="main")
            ], className="app-body",style={'margin-top':'0px'})
        ], className="app header-fixed pace-done pace-done")
])



#starts the server :), flusk magic
if __name__ == '__main__':
    app.run_server(debug=False, port=9994)
