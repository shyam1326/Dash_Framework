import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('dataset/2018WinterOlympics.csv')

data = []
color = {'Gold': 'gold', 'Silver': 'silver', 'Bronze': '#CD7F32'}

for i in df.columns.difference(['Rank', 'NOC', 'Total']):
    trace = go.Bar(x = df['NOC'],
                   y = df[i],
                   name = i,
                   marker = {'color': color[i]})

    data.append(trace)

layout = go.Layout(title = 'Medals') #barmode = 'stack'

fig = go.Figure(data, layout)

pyo.plot(fig, filename= 'Bar_chart_1.html')