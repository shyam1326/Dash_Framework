import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('dataset/abalone.csv')

data = [go.Histogram(x = df['length'],
                     xbins= dict(start = 0, end = max(df['length']),
                     size = 0.02))]

pyo.plot(data, filename= 'Histogram_2')