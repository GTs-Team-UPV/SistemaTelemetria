import dash
import math
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
import predictor

X = deque(maxlen=40)
X2 = deque(maxlen=40)
X3 = deque(maxlen=20)
X4 = deque(maxlen=40)
Y = deque(maxlen=20)
Y2 = deque(maxlen=20)
Y3 = deque(maxlen=20)
Y4 = deque(maxlen=40)

# Declaramos el contenedor de la interfaz
app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.Div(
            [
                # Añadimos la grafica de velocidad
                dcc.Graph(id="vel-graph", animate=False),
            ],
            style={
                "width": "100%",
                "align-items": "center",
                "justify-content": "center",
            },
        ),
        html.Div(
            [
                # Añadimos gráfica de presión de frenada
                dcc.Graph(id="fren-graph", animate=False),
            ],
            style={
                "width": "100%",
                "align-items": "center",
                "justify-content": "center",
            },
        ),
        html.Div(
            [
                # Añadimos gráfica de la marcha actual
                dcc.Graph(id="marcha-graph", animate=False),
            ],
            style={
                "width": "100%",
                "align-items": "center",
                "justify-content": "center",
            },
        ),
        html.Div(
            [
                # Visor de revoluciones por segundo
                daq.Gauge(
                    color="#DC3912",
                    showCurrentValue=True,
                    units="RPS",
                    id="gauge",
                    label="Revoluciones",
                    max=8000,
                    min=0,
                    value=0,
                ),
                # Visor del tanque de gasolina, en porcentage
                daq.Tank(
                    value=100,
                    color="#FF9900",
                    id="tank",
                    showCurrentValue=True,
                    units="litros",
                    max=100,
                    min=0,
                    style={"margin": "auto", "textAlign": "center"},
                ),
            ],
            style={"width": "100%", "display": "flex", "align-items": "center"},
        ),
        html.Div(
            [
                # Gráfica de combustible en tiempo
                dcc.Graph(id="comb-graph", animate=False, style={"center": "auto"}),
                # Actualizamos funciones cada 'interval' empezando desde 'n_interval'
                dcc.Interval(id="graph-update", interval=200, n_intervals=0),
            ],
            style={
                "width": "100%",
                "align-items": "center",
                "justify-content": "center",
            },
        ),
    ]
)
# Declaramos callbacks para el muestreo desde el csv asignado


@app.callback(Output("vel-graph", "figure"), [Input("graph-update", "n_intervals")])
def update_graph_scatter(n):
    data = pd.read_csv("datosSimuladorCorregidos.csv")
    X.append(data["xlength"][n])
    Y.append(data["vel"][n])
    graph = go.Scatter(
        x=list(X),
        y=list(Y),
        name="Scatter",
        mode="lines+markers",
        line=dict(color="#0674D5"),
    )
    return {
        "data": [graph],
        "layout": go.Layout(
            xaxis=dict(
                range=[min(X), max(X)],
                title="Longitud Recorrida (m)",
                showline=True,
                linewidth=2,
                linecolor="black",
                mirror=True,
                gridwidth=1,
                gridcolor="LightPink",
            ),
            yaxis=dict(
                range=[0, 250],
                title="Velocidad (Km/h)",
                showline=True,
                linewidth=2,
                linecolor="black",
                mirror=True,
                gridwidth=1,
                gridcolor="LightPink",
            ),
            title="VELOCIDAD",
        ),
    }


@app.callback(Output("fren-graph", "figure"), [Input("graph-update", "n_intervals")])
def update_graph_scatter(n):
    data = pd.read_csv("datosSimuladorCorregidos.csv")
    Y2.append(data["fren"][n])
    graph = go.Scatter(
        x=list(X),
        y=list(Y2),
        name="Scatter",
        mode="lines+markers",
        line=dict(color="#F55643"),
    )

    return {
        "data": [graph],
        "layout": go.Layout(
            xaxis=dict(
                range=[min(X), max(X)],
                title="Longitud Recorrida (m)",
                showline=True,
                linewidth=2,
                linecolor="black",
                mirror=True,
                gridwidth=1,
                gridcolor="LightBlue",
            ),
            yaxis=dict(
                range=[0, 1],
                title="Presión de Frenada (atm)",
                showline=True,
                linewidth=2,
                linecolor="black",
                mirror=True,
                gridwidth=1,
                gridcolor="LightBlue",
            ),
            title="FRENADA",
        ),
    }


@app.callback(Output("marcha-graph", "figure"), [Input("graph-update", "n_intervals")])
def update_graph_scatter(n):
    data = pd.read_csv("datosSimuladorCorregidos.csv")
    Y3.append(data["marcha"][n])

    graph = go.Scatter(
        x=list(X),
        y=list(Y3),
        name="Scatter",
        mode="lines+markers",
        line=dict(color="#03D750"),
    )

    return {
        "data": [graph],
        "layout": go.Layout(
            xaxis=dict(
                range=[min(X), max(X)],
                title="Longitud Recorrida (m)",
                showline=True,
                linewidth=2,
                linecolor="black",
                mirror=True,
                gridwidth=1,
                gridcolor="LightPink",
            ),
            yaxis=dict(
                range=[-1, 6],
                title="Marcha Actual",
                showline=True,
                linewidth=2,
                linecolor="black",
                mirror=True,
                gridwidth=1,
                gridcolor="LightPink",
            ),
            title="MARCHA",
        ),
    }


@app.callback(Output("gauge", "value"), [Input("graph-update", "n_intervals")])
def update_gauge(n):
    data = pd.read_csv("datosSimuladorCorregidos.csv")
    return data["revact"][n]


@app.callback(Output("tank", "value"), [Input("graph-update", "n_intervals")])
def update_output(n):
    data = pd.read_csv("datosSimuladorCorregidos.csv")
    return int(data["comb"][n])


comb_predic = predictor.Predictor()


@app.callback(Output("comb-graph", "figure"), [Input("graph-update", "n_intervals")])
def update_graph_scatter(n):
    data = pd.read_csv("datosSimuladorCorregidos.csv")
    X4.append(data["xtime"][n])
    Y4.append(data["comb"][n])

    comb_predic.añadirDatos(list(Y4), list(X4), 100)
    punto0 = comb_predic.predecirX([0])
    punto = math.ceil(punto0[0])
    prec = list(range(max(X4), punto, 1))
    prec.append(punto0[0])
    Yp = comb_predic.predecirY(prec)

    graph = go.Scatter(
        x=list(X4), y=list(Y4), name="Combustible actual", fill="tozeroy", mode="lines"
    )

    graph2 = go.Scatter(
        x=prec,
        y=Yp,
        name="Predicción combustible",
        mode="markers",
        line=dict(color="#FF7F0E"),
    )

    return {
        "data": [graph, graph2],
        "layout": go.Layout(
            xaxis=dict(range=[min(X4), punto], title="TIME (s)"),
            yaxis=dict(range=[0, 100], title="COMB ( % )"),
            title="% COMB / TIME",
        ),
    }


if __name__ == "__main__":
    app.run_server(debug=False)
