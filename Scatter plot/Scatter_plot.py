import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

# setting the seed
np.random.seed(123)

# creating data
x = np.random.randint(1,101,100)   # random integer
y = np.random.randint(1,101,100)

# Prepare the data to plot
data = [go.Scatter(x = x,
                   y = y,
                   mode = 'markers',
                   marker = dict(
                   size = 12,
                   color = 'green', #rgb(51,204,153)
                   symbol = 'pentagon',
                   line = {'width': 2})
                   )]

# Layout for the plot
layout = go.Layout(title = 'Scatter plot',
                   xaxis = {'title': 'axis_x'},
                   yaxis = {'title': 'axis_y'}
                   )

# merge the data  and layout
fig = go.Figure(data = data, layout = layout)

# plot the graph
pyo.plot(fig, filename= 'scatter_plot.html')

