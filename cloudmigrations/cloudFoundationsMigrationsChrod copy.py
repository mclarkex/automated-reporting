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

# Create HoloViews Datasets
forecast = hv.Curve(df, 'Measure', 'Total Forecast', label='Total Forecast')
actual = hv.Curve(df, 'Measure', 'Total Actual', label='Total Actual').opts(line_dash='dashed')
target = hv.Curve(df, 'Measure', 'Total Target', label='Total Target').opts(line_dash='dotted')

# Combine into an overlay
overlay = (forecast * actual * target).opts(
    opts.Curve(width=800, height=600, tools=['hover'], show_grid=True),
    opts.Overlay(legend_position='top_left', title="Cloud Migration Forecast vs Actual vs Target"),
    opts.Labels(text_color='black', text_font_size='10pt')
)

# Save the plot as an HTML file
hv.save(overlay, 'forecast_migration_chart.html', backend='bokeh')

# Display the plot
overlay
