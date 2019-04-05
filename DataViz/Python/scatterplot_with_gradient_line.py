import numpy as np

from bokeh.plotting import figure, show, output_file
from bokeh.models import Slope

output_file("slope.html", title="slope.py example")



# Lets set up some contrived data
xpts = [1.1 ,2,3.3,4,5.5,6,7.7]
ypts = [1,2.2 ,3,4.4,5,6.6,7]


# linear equation parameters (obtained from a prior simple linear regression)
gradient = 0.94
y_intercept = 0.1966


# Set the figure up
p = figure(plot_height=480, plot_width= 647,
    y_range=(0, 1.1 * max(ypts)),
    title="Scatterplot with fitted regression line")

# plot the points within the figure
p.circle(xpts, ypts, size=10, color="#aeb3b7")



slope = Slope(gradient=gradient, y_intercept=y_intercept,
    line_color='#3a6587', line_dash='dotted', line_width=2)

p.add_layout(slope)


# Removes the chart gridlines (i.e.. removes the chart clutter)
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None

# Remove the border. Set the width to 0 does not work so we need
# to set to 0.1 to make it less visible.
p.outline_line_width = 0.1


# change just some things about the x-axes
p.xaxis.axis_label = "Independent Variable"
p.xaxis.axis_line_width = 2
p.xaxis.major_label_text_color = "black"
p.xaxis.axis_line_color = "#aeb3b7"
p.xaxis.major_label_text_font_size="10pt"
p.xaxis.axis_label_text_font_size = "14pt"


# change just some things about the y-axes
p.yaxis.axis_label = "Dependent Variable"
p.yaxis.axis_line_width = 2
p.yaxis.major_label_text_color = "black"
p.yaxis.axis_line_color = "#aeb3b7"
p.yaxis.major_label_orientation = "vertical"
p.yaxis.major_label_text_font_size="10pt"
p.yaxis.axis_label_text_font_size = "14pt"


# Set attributes for the chart title
p.title.align = "center"
p.title.text_font_size ="12pt"

show(p)
