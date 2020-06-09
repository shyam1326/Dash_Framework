import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('dataset/mpg.csv')

data = [go.Histogram(x = df['mpg'])]  # xbins= dict(start=0, end = 50, size =2)

pyo.plot(data, filename= 'Histogram_1')