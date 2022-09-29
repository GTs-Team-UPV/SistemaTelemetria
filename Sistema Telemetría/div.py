app.layout = html.Div(
    children=[
        html.Div(
            [
                # Añadimos la grafica de velocidad
                dcc.Graph(id="vel-graph", animate=False),
                # Añadimos gráfica de presión de frenada
                dcc.Graph(id="fren-graph", animate=False),
                # Añadimos gráfica de la marcha actual
                dcc.Graph(id="marcha-graph", animate=False),
            ],
            style={
                "width": "100%",
                "display": "flex",
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
                # Gráfica de combustible en tiempo
                dcc.Graph(id="comb-graph", animate=False, style={"center": "auto"}),
                # Actualizamos funciones cada 'interval' empezando desde 'n_interval'
                dcc.Interval(id="graph-update", interval=200, n_intervals=0),
            ],
            style={
                "width": "100%",
                "display": "flex",
                "align-items": "center",
                "justify-content": "center",
            },
        ),
    ]
)
