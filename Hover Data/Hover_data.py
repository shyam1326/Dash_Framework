import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import pandas as pd
import json
import base64

def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, 'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())

df = pd.read_csv('dataset/wheels.csv')

app = dash.Dash()

app.layout = html.Div([
    html.Div(dcc.Graph(id = 'wheels-plot',
                       figure= {'data': [go.Scatter(
                           x = df['color'],
                           y = df['wheels'],
                           dy= 1,
                           mode= 'markers',
                           marker = {'size':15}
                       )],
                           'layout': go.Layout(title='Test',
                                               hovermode='closest')
                            },
                       ), style= {'width': '30%', 'float': 'left'}
            ),
html.Div(html.Img(id = 'hover-data', src = 'children', height= 600)                                                     #html.Div(html.Pre(id = 'hover-data')
             )
])


@app.callback(Output('hover-data', 'src'),                                                                              # {
          [Input('wheels-plot', 'hoverData')])                                                                          #   "points": [
def callback_image(hover):                                                    #return json.dumps(hover, indent=2)       #   {
    wheel = hover['points'][0]['y']                                                                                     #       "curveNumber": 0,
    color = hover['points'][0]['x']                                                                                     #       "pointNumber": 6,
    path = 'dataset/images/'                                                                                             #       "pointIndex": 6,
    return encode_image(path+df[(df['wheels']==wheel) & (df['color']== color)]['image'].values[0])                      #       "x": "red",
                                                                                                                        #       "y": 3
                                                                                                                        #     }
                                                                                                                        #   ]
                                                                                                                        # }
if __name__ == '__main__':
    app.run_server(port = 8053)
