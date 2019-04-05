from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource
from bokeh.palettes import GnBu3, OrRd3, Spectral6
from bokeh.plotting import figure
from bokeh.transform import factor_cmap, factor_mark

output_file("bar_h_titanic.html")




# Define sample Data
ports = ['Southampton', 'Cherbourg', 'Queenstown (Cobh)']
age = [29.2434, 30.1781, 28.03247]

#Define our colour Palette
blue3 = ['#c6dbef', '#6baed6', '#2171b5']

# Enable colouring of categorical data
source = ColumnDataSource(data=dict(age=age, ports=ports, color=blue3))

TOOLTIPS_HBAR = [
    ("age", "$age"),
    ("ports", "$ports"),
]



# Set the plot dimensions and title
# You can remove the chart tools as follows:
# toolbar_location=None, tools=""
p = figure(y_range=ports, plot_height=600, plot_width=1071,
    title="Titanic Passenger Average Age by Departure Location",
    tooltips=TOOLTIPS_HBAR)

# Draw the horizonal bar within the outline figure
p.hbar(y='ports', right='age', height=0.5,  color='color', legend="ports", source=source)


# Removes the chart gridlines (i.e.. removes the chart clutter)
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None

# change just some things about the x-axes
p.xaxis.axis_label = "Average Passenger Age (in Years)"
p.xaxis.axis_line_width = 2
p.xaxis.major_label_text_color = "black"
p.xaxis.axis_line_color = "#aeb3b7"


# change just some things about the y-axes
p.yaxis.axis_label = "Name of Port"
p.yaxis.axis_line_width = 2
p.yaxis.major_label_text_color = "black"
p.yaxis.axis_line_color = "#aeb3b7"
p.yaxis.major_label_orientation = "vertical"


# Set the range of the chart (can overide figure settings)
p.x_range.start = 0
p.x_range.end = 35


# Remove the border. Set the width to 0 does not work so we need
# to set to 0.1 to make it less visible.
p.outline_line_width = 0.1

# Set attributes for the chart title
p.title.text_color = "black"
#p.title.text_font = "times"
#p.title.text_font_style = "italic"
p.title.align = "center"


# Set the position and orientation of the legend and remove
# the legend border
p.legend.orientation = "vertical"
p.legend.location = "top_right"
p.legend.border_line_width = 0.1

# Rotate the orientation of the y label data
# Don't set to 0 as it will encroach on the chart columns
# Setting to a value close to 0 would show an almost horitzonal
# Category
p.yaxis.major_label_orientation = 0.0001


show(p)
