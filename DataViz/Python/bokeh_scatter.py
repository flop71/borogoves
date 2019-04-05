from bokeh.io import show, output_file
from bokeh.plotting import figure, show
from bokeh.sampledata.iris import flowers
from bokeh.transform import factor_cmap, factor_mark
import pandas as pd
import numpy as np

output_file("scatter.html")

titanic_df = pd.read_csv('/Users/jonathandunne/Dropbox/Data_Viz_101/Chart_Workshop/titanic.csv')

# Convert the Suvived column from int64 to object
titanic_df[['Survived']] = titanic_df[['Survived']].astype(object)

# Convert the 0 & 1 to Dived and Lived
titanic_df[['Survived']] = titanic_df[['Survived']].replace(0, 'Died')
titanic_df[['Survived']] = titanic_df[['Survived']].replace(1, 'Lived')

# Control the shape the text of the legend
FATE = ['Died', 'Lived']
MARKERS = ['cross', 'circle']

# Set the Title a and size of plot
p = figure(plot_height=600, plot_width= 971,
    title = "Titanic Passenger Age & Fare by Survial Type")

# Construnct the colours
p.scatter("Fare", "Age", source=titanic_df, legend="Survived", fill_alpha=0.3,
            size=12,
            marker=factor_mark('Survived', MARKERS, FATE),
            color=factor_cmap('Survived', ['#3a6587', '#aeb3b7'], FATE))

# Set axis labels
p.xaxis.axis_label = 'Fare (In Pounds)'
p.yaxis.axis_label = 'Age (In Years)'

# Remove the Grid lines
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None

# change just some things about the x-axis
p.xaxis.axis_line_width = 2
p.xaxis.major_label_text_color = "black"
p.xaxis.axis_line_color = "#aeb3b7"

# change just some things about the y-axis
p.yaxis.axis_line_width = 2
p.yaxis.major_label_text_color = "black"
p.yaxis.axis_line_color = "#aeb3b7"

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

show(p)

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
