import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dts

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1('S2M'),
    html.Div('Fraud detection dashboard with Dash, Pyspark and Cassandra.'),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'line', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Montreal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])


app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})


if __name__ == '__main__':
    app.run_server(debug=True)
