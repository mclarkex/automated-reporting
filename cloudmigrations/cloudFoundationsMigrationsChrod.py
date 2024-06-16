import holoviews as hv
import pandas as pd
from holoviews import opts
from bokeh.io import output_file, save

hv.extension('bokeh')

# Example data
data = {
    'source': ['LGIM AWS Cloud', 'LGRI Azure Cloud', 'LGRS Retail Protection Azure Cloud', 'LGRS Retail Protection AWS Cloud', 'GT: Core Services Azure', 'GT: Digital AWS', 'GT: Group Data AWS'],
    'target': ['AWS Cloud Foundations', 'Azure Cloud Foundations', 'Azure Cloud Foundations', 'AWS Cloud Foundations', 'Azure Cloud Foundations', 'AWS Cloud Foundations', 'AWS Cloud Foundations'],
    'value':  [20, 30, 40, 10, 50, 60, 10],
    'cost': [20000, 30000, 40000, 10000, 50000, 60000, 10000],
    'time': [6, 8, 7, 4, 9, 10, 5],  # in months
    'efficiency': [15, 20, 25, 10, 30, 35, 5],  # efficiency improvement in percentage
    'services': [10, 15, 20, 5, 25, 30, 8],  # number of services migrated
    'user_impact': [500, 600, 700, 300, 800, 900, 250]  # number of users impacted
}

df = pd.DataFrame(data)

# Define custom colors for nodes
colors = {
    'AWS Cloud Foundations': '#FF9900',  # AWS in Orange
    'Azure Cloud Foundations': '#0072C6',  # Azure in Blue
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
        cmap='Category20',  # Use a categorical color map for edges
        edge_cmap='Category20',
        node_color=hv.dim('name').categorize(colors),  # Apply specific colors to nodes
        node_size=hv.dim('size'),  # Use pre-computed node sizes
        edge_color=hv.dim('source').str(),
        width=1000, 
        height=1000, 
        title="Cloud Cost Migration Flow",
        fontsize={'labels': '10pt', 'title': '14pt'},
        node_hover_fill_color='orange',  # Hover color for nodes
        edge_hover_line_color='red',  # Hover color for edges
        tools=['hover'],  # Add hover tool for better interactivity
        toolbar='above'
    )
)

# Enhance tooltips to include additional information
hover = chord.opts(
    opts.Chord(
        inspection_policy='nodes',  # Show tooltips on nodes
        tools=['hover'],  # Enable hover tool
        hover_line_color='red',  # Hover color for lines
        hover_fill_color='orange',  # Hover color for nodes
        tooltips=[
            ("Source", "@source"),
            ("Target", "@target"),
            ("Value", "@value"),
            ("Cost", "@cost"),
            ("Time (months)", "@time"),
            ("Efficiency (%)", "@efficiency"),
            ("Services Migrated", "@services"),
            ("Users Impacted", "@user_impact")
        ]
    )
)

# Save the plot as an HTML file
output_file("enhanced_chord_diagram.html")
save(hv.render(hover, backend='bokeh'))
hover
