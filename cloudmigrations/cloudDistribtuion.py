import matplotlib.pyplot as plt

# Data
labels = ['AWS Cloud Foundations', 'Azure Cloud Foundations', 'All other AWS', 'All other Azure']
sizes = [5.72, 7.40, 28.88, 48.00]
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99']
explode = (0.1, 0.1, 0, 0)  # explode the first two slices

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
       shadow=True, startangle=140, textprops={'fontsize': 14})

# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')

plt.title('Current Cloud Distribution', fontsize=18, color='#333333', weight='bold')
plt.show()
