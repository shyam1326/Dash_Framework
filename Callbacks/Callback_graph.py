import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output


df = pd.read_csv('dataset/gapminderDataFiveYear.csv')

app = dash.Dash()

year_options = []
for year in df['year'].unique():
    year_options.append({'label': str(year),'value': year})


app.layout = html.Div([
    dcc.Dropdown(id = 'year-picker',
                 options = year_options,
                 value= df['year'].min()),
    dcc.Graph(id = 'graph'),
                    ])

@app.callback(Output('graph', 'figure'),
              [Input('year-picker', 'value')])
def update_figure(select_year):
    filtered_df = df[df['year']==select_year]

    traces = []
    for continent_name in df['continent'].unique():
        df_continent = filtered_df[filtered_df['continent']== continent_name]
        traces.append(go.Scatter(
            x = df_continent['gdpPercap'],
            y = df_continent['lifeExp'],
            mode = 'markers',
            marker= {'size': 15},
            opacity = 0.7,
            name = continent_name
        ))
    return {'data': traces,
            'layout': go.Layout(title = 'Plot',
                                xaxis={'title': 'GDP per capita', 'type': 'log'},
                                yaxis = {'title': 'Life Expectancy'}
                                )
            }

if __name__ == '__main__':
    app.run_server(debug= True)
