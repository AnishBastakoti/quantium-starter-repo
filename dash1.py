from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from pathlib import Path

app = Dash(__name__)

# Load data
def load_data():
    data_dir = Path("data")
    df = pd.read_csv(data_dir / "pink_morsels_sales.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')
    return df

df = load_data()

# Create figure with colors by Region
fig = px.line(
    df,
    x="Date",
    y="Sales",
    #color="Region",       # Each Region gets its own color
    line_group="Region",  # Connect points for the same region
    markers=True          # Optional: show markers on points
)

# Dash layout
app.layout = html.Div(children=[
    html.H4(children='Pink Morsels Sales'),

    html.P(children='Dash: Data visualization for our pink morsels sales.'),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
