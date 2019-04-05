import numpy as np

from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file
from bokeh.sampledata.stocks import AAPL, GOOG, IBM, MSFT

def datetime(x):
    return np.array(x, dtype=np.datetime64)

p4 = figure(x_axis_type="datetime", plot_height=600, plot_width= 971, title="Stock Closing Prices")

p4.line(datetime(AAPL['date']), AAPL['adj_close'], color='#B2DF8A',
    legend='Apple (AAPL)', line_width=2)
p4.line(datetime(GOOG['date']), GOOG['adj_close'], color='#3a6587',
    legend='Google (GOOG)', line_width=3)
p4.line(datetime(IBM['date']), IBM['adj_close'], color='#aeb3b7',
    legend='IBM', line_width=1, line_dash='dashed')
p4.line(datetime(MSFT['date']), MSFT['adj_close'], color='#aeb3b7',
    legend='Microsoft (MSFT)', line_width=1, line_dash='dotted')

# Appexdix 3 - Dashing options
#'solid'
#'dashed'
#'dotted'
#'dotdash'
#'dashdot'


# Set attributes for the chart title
p4.title.text_color = "black"
#p.title.text_font = "times"
#p.title.text_font_style = "italic"
p4.title.align = "center"

# Define the Axis labels
p4.xaxis.axis_label = 'Year'
p4.yaxis.axis_label = 'Price'

# Remove the Grid lines
p4.xgrid.grid_line_color = None
p4.ygrid.grid_line_color = None


# change just some things about the x-axes
p4.xaxis.axis_line_width = 2
p4.xaxis.major_label_text_color = "black"
p4.xaxis.axis_line_color = "#aeb3b7"


# change just some things about the y-axis
p4.yaxis.axis_line_width = 2
p4.yaxis.major_label_text_color = "black"
p4.yaxis.axis_line_color = "#aeb3b7"

# Set the position and orientation of the legend and remove
# the legend border
p4.legend.location = "top_left"
p4.legend.border_line_width = 0.1


# Remove the border. Set the width to 0 does not work so we need
# to set to 0.1 to make it less visible.
p4.outline_line_width = 0.1

aapl = np.array(AAPL['adj_close'])
aapl_dates = np.array(AAPL['date'], dtype=np.datetime64)

window_size = 30
window = np.ones(window_size)/float(window_size)
aapl_avg = np.convolve(aapl, window, 'same')





p2 = figure(x_axis_type="datetime", plot_height=400, plot_width= 647, title="AAPL One-Month Average")
p2.grid.grid_line_alpha = 0
p2.xaxis.axis_label = 'Date'
p2.yaxis.axis_label = 'Price'
p2.ygrid.band_fill_color = "olive"
p2.ygrid.band_fill_alpha = 0.1

p2.circle(aapl_dates, aapl, size=4, legend='close',
          color='darkgrey', alpha=0.2)

p2.line(aapl_dates, aapl_avg, legend='avg', color='navy')
p2.legend.location = "top_left"

output_file("stocks.html", title="stocks.py example")

show(gridplot([[p4]]))  # open a browser
