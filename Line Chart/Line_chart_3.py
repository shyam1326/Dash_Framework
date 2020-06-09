import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# Read the data
df = pd.read_csv('dataset/2010YumaAZ.csv')
print(df)


data = []
for day in df['DAY'].unique():
    trace = go.Scatter(x = df['LST_TIME'],
                       y = df[df['DAY']==day] ['T_HR_AVG'],
                       mode = 'lines',
                       name = day)
    data.append(trace)



layout = go.Layout(title = 'Daily temperature average')

fig = go.Figure(data, layout)

pyo.plot(fig)


