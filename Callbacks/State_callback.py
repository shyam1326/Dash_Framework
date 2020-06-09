import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id = 'number_in',
              value= '',
              style= {'fontSize': 24}),
    html.Button(id = 'submit_button',
                n_clicks=0,
                children= 'Submit Here',
                style= {'fontSize': 24}),
    html.H1(id = 'number_out')
])

@app.callback(Output('number_out', 'children'),
              [Input('submit_button', 'n_clicks')],
              [State('number_in', 'value')])
def update_number(n_click, number):
    return '{} was typed in, and the button was clicked {} times'.format(number,n_click)


if __name__ == '__main__':
    app.run_server()