import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('dataset/mpg.csv')

data = [go.Scatter(x = df['displacement'],
                   y = df['acceleration'],
                   text = df['name'],
                   mode= 'markers',
                   marker= dict(size = df['weight']/100,
                                color = df['origin'],
                                showscale = True)
                   )]

layout = go.Layout(title= 'Bubble_chart',
                   hovermode= 'closest',
                   xaxis= dict(title = 'Displacement'),
                   yaxis= dict(title = 'Acceleration'),
                   )

fig = go.Figure(data, layout)

pyo.plot(fig, filename= 'Bubble_chart_2.html')