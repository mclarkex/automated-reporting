import holoviews as hv
import pandas as pd
from holoviews import opts

hv.extension('bokeh')

# Define the data
data = {
    'Measure': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Total Forecast': [7.30, 10.10, 12.90, 15.70, 18.50, 21.30, 24.10, 26.90, 29.70, 32.50, 35.30, 38.10],
    'Total Actual': [7.30, 10.10, 12.90, 15.70, 15.44, None, None, None, None, None, None, None],
    'Total Target': [5.50, 11.00, 16.50, 22.00, 27.50, 33.00, 38.50, 44.00, 49.50, 55.00, 60.50, 66.00]
}

df = pd.DataFrame(data)

# Convert the data into a long format for the chord diagram
long_df = pd.melt(df, id_vars=['Measure'], var_name='Type', value_name='Value')
long_df.dropna(inplace=True)

# Define custom colors for nodes
colors = {
    'Total Forecast': '#1f77b4',  # Blue for forecast
    'Total Actual': '#ff7f0e',  # Orange for actual
    'Total Target': '#2ca02c'  # Green for target
}

# Create a mapping from Measure and Type to colors
color_map = {f"{row['Measure']} - {row['Type']}": colors[row['Type']] for _, row in long_df.iterrows()}

# Prepare edges and nodes data for the chord diagram
edges_data = {
    'source': [],
    'target': [],
    'value': []
}
nodes = set()

for i, row in long_df.iterrows():
    source_node = f"{row['Measure']} - {row['Type']}"
    nodes.add(source_node)
    next_measure = df['Measure'][(df['Measure'].index(row['Measure']) + 1) % len(df['Measure'])]
    for type_ in ['Total Forecast', 'Total Actual', 'Total Target']:
        if pd.notna(df.loc[df['Measure'] == next_measure, type_].values[0]):
            target_node = f"{next_measure} - {type_}"
            nodes.add(target_node)
            edges_data['source'].append(source_node)
            edges_data['target'].append(target_node)
            edges_data['value'].append(row['Value'])

nodes_info = pd.DataFrame({'name': list(nodes)})
edges = pd.DataFrame(edges_data)

# Create HoloViews Datasets for nodes and edges
edges_ds = hv.Dataset(edges, ['source', 'target'], 'value')
nodes_ds = hv.Dataset(nodes_info, 'name')

# Create Chord diagram
chord = hv.Chord((edges_ds, nodes_ds)).opts(
    opts.Chord(
        labels='name',
        cmap='Category20',
        edge_cmap='Category20',
        node_color=hv.dim('name').categorize(color_map),
        node_size=10,
        edge_color=hv.dim('source').str(),
        width=1000,
        height=1000,
        title="Cloud Migration Forecast vs Actual vs Target Flow",
        fontsize={'labels': '10pt', 'title': '14pt'},
        edge_hover_line_color='red',
        tools=['hover'],
        toolbar='above'
    )
)

# Save the plot as an HTML file
hv.save(chord, 'forecast_migration_chord_diagram.html', backend='bokeh')

# Display the plot
chord
