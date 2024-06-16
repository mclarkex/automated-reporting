import holoviews as hv
import pandas as pd
from holoviews import opts

hv.extension('bokeh')

# Example data
data = {
    'source': ['LGIM AWS Cloud', 'LGRI Azure Cloud', 'LGRS Retail Protection Azure Cloud', 'LGRS Retail Protection AWS Cloud', 'GT: Core Services Azure', 'GT: Digital AWS', 'GT: Group Data AWS'],
    'target': ['AWS Cloud Foundations', 'Azure Cloud Foundations', 'Azure Cloud Foundations', 'AWS Cloud Foundations', 'Azure Cloud Foundations', 'AWS Cloud Foundations', 'AWS Cloud Foundations'],
    'value':  [20, 30, 40, 10, 50, 60, 10]
}

df = pd.DataFrame(data)

# Define custom colors for nodes
colors = {
    'AWS Cloud Foundations': '#ff9900',  # AWS in Reddish
    'Azure Cloud Foundations': '#069AF3',  # Azure in Blueish
    'LGIM AWS Cloud': '#B1B1B1',
    'LGRI Azure Cloud': '#C2C2C2',
    'LGRS Retail Protection Azure Cloud': '#D3D3D3',
    'LGRS Retail Protection AWS Cloud': '#D3D3D3',
    'GT: Core Services Azure': '#D3D3D3',
    'GT: Digital AWS': '#D3D3D3',
    'GT: Group Data AWS': '#D3D3D3',
}

# Prepare node sizes based on their role
node_sizes = {
    'AWS Cloud Foundations': 50,
    'Azure Cloud Foundations': 50,
    'LGIM AWS Cloud': 20,
    'LGRI Azure Cloud': 20,
    'LGRS Retail Protection Azure Cloud': 20,
    'LGRS Retail Protection AWS Cloud': 20,
    'GT: Core Services Azure': 20,
    'GT: Digital AWS': 20,
    'GT: Group Data AWS': 20,
}

# Create nodes DataFrame including the sizes
nodes_info = pd.DataFrame({
    'name': list(set(df['source'].tolist() + df['target'].tolist())),
    'size': [node_sizes[name] for name in set(df['source'].tolist() + df['target'].tolist())]
})

# Create HoloViews Datasets for nodes and edges
edges = hv.Dataset(df, ['source', 'target'], 'value')
nodes_ds = hv.Dataset(nodes_info, 'name')

# Create Chord diagram with specified node sizes
chord = hv.Chord((edges, nodes_ds)).opts(
    opts.Chord(
        labels='name', 
        cmap=colors,  # Using custom colors
        edge_cmap='Category20',
        node_color=hv.dim('name').categorize(colors),  # Apply specific colors to nodes
        node_size=hv.dim('size'),  # Use pre-computed node sizes
        edge_color=hv.dim('source').str(),
        width=800, 
        height=800, 
        title="Cloud Cost Migration Flow",
        fontsize={'labels': '10pt', 'title': '12pt'}
    )
)

# Display the plot
hv.save(chord, 'chord_diagram.html', backend='bokeh')
chord
