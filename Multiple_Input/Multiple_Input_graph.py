import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output

df = pd.read_csv('dataset/mpg.csv')

features = df.columns
# ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name']

app = dash.Dash()

app.layout = html.Div([

    html.Div([
        dcc.Dropdown(id='xaxis',
                     options=[{'label': str(i), 'value': i} for i in features],
                     value='displacement')
    ], style= {'width': '48%', 'display': 'inline-block'}),

    html.Div([
        dcc.Dropdown(id='yaxis',
                     options=[{'label': str(i), 'value': i} for i in features],
                     value='acceleration')
    ], style= {'width': '48%','display': 'inline-block'}),

    dcc.Graph(id='feature_graph'),

], style= {'padding': 10})


@app.callback(Output('feature_graph', 'figure'),
              [Input('xaxis', 'value'),
               Input('yaxis', 'value')])
def update_figure(xaxis_name, yaxis_name):
    return {
        'data': [go.Scatter(
            x=df[xaxis_name],
            y=df[yaxis_name],
            text=df['name'],
            mode='markers',
            marker={'size': 15,
                    'opacity': 0.5,
                    'line': {'width': 0.5, 'color': 'white'}
                    }

                            )
                 ],
        'layout': go.Layout(title='Scatter Plot',
                            xaxis={'title': xaxis_name},
                            yaxis={'title': yaxis_name},
                            hovermode='closest'
                            )
    }


if __name__ == '__main__':
    app.run_server()
