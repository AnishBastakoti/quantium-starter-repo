from dash import Dash, html, dcc, Output, Input
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
    color="Region",       # Each Region gets its own color
    line_group="Region",  # Connect points for the same region
    markers=True          # Optional: show markers on points
)
#giving color

region_colors = {
    "north": "blue",
    "east": "green",
    "south": "red",
    "west": "black"
}
# Dash layout
app.layout = html.Div(children=[
    html.H4(children='Pink Morsels Sales'),

    html.P(children='Dash: Data visualization for our pink morsels sales.'),

    dcc.Graph(
        id='example-graph', style={'flex': '4'},
        figure=fig
    ),
    dcc.RadioItems(
        id='region-selector',
        options=[{'label': r, 'value': r} for r in ['All'] + list(region_colors.keys())],
        
        value='All',
        inline=False,
        style={'flex': '1','marginLeft': '20px', 'display': 'flex', 'flexDirection': 'grid'}
    )
])
"""{'label': 'North', 'value': 'north'},
        {'label': 'East', 'value': 'east'},
        {'label': 'South', 'value': 'south'},
        {'label': 'West', 'value': 'west'},
        {'label': 'All', 'value': 'All'}
"""

# Callback to update graph

@app.callback(
    Output('example-graph', 'figure'),
    Input('region-selector', 'value')
)
def update_graph(selected_region):
    if selected_region == 'All':
        filtered_df = df
        color_arg = None #removed color in all
    else:
        filtered_df = df[df['Region'].str.lower() == selected_region]
        color_arg = 'Region'

    fig = px.line(
        filtered_df,
        x='Date',
        y='Sales',
        color=color_arg,  # Each region gets its own color
        markers=True,
        line_group='Region',
        title=f"Pink Morsels Sales: {selected_region}",
        color_discrete_map=region_colors
    )
    return fig

if __name__ == '__main__':
    app.run(debug=True)
