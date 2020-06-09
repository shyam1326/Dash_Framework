import numpy as np
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go

x = np.random.randint(1,101,100)
y = np.random.randint(1,101,100)

app = dash.Dash()

app.layout = html.Div([
                        dcc.Graph(id = 'scatter',
                                  figure = {'data': [go.Scatter(x = x,
                                                                y = y,
                                                                mode = 'markers',
                                                                marker = {'size': 12,
                                                                          'color' : 'green',
                                                                          'symbol' : 'pentagon',
                                                                          'line' : {'width': 2}
                                                                          }
                                                                )],

                                            'layout' : go.Layout(title = 'scatterplot',
                                                                xaxis = {'title': 'some Xa  xis'})}
                                  ),
                        dcc.Graph(id = 'scatter2',
                                  figure = {'data': [go.Scatter(x = x,
                                                                y = y,
                                                                mode = 'markers',
                                                                marker = {'size': 12,
                                                                          'color' : 'red',
                                                                          'symbol' : 'star',
                                                                          'line' : {'width': 2}
                                                                          }
                                                                )],

                                            'layout' : go.Layout(title = 'scatterplot_2',
                                                                xaxis = {'title': 'some Xaxis'})}
                                  )
                                  ])

if __name__ == '__main__':
    app.run_server()