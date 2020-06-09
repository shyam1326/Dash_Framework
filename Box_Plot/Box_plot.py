import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import numpy as np

df = pd.read_csv('dataset/abalone.csv')

a = np.random.choice(df['rings'],100,replace= False) # randomly pick samples from the population
b = np.random.choice(df['rings'],100,replace= False)

data = [go.Box(y = a, name = 'A'),
        go.Box(y = b, name = 'B')]

layout = go.Layout(title = 'Box plot of samples')

fig = go.Figure(data, layout)

pyo.plot(fig, filename= 'Box_plot.html')
