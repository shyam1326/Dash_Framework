import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()

app.layout = html.Div([
    html.Label('Dropdown'),
    dcc.Dropdown(options=[{'label': 'Texas', 'value': 'TX'},
                          {'label': 'New york', 'value': 'NYC'},
                          ], value='NYC', multi= True
                 ),
    html.Br(),

    html.Label('Slider'),
    dcc.Slider(min=-10,
               max=10,
               step=0.5,
               value=0,
               marks={i:i for i in range(-10, 11)}
               ),
    html.Br(),

    html.Label('Radio Button'),
    dcc.RadioItems(options=[{'label': 'Texas', 'value': 'TX'},
                            {'label': 'New york', 'value': 'NYC'},
                            ], value = 'TX'
                  )

])


if __name__ == '__main__':
    app.run_server()
