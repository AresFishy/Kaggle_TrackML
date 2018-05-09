from plotly.offline import iplot, init_notebook_mode
import plotly.graph_objs as go
import plotly.figure_factory as ff

def plotly_trace(x,y,z):
    trace1 = go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode='markers',
    marker=dict(
        size=6
#         line=dict(
#             color='rgba(217, 217, 217, 0.14)',
#             width=0.5
        ),
        opacity=1
    ),
    return trace1[0]
