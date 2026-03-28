import marimo as mo
import numpy as np
import plotly.graph_objects as go

# 1. Initialize data once (using a state to keep it persistent)
np.random.seed(42)
x = np.linspace(0, 10, 50)
noise = np.random.normal(0, 1, 50)
y_true = 1.5 * x + 2 + noise

# 2. Create the UI elements
mo.md("# Linear Regression Lab")
mo.md("Try to fit the line to the data points by adjusting the parameters below.")

slope_slider = mo.ui.slider(start=-2.0, stop=5.0, step=0.1, value=1.0, label="Slope ($m$)")
intercept_slider = mo.ui.slider(start=-5.0, stop=5.0, step=0.1, value=0.0, label="Intercept ($b$)")

# Display sliders in a row
mo.hstack([slope_slider, intercept_slider])

# 3. Calculate the fit and error
m = slope_slider.value
b = intercept_slider.value
y_pred = m * x + b
mse = np.mean((y_true - y_pred)**2)

# 4. Create the Plotly visualization
fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y_true, mode='markers', name='Data Points'))
fig.add_trace(go.Scatter(x=x, y=y_pred, mode='lines', name='Your Fit', line=dict(color='red')))
fig.update_layout(title=f"Mean Squared Error: {mse:.2f}", template="minimal")

# 5. Output the plot
mo.ui.plotly(fig)