import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import ConnectionPatch

# Data
labels = ['AWS Cloud Foundations', 'Azure Cloud Foundations', 'All other AWS', 'All other Azure']
sizes = [5.72, 7.40, 28.88, 48.00]

# Brand colors
aws_color = '#FF9900'
azure_color = '#0072C6'
other_aws_color = '#FFCC66'  # brighter shade of AWS orange
other_azure_color = '#3399FF'  # brighter shade of Azure blue
colors = [aws_color, azure_color, other_aws_color, other_azure_color]

explode = (0.1, 0.1, 0, 0)  # explode the first two slices

# Create the pie chart
fig, ax = plt.subplots(figsize=(12, 9))
wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
                                  shadow=True, startangle=140, textprops={'fontsize': 14}, pctdistance=0.85)

# Draw a circle at the center to make it look like a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white', linewidth=1.25, edgecolor='black')
fig.gca().add_artist(centre_circle)

# Enhance the appearance of the pie chart
for i, (wedge, text, autotext) in enumerate(zip(wedges, texts, autotexts)):
    text.set_color('#333333')  # set text color to dark grey
    text.set_fontsize(14)
    autotext.set_color('white')  # set percentage text color to white
    autotext.set_fontsize(14)
    
    # Add gradient effect to each wedge
    wedge.set_edgecolor('white')
    wedge.set_linewidth(2)

# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')

# Add annotations to enhance information
for i, (text, wedge) in enumerate(zip(texts, wedges)):
    # Create the connection lines
    angle = (wedge.theta2 - wedge.theta1) / 2. + wedge.theta1
    x = np.cos(np.deg2rad(angle))
    y = np.sin(np.deg2rad(angle))

    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connection = ConnectionPatch(
        xyA=(0, 0), coordsA=ax.transData,
        xyB=(x * 1.5, y * 1.5), coordsB=ax.transData,
        arrowstyle="-", color='#333333', lw=1.5
    )
    ax.add_patch(connection)
    text.set_horizontalalignment(horizontalalignment)
    text.set_position((x * 1.6, y * 1.6))

plt.title('Current Cloud Distribution', fontsize=22, color='#333333', weight='bold', pad=20)
plt.tight_layout()
plt.show()
