import dash
import dash_html_components as html
import  dash_core_components as dcc
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
    html.H1('Range slider product', style= {'textAlign': 'center'}),
    dcc.RangeSlider(id = 'range_slider',
                    min = -10,
                    max = 10,
                    marks= {i:str(i) for i in range(-10,11)},
                    value = [-1,2]
                    ),
    html.H1(id = 'product')
])

@app.callback(Output('product', 'children'),
              [Input('range_slider', 'value')])
def update_product(value_list):
    return value_list[0]* value_list[1]

if __name__ == '__main__':
    app.run_server()