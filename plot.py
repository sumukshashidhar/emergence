import plotly.express as px
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

def plot():
    df = pd.read_csv('ant_data.csv', header=None)
    fig = px.line()
    fig.add_scatter(mode='lines', y=df[0] / df[4], name='worker')
    fig.add_scatter(mode='lines', y=df[1] / df[4], name='harvester')
    fig.add_scatter(mode='lines', y=df[2] / df[4], name='soldier')
    fig.add_scatter(mode='lines', y=df[3] / df[4], name='caretaker')
    fig.show()


    fig = px.line()
    fig.add_scatter(mode='lines', y=df[0], name='worker')
    fig.add_scatter(mode='lines', y=df[1], name='harvester')
    fig.add_scatter(mode='lines', y=df[2], name='soldier')
    fig.add_scatter(mode='lines', y=df[3], name='caretaker')
    fig.show()