import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('dataset/2010YumaAZ.csv')

data = [go.Heatmap(x = df['DAY'],
                   y = df['LST_TIME'],
                   z = df['T_HR_AVG'],
                   colorscale= 'Jet')]

layout = go.Layout(title= 'Heat Maps')

fig = go.Figure(data, layout)

pyo.plot(fig, filename= 'Heatmaps_1.html')