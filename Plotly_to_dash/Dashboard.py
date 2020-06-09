import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('dataset/OldFaithful.csv')

app = dash.Dash()

app.layout = html.Div([
                    dcc.Graph(id = 'old faith',
                              figure= {
                                  'data': [go.Scatter(x = df['X'],
                                                      y = df['Y'],
                                                      mode= 'markers',
                                                      # marker={'size': 12,
                                                      #         'color': 'yellow',
                                                      #         'symbol': 'hexagon',
                                                      #         'line': {'width': 2}}
                                                      )
                                           ],
                                  'layout': go.Layout(title = 'Dashboard',
                                                      xaxis={'title': 'Duration'},
                                                      yaxis={'title': 'Interval'}
                                                      )
                                  }
                              )
                     ])

if __name__ == '__main__':
    app.run_server()