import plotly.offline as pyo
import plotly.figure_factory as ff
import pandas as pd
import numpy as np

df = pd.read_csv('dataset/iris.csv')

trace0 = df[df['class']=='Iris-setosa']['petal_length']
trace1 = df[df['class']=='Iris-versicolor']['petal_length']
trace2 = df[df['class']=='Iris-virginica']['petal_length']

data_hist = [trace0, trace1, trace2]
group_labels = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

fig = ff.create_distplot(data_hist, group_labels)

pyo.plot(fig, filename= 'Dist_plot_2.html')