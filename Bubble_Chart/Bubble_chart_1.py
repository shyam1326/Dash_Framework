import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('dataset/mpg.csv')

data = [go.Scatter(x = df['horsepower'],
                   y = df['mpg'],
                   text = df['name'],
                   mode = 'markers',
                   marker= dict(size = df['weight']/100,  # if the size is small multiply by 2 or 4 ,if the size is high divide by 100 or any number
                                color = df['cylinders'],
                                showscale = True)
                   )]

layout = go.Layout(title = 'Bubble_chart',
                   xaxis= dict(title = 'Horsepower'),
                   yaxis= dict(title = 'MPG'))


fig = go.Figure(data, layout)

pyo.plot(fig, filename= 'Bubble_chart_1.html')