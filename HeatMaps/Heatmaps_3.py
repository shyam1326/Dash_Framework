import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
from plotly.subplots import make_subplots

df = pd.read_csv('dataset/flights.csv')

data = [go.Heatmap(x = df['year'],
                   y = df['month'],
                   z = df['passengers'],
                   colorscale= 'Jet')]

layout = go.Layout(title= 'Flights',
                   xaxis= dict(title = 'Year'),
                   yaxis= dict(title = 'Month'))

fig = go.Figure(data, layout)


pyo.plot(fig,filename= 'Heatmaps_3.html')