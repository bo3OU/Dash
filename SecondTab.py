import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dte

from DashFunctions import *

dfss = getPercentCountries()
df_percentages = getPercentageChange()

dataMap = [ dict(
        type = 'choropleth',
        locations = dfss['alpha-3'],
        z = dfss['percent'],
        text = dfss['name'],
        colorscale = [[0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
            [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"]],
        autocolorscale = False,
        reversescale = True,
        marker = dict(
            line = dict (
                color = 'rgb(180,180,180)',
                width = 0.5
            ) ),
        colorbar = dict(
            autotick = False,
            tickprefix = '+',
            title = 'Nombre de Frauds'),
      ) ]

layoutMap = dict(
    height = 800,
    title = 'Fraud par pays',
    geo = dict(
        showframe = False,
        showcoastlines = False,
        projection = dict(
            type = 'Mercator'
        )
    )
)

fig = dict( data=dataMap, layout=layoutMap,style={ 'height': 800 },
)    

Tab2 =  html.Div([
                    html.Div([
                        html.Div([
                            html.Div([
                                html.Div([
                                    
                                    html.Div([
                                        html.Div([
                                            dcc.Graph(id='graphMap', figure=fig)
                                        ], className="col-12"),    
                                    ], className="row"),
                                    
                                    html.Div([
                                        html.Div([
                                            dcc.Graph(
                                                id='Graph1-2',
                                                figure={
                                                'data': [
                                                    {
                                                        'y':getY(df_percentages.query('classe == 1')),
                                                        'x':getX(df_percentages.query('classe == 1')),
                                                        'type':'bar',
                                                        'name': u"nombre d'auts fraudees * 100"
                                                    },
                                                     {
                                                         'y':getY(df_percentages.query('classe == 0')),
                                                         'x':getX(df_percentages.query('classe == 0')),
                                                         'type':'bar',
                                                         'name': "nombre d'auts non fraudees"
                                                     },
                                                ],
                                                'layout': {
                                                    'title': 'Nombre d\'autorisations valides/fraudes par trimestre'
                                                }
                                            }
                                                )
                                        ], className="col-6"),    
                                        html.Div([
                                                html.Div([
                                                    html.Div([

                                                    ], className="card-body")
                                                ], className="card")
                                        ], className="col-6"),    
                                    ], className="row"),
                                    
                                ], className="animated faceIn")
                            ], className="container-fluid")
                        ], className="main")
                    ], className="app-body",style={'margin-top':'0px'})
                ], className="app header-fixed pace-done pace-done")