import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children= [
    html.H1('Hello Dash!'),
    html.Div('Web dashboard with python'),
    dcc.Graph(id = 'ex',
              figure= {'data':[
                  {'x': [1,2,3], 'y': [4,1,2], 'type': 'bar', 'name': 'SF'},
                  {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'NYC'}
              ],
                        'layout':{'title': 'BAR plot'}
              })
])

if __name__ == '__main__':
    app.run_server()