import plotly.graph_objects as go

# Define the data
data = {
    'source': ['LGIM AWS Cloud', 'LGRI Azure Cloud', 'LGRS Retail Protection Azure Cloud', 'LGRS Retail Protection AWS Cloud', 'GT: Core Services Azure', 'GT: Digital AWS', 'GT: Group Data AWS'],
    'target': ['AWS Cloud Foundations', 'Azure Cloud Foundations', 'Azure Cloud Foundations', 'AWS Cloud Foundations', 'Azure Cloud Foundations', 'AWS Cloud Foundations', 'AWS Cloud Foundations'],
    'value':  [20, 30, 40, 10, 50, 60, 10]
}

# Prepare source and target indices
all_nodes = list(set(data['source'] + data['target']))
node_indices = {node: idx for idx, node in enumerate(all_nodes)}
source_indices = [node_indices[src] for src in data['source']]
target_indices = [node_indices[tgt] for tgt in data['target']]
values = data['value']

# Node colors
node_colors = ['#FF9900', '#0072C6', '#FFCC66', '#3399FF', '#FFD580', '#66B2FF', '#FFD580'] + ['#FF9900', '#0072C6']

# Link colors
link_colors = ['rgba(255, 153, 0, 0.6)', 'rgba(0, 114, 198, 0.6)', 'rgba(0, 114, 198, 0.6)', 'rgba(255, 153, 0, 0.6)',
               'rgba(0, 114, 198, 0.6)', 'rgba(255, 153, 0, 0.6)', 'rgba(255, 153, 0, 0.6)']

# Create the Sankey diagram
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=all_nodes,
        color=node_colors
    ),
    link=dict(
        source=source_indices,
        target=target_indices,
        value=values,
        color=link_colors,
        customdata=data['source'],
        hovertemplate='Source: %{customdata}<br />Target: %{target.label}<br />Value: %{value}<extra></extra>'
    )
)])

fig.update_layout(
    title_text="Cloud Distribution Flow Diagram",
    font=dict(size=12, color='black'),
    title_font=dict(size=20, color='black', family="Arial"),
    plot_bgcolor='white',
    paper_bgcolor='white',
    margin=dict(l=20, r=20, t=50, b=20)
)

fig.show()
