import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd


df = pd.read_csv('dataset/mocksurvey.csv', index_col=0)

data = [go.Bar(x = df[i],
               y = df.index,
               orientation= 'h',
               name = i) for i in df.columns]

layout = go.Layout(title = 'survey Results', barmode = 'stack')

fig = go.Figure(data, layout)

pyo.plot(fig, filename = 'Bar_chart_3.html')