import pandas as pd
import matplotlib.pyplot as plt
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
    'Total Actual': [7.30, 10.10, 12.90, 15.70, 15.44, None, None, None, None, None, None, None],
    'Total Target': [5.50, 11.00, 16.50, 22.00, 27.50, 33.00, 38.50, 44.00, 49.50, 55.00, 60.50, 66.00]
}

df = pd.DataFrame(data)

# Calculate month-over-month growth rate for forecasted migration rates
df['Forecast Growth Rate'] = df['Total Forecast'].pct_change().fillna(0) * 100
df['Actual Growth Rate'] = df['Total Actual'].pct_change().fillna(0) * 100
df['Target Growth Rate'] = df['Total Target'].pct_change().fillna(0) * 100

# Set plot style
plt.style.use('seaborn-v0_8-whitegrid')

# Create the plot for Forecast vs Actual vs Target
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot each line with distinct styles and company colors
ax1.plot(df['Measure'], df['Total Forecast'], marker='o', markersize=10, label='Total Forecast', linewidth=2, color=core_blue, zorder=3)
ax1.plot(df['Measure'], df['Total Actual'], marker='s', markersize=10, label='Total Actual', linestyle='--', linewidth=2, color=core_yellow, zorder=3)
ax1.plot(df['Measure'], df['Total Target'], marker='D', markersize=10, label='Total Target', linestyle=':', linewidth=2, color=core_green, zorder=3)

# Fill between Actual and Target with company colors
actual_up_to = df['Total Actual'].last_valid_index()
ax1.fill_between(df['Measure'][:actual_up_to + 1], df['Total Actual'][:actual_up_to + 1], df['Total Target'][:actual_up_to + 1], where=(df['Total Actual'][:actual_up_to + 1] < df['Total Target'][:actual_up_to + 1]), color=core_red, alpha=0.3, interpolate=True, label='Below Target', zorder=1)
ax1.fill_between(df['Measure'][:actual_up_to + 1], df['Total Actual'][:actual_up_to + 1], df['Total Target'][:actual_up_to + 1], where=(df['Total Actual'][:actual_up_to + 1] > df['Total Target'][:actual_up_to + 1]), color=core_green, alpha=0.3, interpolate=True, label='Above Target', zorder=1)

# Extend the y-axis to ensure all data fits within the grid
ax1.set_ylim(0, 70)

# Plot growth rate on secondary axis
ax2 = ax1.twinx()
ax2.plot(df['Measure'], df['Actual Growth Rate'], marker='x', markersize=10, label='Actual Growth Rate', linewidth=2, color=core_red, linestyle='--')
ax2.set_ylabel('Actual Growth Rate (%)', fontsize=16, color=core_red)
ax2.tick_params(axis='y', labelcolor=core_red)

# Function to adjust annotation positions to avoid overlap
def annotate_points(ax, x, y, y_offsets):
    for i, txt in enumerate(y):
        if txt is not None:
            y_offset = y_offsets[i]
            ax.annotate(f'{txt:.2f}%', (x[i], y[i]), textcoords="offset points", xytext=(0, y_offset), ha='center', fontsize=12, bbox=dict(facecolor='white', alpha=0.8))

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

# Data for the updated monthly migration rates
migration_data = {
    'Measure': ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Forecasted Migration Rate': [7.30, 10.10, 12.90, 15.70, 18.50, 21.30, 24.10, 26.90, 29.70, 32.50, 35.30, 38.10],
    'Actual Migration Rate': [7.30, 10.10, 12.90, 15.70, 15.44, None, None, None, None, None, None, None],
    'Target Migration Rate': [5.50, 11.00, 16.50, 22.00, 27.50, 33.00, 38.50, 44.00, 49.50, 55.00, 60.50, 66.00]
}

df_migration = pd.DataFrame(migration_data)

# Create the plot for Monthly Migration Rates
fig, ax3 = plt.subplots(figsize=(14, 8))

# Plot each line with distinct styles and company colors
ax3.plot(df_migration['Measure'], df_migration['Forecasted Migration Rate'], marker='o', markersize=10, label='Forecasted Migration Rate', linewidth=2, color=core_blue)
ax3.plot(df_migration['Measure'], df_migration['Actual Migration Rate'], marker='s', markersize=10, label='Actual Migration Rate', linestyle='--', linewidth=2, color=core_yellow)
ax3.plot(df_migration['Measure'], df_migration['Target Migration Rate'], marker='D', markersize=10, label='Target Migration Rate', linestyle=':', linewidth=2, color=core_green)

# Fill between Actual and Target with company colors
ax3.fill_between(df_migration['Measure'], df_migration['Actual Migration Rate'], df_migration['Target Migration Rate'], where=(df_migration['Actual Migration Rate'] < df_migration['Target Migration Rate']), color=core_red, alpha=0.3, interpolate=True, label='Below Target')
ax3.fill_between(df_migration['Measure'], df_migration['Actual Migration Rate'], df_migration['Target Migration Rate'], where=(df_migration['Actual Migration Rate'] > df_migration['Target Migration Rate']), color=core_green, alpha=0.3, interpolate=True, label='Above Target')

# Extend the y-axis to ensure all data fits within the grid
ax3.set_ylim(0, 70)

# Annotate monthly migration rates
annotate_points(ax3, df_migration['Measure'], df_migration['Actual Migration Rate'], y_offsets_actual)
annotate_points(ax3, df_migration['Measure'], df_migration['Target Migration Rate'], y_offsets_target)

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

# Create the plot for Month-over-Month Growth Rates
fig, ax4 = plt.subplots(figsize=(14, 8))

# Plot each line with distinct styles and company colors
ax4.plot(df['Measure'], df['Forecast Growth Rate'], marker='o', markersize=10, label='Forecast Growth Rate', linewidth=2, color=core_blue)
ax4.plot(df['Measure'], df['Actual Growth Rate'], marker='s', markersize=10, label='Actual Growth Rate', linestyle='--', linewidth=2, color=core_yellow)
ax4.plot(df['Measure'], df['Target Growth Rate'], marker='D', markersize=10, label='Target Growth Rate', linestyle=':', linewidth=2, color=core_green)

# Annotate growth rates
annotate_points(ax4, df['Measure'], df['Forecast Growth Rate'], y_offsets_actual)
annotate_points(ax4, df['Measure'], df['Actual Growth Rate'], y_offsets_actual)
annotate_points(ax4, df['Measure'], df['Target Growth Rate'], y_offsets_target)

# Titles and labels
ax4.set_title('Month-over-Month Growth Rates', fontsize=24, color=charcoal, weight='bold')
ax4.set_xlabel('Month', fontsize=16, color=charcoal)
ax4.set_ylabel('Growth Rate (%)', fontsize=16, color=charcoal)
ax4.legend(fontsize=14, loc='upper left', frameon=True, facecolor='white', edgecolor=charcoal)
ax4.grid(True, color=charcoal, alpha=0.3)
ax4.tick_params(axis='x', rotation=45, labelsize=14, labelcolor=charcoal)
ax4.tick_params(axis='y', labelsize=14, labelcolor=charcoal)

plt.tight_layout()
plt.show()


