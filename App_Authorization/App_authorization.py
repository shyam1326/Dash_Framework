import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_auth


USERNAME_PASSWORD_PAIRS = {'shyam': 'prasath'}

app = dash.Dash()

auth = dash_auth.BasicAuth(app, USERNAME_PASSWORD_PAIRS)

app.layout = html.Div([
    html.H1('RangeSlider Product', style= {'textAlign': 'center'}),
    dcc.RangeSlider(id = 'Range',
                    min = -10,
                    max = 10,
                    marks= {i:str(i) for i in range(-10,11)},
                    value= [-2,2]
                    ),
    html.H1(id = 'product'),
])

@app.callback(Output('product', 'children'),
              [Input('Range', 'value')])
def update_range(value):
    return value[0]*value[1]

if __name__ == '__main__':
    app.run_server()