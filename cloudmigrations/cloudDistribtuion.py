import matplotlib.pyplot as plt

# Data
labels = ['AWS Cloud Foundations', 'Azure Cloud Foundations', 'All other AWS', 'All other Azure']
sizes = [5.72, 7.40, 28.88, 48.00]

# Brand colors
aws_color = '#FF9900'
azure_color = '#0072C6'
other_aws_color = '#FFD580'  # lighter shade of AWS orange
other_azure_color = '#66B2FF'  # lighter shade of Azure blue
colors = [aws_color, azure_color, other_aws_color, other_azure_color]

explode = (0.1, 0.1, 0, 0)  # explode the first two slices

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
                                  shadow=True, startangle=140, textprops={'fontsize': 14}, pctdistance=0.85)

# Draw a circle at the center to make it look like a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Customize the appearance of the pie chart
for text in texts + autotexts:
    text.set_color('#333333')  # set text color to dark grey
    text.set_fontsize(14)
    
# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')

plt.title('Current Cloud Distribution', fontsize=18, color='#333333', weight='bold')
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt

# Data
labels = ['AWS Cloud Foundations', 'Azure Cloud Foundations', 'All other AWS', 'All other Azure']
sizes = [5.72, 7.40, 28.88, 48.00]

# Brand colors
aws_color = '#FF9900'
azure_color = '#0072C6'
other_aws_color = '#FFD580'  # lighter shade of AWS orange
other_azure_color = '#66B2FF'  # lighter shade of Azure blue
colors = [aws_color, azure_color, other_aws_color, other_azure_color]

explode = (0.05, 0.05, 0, 0)  # slight explode for the first two slices

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
                                  shadow=False, startangle=140, textprops={'fontsize': 14}, pctdistance=0.85)

# Customize the appearance of the pie chart
for text in texts:
    text.set_color('#333333')  # set text color to dark grey
    text.set_fontsize(14)

for autotext in autotexts:
    autotext.set_color('white')  # set percentage text color to white
    autotext.set_fontsize(14)

# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')

plt.title('Current Cloud Distribution', fontsize=18, color='#333333', weight='bold')
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt

# Data
labels = ['AWS Cloud Foundations', 'Azure Cloud Foundations', 'All other AWS', 'All other Azure']
sizes = [5.72, 7.40, 28.88, 48.00]

# Brand colors
aws_color = '#FF9900'
azure_color = '#0072C6'
other_aws_color = '#FFD580'  # lighter shade of AWS orange
other_azure_color = '#66B2FF'  # lighter shade of Azure blue
colors = [aws_color, azure_color, other_aws_color, other_azure_color]

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
                                  shadow=False, startangle=140, textprops={'fontsize': 14}, pctdistance=0.85)

# Customize the appearance of the pie chart
for text in texts:
    text.set_color('#333333')  # set text color to dark grey
    text.set_fontsize(14)

for autotext in autotexts:
    autotext.set_color('white')  # set percentage text color to white
    autotext.set_fontsize(14)

# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')

# Add transparency to the background
fig.patch.set_alpha(0.0)

plt.title('Current Cloud Distribution', fontsize=18, color='#333333', weight='bold')
plt.tight_layout()
plt.show()


