from bokeh.io import show, output_file
from bokeh.plotting import figure, show
from bokeh.sampledata.iris import flowers
from bokeh.transform import factor_cmap, factor_mark
import pandas as pd
import numpy as np

output_file("scatter_bowlers_1877_1919.html")

titanic_df = pd.read_csv('/Users/jonathandunne/Dropbox/Data_Viz_101/Chart_Workshop/cricket_1877_1919.csv')
#print(titanic_df)


# Convert the Suvived column from int64 to object
#print(titanic_df.RightHand.dtype)
titanic_df[['RightHand']] = titanic_df[['RightHand']].astype(object)
#print(titanic_df.RightHand.dtype)


# Convert the 0 & 1 to Dived and Lived
titanic_df[['RightHand']] = titanic_df[['RightHand']].replace(0, 'Left Handed')
titanic_df[['RightHand']] = titanic_df[['RightHand']].replace(1, 'Right Handed')

#print(titanic_df[['Wickets']])
#print(titanic_df[['Average']])

# Control the shape the text of the legend
FATE = ['Left Handed', 'Right Handed']
MARKERS = ['diamond', 'circle']


TOOLTIPS_SCATTER = [
    ("First Name", "@FirstName"),
    ("Last Name", "@LastName"),
    ("Wickets", "@Wickets"),
    ("Average", "@Average"),
    ("BowlerType", "@BowlerType"),
]


# Set the Title
p = figure(title = "Top Test Bowlers by Decade (1877-1919)",
    tooltips=TOOLTIPS_SCATTER, 
    x_range=(0, 30),
    y_range=(0, 200),
    plot_width=1280, plot_height=800)

p.title.text_font_size = '24pt'

# Construnct the colours
p.scatter("Average", "Wickets", source=titanic_df, legend="RightHand", fill_alpha=0.9, size=24,
          marker=factor_mark('RightHand', MARKERS, FATE),
          color=factor_cmap('RightHand', palette=['#aeb3b7', '#3a6587'], factors=FATE))

#Set the axis labels
p.xaxis.axis_label = 'Career Bowling Average'
p.yaxis.axis_label = 'Total Career Wickets'

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
p.legend.label_text_font_size = "12pt"
p.legend.glyph_height=48
p.legend.glyph_width=48
#p.label_text_color=palette=['#aeb3b7', '#3a6587']




show(p)
