from bokeh.io import output_file, show
from bokeh.layouts import gridplot  ## Needed for the dashboard
from bokeh.models import ColumnDataSource
from bokeh.palettes import GnBu3, OrRd3, Spectral6
from bokeh.plotting import figure
from bokeh.transform import factor_cmap, factor_mark
import pandas as pd
import numpy as np
from bokeh.sampledata.stocks import AAPL, GOOG, IBM, MSFT

output_file("dash_titanic.html")

# Define sample Data
ports = ['Southampton', 'Cherbourg', 'Queenstown (Cobh)']
age = [29.2434, 30.1781, 28.03247]
ticket = ['First', 'Second', 'Third']
counts = [84.15, 20.66, 13.68]
titanic_df = pd.read_csv('/Users/jonathandunne/Dropbox/Data_Viz_101/Chart_Workshop/titanic.csv')

def datetime(x):
    return np.array(x, dtype=np.datetime64)

#Define our colour Palette
blue3 = ['#c6dbef', '#6baed6', '#2171b5']

# Convert the Suvived column from int64 to object
titanic_df[['Survived']] = titanic_df[['Survived']].astype(object)

# Convert the 0 & 1 to Dived and Lived
titanic_df[['Survived']] = titanic_df[['Survived']].replace(0, 'Died')
titanic_df[['Survived']] = titanic_df[['Survived']].replace(1, 'Lived')

# Control the shape the text of the legend
FATE = ['Died', 'Lived']
MARKERS = ['cross', 'circle']


# Enable colouring of categorical data
source1 = ColumnDataSource(data=dict(age=age, ports=ports, color=blue3))
source2 = ColumnDataSource(data=dict(ticket=ticket, counts=counts))

TOOLTIPS_SCATTER = [
    ("(Fare,Age)", "$x, $y"),
]


# Set the plot dimensions and title
p1 = figure(y_range=ports, plot_height=400, plot_width=647,
    title="Titanic Passenger Average Age by Departure Location",
    toolbar_location=None, tools="")

p2 = figure(x_range=ticket, plot_height=400, plot_width= 647, toolbar_location=None,
        title="Average Titanic Fare, by Class")


p3 = figure(plot_height=400, plot_width=647,
    title = "Titanic Passenger Age & Fare by Survial Type",
    tooltips=TOOLTIPS_SCATTER)

p4 = figure(x_axis_type="datetime", plot_height=400, plot_width= 647,
    title="Stock Closing Prices")


# Draw the horizonal bar within the outline figure
p1.hbar(y='ports', right='age', height=0.5,  color='color', legend="ports", source=source1)

p2.vbar(x='ticket', top='counts', width=0.7, source=source2, legend="ticket",
       line_color='white', fill_color=factor_cmap('ticket',
        palette=['#3a6587', '#aeb3b7', '#aeb3b7'], factors=ticket))

p3.scatter("Fare", "Age", source=titanic_df, legend="Survived", fill_alpha=0.3, size=12,
          marker=factor_mark('Survived', MARKERS, FATE),
          color=factor_cmap('Survived', palette=['#3a6587', '#aeb3b7'], factors=FATE))

p4.line(datetime(AAPL['date']), AAPL['adj_close'], color='#B2DF8A',
    legend='Apple (AAPL)', line_width=2)
p4.line(datetime(GOOG['date']), GOOG['adj_close'], color='#3a6587',
    legend='Google (GOOG)', line_width=3)
p4.line(datetime(IBM['date']), IBM['adj_close'], color='#aeb3b7',
    legend='IBM', line_width=1, line_dash='dashed')
p4.line(datetime(MSFT['date']), MSFT['adj_close'], color='#aeb3b7',
    legend='Microsoft (MSFT)', line_width=1, line_dash='dotted')

# Removes the chart gridlines (i.e.. removes the chart clutter)
p1.xgrid.grid_line_color = None
p1.ygrid.grid_line_color = None

# change just some things about the x-axes
p1.xaxis.axis_label = "Average Passenger Age (in Years)"
p1.xaxis.axis_line_width = 2
p1.xaxis.major_label_text_color = "black"
p1.xaxis.axis_line_color = "#aeb3b7"

# change just some things about the y-axes
p1.yaxis.axis_label = "Name of Port"
p1.yaxis.axis_line_width = 2
p1.yaxis.major_label_text_color = "black"
p1.yaxis.axis_line_color = "#aeb3b7"
p1.yaxis.major_label_orientation = "vertical"

# Set the range of the chart (can overide figure settings)
p1.x_range.start = 0
p1.x_range.end = 41

# Remove the border. Set the width to 0 does not work so we need
# to set to 0.1 to make it less visible.
p1.outline_line_width = 0.1

# Set attributes for the chart title
p1.title.text_color = "black"
#p.title.text_font = "times"
#p.title.text_font_style = "italic"
p1.title.align = "center"

# Set the position and orientation of the legend and remove
# the legend border
p1.legend.orientation = "vertical"
p1.legend.location = "top_right"
p1.legend.border_line_width = 0.1

# Removes the chart gridlines (i.e.. removes the chart clutter)
p2.xgrid.grid_line_color = None
p2.ygrid.grid_line_color = None

# change just some things about the x-axes
p2.xaxis.axis_label = "Class Type"
p2.xaxis.axis_line_width = 2
p2.xaxis.major_label_text_color = "black"
p2.xaxis.axis_line_color = "#aeb3b7"

# change just some things about the y-axes
p2.yaxis.axis_label = "Average Fare Price (in Pounds)"
p2.yaxis.axis_line_width = 2
p2.yaxis.major_label_text_color = "black"
p2.yaxis.axis_line_color = "#aeb3b7"
p2.yaxis.major_label_orientation = "vertical"

# Set the range of the chart
p2.y_range.start = 0
p2.y_range.end = 90

# Remove the border. Set the width to 0 does not work so we need
# to set to 0.1 to make it less visible.
p2.outline_line_width = 0.1

# Set attributes for the chart title
p2.title.text_color = "black"
#p.title.text_font = "times"
#p.title.text_font_style = "italic"
p2.title.align = "center"


# Set the position and orientation of the legend and remove
# the legend border
p2.legend.orientation = "vertical"
p2.legend.location = "top_right"
p2.legend.border_line_width = 0.1


#Set the axis labels
p3.xaxis.axis_label = 'Fare (In Pounds)'
p3.yaxis.axis_label = 'Age (In Years)'

# Remove the Grid lines
p3.xgrid.grid_line_color = None
p3.ygrid.grid_line_color = None

# change just some things about the x-axis
p3.xaxis.axis_line_width = 2
p3.xaxis.major_label_text_color = "black"
p3.xaxis.axis_line_color = "#aeb3b7"

# change just some things about the y-axis
p3.yaxis.axis_line_width = 2
p3.yaxis.major_label_text_color = "black"
p3.yaxis.axis_line_color = "#aeb3b7"

# Remove the border. Set the width to 0 does not work so we need
# to set to 0.1 to make it less visible.
p3.outline_line_width = 0.1

# Set attributes for the chart title
p3.title.text_color = "black"
#p.title.text_font = "times"
#p.title.text_font_style = "italic"
p3.title.align = "center"

# Set the position and orientation of the legend and remove
# the legend border
p3.legend.orientation = "vertical"
p3.legend.location = "top_right"
p3.legend.border_line_width = 0.1

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

# make a grid
grid = gridplot([[p1, p2], [p3, p4]])

# Show the grid
show(grid)

#Appendix

#Appendix 1 Ratio's of heights to width using the golden ratio
#Height	Width
#400	647
#500	809
#600	971
#700	1133
#800	1294
#900	1456
#1000	1618


# Appendix 2 names of Legend shapes

#[Asterisk, Circle, CircleCross, CircleX, Cross, Dash, Diamond, DiamondCross,
#Hex, InvertedTriangle, Square, SquareCross, SquareX, Triangle, X]


# Appexdix 3 - Dashing options
#'solid'
#'dashed'
#'dotted'
#'dotdash'
#'dashdot'
