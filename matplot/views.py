import plotly.graph_objects as go
import time

import pandas as pd

data = pd.read_csv('C:/Users/Carlos/data.csv')

fig = go.FigureWidget()
fig.add_scatter()
fig
for i in range(20):
    time.sleep(0.3)
    data = pd.read_csv('C:/Users/Carlos/data.csv')
    fig.data[0].y = data['total_1']

# fig is plotly figure object and graph_div the html code for displaying the graph
graph_div = fig.show()
# pass the div to the template