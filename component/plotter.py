import plotly.graph_objects as go
import numpy as np
from core.eval_f import evaluate

def plot_functions(expressions, x_range, y_range, extra_funcs=None):
    x = np.linspace(x_range[0], x_range[1], 1000)
    fig = go.Figure()

    for expr in expressions:
        try:
            y = evaluate(expr, x)
            fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=expr))
        except:
            continue


    if extra_funcs:
        for name, func in extra_funcs:
            try:
                y = func(x)
                fig.add_trace(go.Scatter(
                    x=x, y=y, mode='lines',
                    name=name,
                    line=dict(dash='dash')  # visually different
                ))
            except:
                continue

    fig.update_layout(
        title="Sketcher",
        xaxis=dict(range=[x_range[0], x_range[1]]),
        yaxis=dict(range=[y_range[0], y_range[1]])
    )

    return fig