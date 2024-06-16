import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np

# Company colors
core_blue = '#0076D6'
core_green = '#028844'
core_yellow = '#FFD500'
core_red = '#E22922'
charcoal = '#333333'

# Use a commonly available font
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 12

# Data
data = {
    'Measure': ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Total Forecast': [7.30, 10.10, 12.90, 15.70, 18.50, 21.30, 24.10, 26.90, 29.70, 32.50, 35.30, 38.10],
    'Total Actual': [7.30, 10.10, 12.90, 15.70, 15.44, 16.5, 17.2, 18.0, 19.0, 20.0, 21.0, 22.0],
    'Total Target': [5.50, 11.00, 16.50, 22.00, 27.50, 33.00, 38.50, 44.00, 49.50, 55.00, 60.50, 66.00]
}

df = pd.DataFrame(data)

# Calculate month-over-month growth rate for forecasted migration rates
df['Forecast Growth Rate'] = df['Total Forecast'].pct_change().fillna(0) * 100

# Set plot style
plt.style.use('seaborn-v0_8-whitegrid')

# Create the plot for Forecast vs Actual vs Target
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot each line with distinct styles and company colors
ax1.plot(df['Measure'], df['Total Forecast'], marker='o', markersize=10, label='Total Forecast', linewidth=2, color=core_blue, zorder=3)
ax1.plot(df['Measure'], df['Total Actual'], marker='s', markersize=10, label='Total Actual', linestyle='--', linewidth=2, color=core_yellow, zorder=3)
ax1.plot(df['Measure'], df['Total Target'], marker='D', markersize=10, label='Total Target', linestyle=':', linewidth=2, color=core_green, zorder=3)

# Fill between Actual and Target with company colors
ax1.fill_between(df['Measure'], df['Total Actual'], df['Total Target'], where=(df['Total Actual'] < df['Total Target']), color=core_red, alpha=0.3, interpolate=True, label='Below Target', zorder=1)
ax1.fill_between(df['Measure'], df['Total Actual'], df['Total Target'], where=(df['Total Actual'] > df['Total Target']), color=core_green, alpha=0.3, interpolate=True, label='Above Target', zorder=1)

# Plot growth rate
ax2 = ax1.twinx()
ax2.plot(df['Measure'], df['Forecast Growth Rate'], marker='x', markersize=10, label='Forecast Growth Rate', linewidth=2, color=core_red, linestyle='--')
ax2.set_ylabel('Forecast Growth Rate (%)', fontsize=16, color=core_red)
ax2.tick_params(axis='y', labelcolor=core_red)

# Function to adjust annotation positions to avoid overlap
def annotate_points(ax, x, y, y_offsets):
    for i, txt in enumerate(y):
        if txt is not None:
            y_offset = y_offsets[i]
            ax.annotate(f'{txt:.2f}%', (x[i], y[i]), textcoords="offset points", xytext=(0,y_offset), ha='center', fontsize=12, bbox=dict(facecolor='white', alpha=0.8))

# Define custom y-offsets for annotations
y_offsets_actual = [20, -20, 30, -30] + [15, -15] * ((len(df) - 4) // 2)
y_offsets_target = [-20, 20, -30, 30] + [-15, 15] * ((len(df) - 4) // 2)

# Add annotations for key points with custom y-offsets
annotate_points(ax1, df['Measure'], df['Total Actual'], y_offsets_actual)
annotate_points(ax1, df['Measure'], df['Total Target'], y_offsets_target)

# Titles and labels
ax1.set_title('Forecast vs Actual vs Target', fontsize=24, color=charcoal, weight='bold')
ax1.set_xlabel('Month', fontsize=16, color=charcoal)
ax1.set_ylabel('Percentage', fontsize=16, color=charcoal)
ax1.legend(fontsize=14, loc='upper left', frameon=True, facecolor='white', edgecolor=charcoal)
ax1.grid(True, color=charcoal, alpha=0.3)
ax1.tick_params(axis='x', rotation=45, labelsize=14, labelcolor=charcoal)
ax1.tick_params(axis='y', labelsize=14, labelcolor=charcoal)

# Adjust the grid settings to remove double lines
ax1.grid(which='major', linestyle='-', linewidth='0.5', color=charcoal)
ax2.grid(False)  # Disable grid on secondary axis to avoid overlap

plt.tight_layout()
plt.show()

# Create the plot for Monthly Migration Rates
fig, ax3 = plt.subplots(figsize=(14, 8))

# Plot each line with distinct styles and company colors
ax3.plot(df['Measure'], df['Total Forecast'], marker='o', markersize=10, label='Forecasted Migration Rate', linewidth=2, color=core_blue)
ax3.plot(df['Measure'], df['Total Actual'], marker='s', markersize=10, label='Actual Migration Rate', linestyle='--', linewidth=2, color=core_yellow)
ax3.plot(df['Measure'], df['Total Target'], marker='D', markersize=10, label='Target Migration Rate', linestyle=':', linewidth=2, color=core_green)

# Fill between Actual and Target with company colors
ax3.fill_between(df['Measure'], df['Total Actual'], df['Total Target'], where=(df['Total Actual'] < df['Total Target']), color=core_red, alpha=0.3, interpolate=True, label='Below Target')
ax3.fill_between(df['Measure'], df['Total Actual'], df['Total Target'], where=(df['Total Actual'] > df['Total Target']), color=core_green, alpha=0.3, interpolate=True, label='Above Target')

# Annotate monthly migration rates
annotate_points(ax3, df['Measure'], df['Total Actual'], y_offsets_actual)
annotate_points(ax3, df['Measure'], df['Total Target'], y_offsets_target)

# Titles and labels
ax3.set_title('Monthly Migration Rates: Forecast vs Actual vs Target', fontsize=24, color=charcoal, weight='bold')
ax3.set_xlabel('Month', fontsize=16, color=charcoal)
ax3.set_ylabel('Migration Rate (%)', fontsize=16, color=charcoal)
ax3.legend(fontsize=14, loc='upper left', frameon=True, facecolor='white', edgecolor=charcoal)
ax3.grid(True, color=charcoal, alpha=0.3)
ax3.tick_params(axis='x', rotation=45, labelsize=14, labelcolor=charcoal)
ax3.tick_params(axis='y', labelsize=14, labelcolor=charcoal)

plt.tight_layout()
plt.show()
