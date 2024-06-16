import plotly.graph_objects as go

# Define the data
data = {
    'source': ['LGIM AWS Cloud', 'LGRI Azure Cloud', 'LGRS Retail Protection Azure Cloud', 'LGRS Retail Protection AWS Cloud', 'GT: Core Services Azure', 'GT: Digital AWS', 'GT: Group Data AWS'],
    'target': ['AWS Cloud Foundations', 'Azure Cloud Foundations', 'Azure Cloud Foundations', 'AWS Cloud Foundations', 'Azure Cloud Foundations', 'AWS Cloud Foundations', 'AWS Cloud Foundations'],
    'value':  [20, 30, 40, 10, 50, 60, 10],
    'cost':  [20000, 30000, 40000, 10000, 50000, 60000, 10000],
    'time':  [6, 8, 7, 4, 9, 10, 5],  # in months
    'efficiency': [15, 20, 25, 10, 30, 35, 5],  # efficiency improvement in percentage
    'services': [10, 15, 20, 5, 25, 30, 8],  # number of services migrated
    'user_impact': [500, 600, 700, 300, 800, 900, 250],  # number of users impacted
    'cost_reduction': [10000, 12000, 15000, 5000, 20000, 25000, 4000]  # cost reduction in USD
}

# Prepare source and target indices
all_nodes = list(set(data['source'] + data['target']))
node_indices = {node: idx for idx, node in enumerate(all_nodes)}
source_indices = [node_indices[src] for src in data['source']]
target_indices = [node_indices[tgt] for tgt in data['target']]
values = data['value']
costs = data['cost']
times = data['time']
efficiencies = data['efficiency']
services = data['services']
user_impacts = data['user_impact']
cost_reductions = data['cost_reduction']

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
        customdata=list(zip(data['source'], data['target'], values, costs, times, efficiencies, services, user_impacts, cost_reductions)),
        hovertemplate=(
            'Source: %{customdata[0]}<br />'
            'Target: %{customdata[1]}<br />'
            'Value: %{customdata[2]}<br />'
            'Cost: $%{customdata[3]}<br />'
            'Time: %{customdata[4]} months<br />'
            'Efficiency Improvement: %{customdata[5]}%<br />'
            'Services Migrated: %{customdata[6]}<br />'
            'Users Impacted: %{customdata[7]}<br />'
            'Cost Reduction: $%{customdata[8]}<extra></extra>'
        )
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


# Display the plot
# Save the plot as an HTML file
fig.write_html("cloud_distribution_flow_diagram.html")
fig.show()
