import numpy as np
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# setting the seed
np.random.seed(100)

# creating data
x = np.linspace(0, 1, 100)
y = np.random.randn(100)

# Prepare the data to plot
trace0 = go.Scatter(x = x,
                    y = y+5,
                    mode = 'markers',
                    name = 'scatter') # +5 and -5 we have used to show the differenciate of graph

trace1 = go.Scatter(x = x,
                    y = y,
                    mode = 'lines',
                    name = 'line chart')

trace2 = go.Scatter(x = x,
                    y = y-5,
                    mode = 'lines+markers',
                    name = 'line and marker chart')

data = [trace0, trace1, trace2]

# Layout for the plot
layout = go.Layout(title = 'Multiple chart')

# merge the data and layout
fig = go.Figure(data, layout)

# plot the graph
pyo.plot(fig, filename= 'multiple chart.html')