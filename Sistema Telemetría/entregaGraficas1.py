import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
from pandas.core.base import DataError
import plotly
import random
import plotly.graph_objs as go
from collections import deque
import pandas as pd
import dash_daq as daq
import numpy as np
import plotly.express as px

X = deque(maxlen = 40)
X2 = deque(maxlen = 40)
X3 = deque(maxlen = 20)
X4 = deque(maxlen = 40)
Y = deque(maxlen = 20)
Y2 = deque(maxlen = 20)
Y3 = deque(maxlen = 20)
Y4 = deque(maxlen = 300)

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dcc.Graph(id = 'live-graph', animate = False),
        dcc.Graph(id = 'live-graph2', animate = False),
        dcc.Graph(id = 'live-graph3', animate = False),
        daq.Gauge(  
			color="#DC3912",
			showCurrentValue=True,
			units="RPS",
			id='gauge',
			label="Revoluciones",
			max = 8000,
			min = 0,
			value=0
		),
        daq.Tank(
			value=100,
            color="#FF9900",
			id = 'tank',
			showCurrentValue=True,
			units='litros',
			max = 100,
            min = 0,
			style={'margin': 'auto', 'textAlign': 'center'}
		),
        dcc.Graph(id = 'live-graph4', animate = False , style = {'center' : 'auto'}),
        dcc.Interval(
			id = 'graph-update',
			interval = 100,
			n_intervals = 0
		),
    ]
)

@app.callback(
	Output('live-graph', 'figure'),
	[ Input('graph-update', 'n_intervals') ]
)
def update_graph_scatter(n):
		data = pd.read_csv('datosSimuladorCorregidos.csv')
		X.append(data['xlength'][n])
		Y.append(data['vel'][n])
		
		graph = go.Scatter(
			x=list(X),
			y=list(Y),
			name='Scatter',
			mode= 'lines+markers',
			line=dict(color="#0674D5")
		)

		return {'data': [graph],
				'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)], title = 'Longitud Recorrida (m)'),
                yaxis = dict(range = [min(Y),max(Y)], title = 'Velocidad (Km/h)'),
                title = 'SPEED')}


@app.callback(
	Output('live-graph2', 'figure'),
	[ Input('graph-update', 'n_intervals') ]
)
def update_graph_scatter(n):
		data = pd.read_csv('datosSimuladorCorregidos.csv')
		Y2.append(data['fren'][n])		
		graph = go.Scatter(
			x=list(X),
			y=list(Y2),
			name='Scatter',
			mode= 'lines+markers',
			line=dict(color="#F55643")
		)

		

		return {'data': [graph],
				'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)], title = 'Longitud Recorrida (m)'),
                yaxis = dict(range = [min(Y2),max(Y2)], title = 'Presión de Frenada (atm)'),
                title = 'FRENADA')}  


@app.callback(
	Output('live-graph3', 'figure'),
	[ Input('graph-update', 'n_intervals') ]
)
def update_graph_scatter(n):
		data = pd.read_csv('datosSimuladorCorregidos.csv')
		Y3.append(data['marcha'][n])
		
		graph = go.Scatter(
			x=list(X),
			y=list(Y3),
			name='Scatter',
			mode= 'lines+markers',
			line=dict(color="#03D750")
		)

		return {'data': [graph],
				'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)], title = 'Longitud Recorrida (m)'),
                yaxis = dict(range = [min(Y3),max(Y3)], title = 'Marcha Actual'),
                title = 'MARCHA')}


@app.callback(
	Output('gauge', 'value'),
	[ Input('graph-update', 'n_intervals') ]
)
def update_gauge(n):
	data = pd.read_csv('datosSimuladorCorregidos.csv')
	return data['revact'][n]


@app.callback(
	Output('tank', 'value'),
	[ Input('graph-update', 'n_intervals')]
)
def update_output(n):
	data = pd.read_csv('datosSimuladorCorregidos.csv')
	return int(data['comb'][n])



@app.callback(
	Output('live-graph4', 'figure'),
	[ Input('graph-update', 'n_intervals') ]
)
def update_graph_scatter(n):
		data = pd.read_csv('datosSimuladorCorregidos.csv')
		X4.append(data['xtime'][n])
		Y4.append(data['comb'][n])
		
		graph = go.Scatter(
			x=list(X),
			y=list(Y4),
			name='Scatter',
            fill = 'tozeroy',
            fillcolor = '#FF7F0E',
			mode= 'lines'
		)

		return {'data': [graph],
				'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)], title = 'TIME (s)'),
                yaxis = dict(range = [min(Y4),max(Y4)], title = 'COMB ( % )'),
                title = '% COMB / TIME')}

if __name__ == '__main__':
	app.run_server(debug = True)

