import plotly.offline as pyo
import plotly.figure_factory as ff
import numpy as np

x1 = np.random.randn(200)-2
x2 = np.random.randn(200)
x3 = np.random.randn(200)+2
x4 = np.random.randn(200)+4

data_hist = [x1,x2,x3,x4]
group_labels = ['x1','x2','x3','x4']

fig = ff.create_distplot(data_hist, group_labels) # bin_size = [0.2,0.3,0.4,]

pyo.plot(fig, filename= 'Dist_plot_1.html')