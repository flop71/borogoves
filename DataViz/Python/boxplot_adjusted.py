import numpy as np
import pandas as pd

from bokeh.plotting import figure, show, output_file

# generate some synthetic time series for six different categories
cats = list("abcdef")
yy = np.random.randn(2000)
g = np.random.choice(cats, 2000)
for i, l in enumerate(cats):
    yy[g == l] += i // 2
df = pd.DataFrame(dict(score=yy, group=g))

# find the quartiles and IQR for each category
groups = df.groupby('group')
q1 = groups.quantile(q=0.25)
q2 = groups.quantile(q=0.5)
q3 = groups.quantile(q=0.75)
iqr = q3 - q1
upper = q3 + 1.5*iqr
lower = q1 - 1.5*iqr

# find the outliers for each category
def outliers(group):
    cat = group.name
    return group[(group.score > upper.loc[cat]['score']) | (group.score < lower.loc[cat]['score'])]['score']
out = groups.apply(outliers).dropna()

# prepare outlier data for plotting, we need coordinates for every outlier.
if not out.empty:
    outx = []
    outy = []
    for keys in out.index:
        outx.append(keys[0])
        outy.append(out.loc[keys[0]].loc[keys[1]])

# Background fill colour #efefef. We can change to white and add a
# horizontal grid line of #efefef, instead of white
p = figure(tools="", background_fill_color="white",
    x_range=cats, toolbar_location=None,
    title="Response location scores for seven measles treatments")

# if no outliers, shrink lengths of stems to be no longer than the minimums or maximums
qmin = groups.quantile(q=0.00)
qmax = groups.quantile(q=1.00)
upper.score = [min([x,y]) for (x,y) in zip(list(qmax.loc[:,'score']),upper.score)]
lower.score = [max([x,y]) for (x,y) in zip(list(qmin.loc[:,'score']),lower.score)]

# stems.  Colours for the boxes are set with the fill
p.segment(cats, upper.score, cats, q3.score, line_color="black")
p.segment(cats, lower.score, cats, q1.score, line_color="black")


# boxes. Colours for the boxes are set with the fill
p.vbar(cats, 0.7, q2.score, q3.score, fill_color="#3a6587", line_color="black")
p.vbar(cats, 0.7, q1.score, q2.score, fill_color="#aeb3b7", line_color="black")

# whiskers (almost-0 height rects simpler than segments)
p.rect(cats, lower.score, 0.2, 0.01, line_color="black")
p.rect(cats, upper.score, 0.2, 0.01, line_color="black")

# outliers. Colours for the boxes are set with the fill
if not out.empty:
    p.circle(outx, outy, size=8, color="#F38630", fill_alpha=0.7) #orange



# Set gridlines for box (we add gridlines as the boxplot is a
# statistical chart)
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None
#p.ygrid.grid_line_color = "#efefef"
#p.grid.grid_line_width = 1



# Removes the chart gridlines (i.e.. removes the chart clutter)
#p.xgrid.grid_line_color = None
#p.ygrid.grid_line_color = None

# change just some things about the x-axes
p.xaxis.axis_label = "Treatment category"
p.xaxis.axis_line_width = 2
p.xaxis.major_label_text_color = "black"
p.xaxis.axis_line_color = "#aeb3b7"
p.xaxis.axis_label_text_font_size = "14pt"
p.xaxis.major_label_text_font_size="14pt"

# change just some things about the y-axes
p.yaxis.axis_label = "Treatment response score"
p.yaxis.axis_line_width = 2
p.yaxis.major_label_text_color = "black"
p.yaxis.axis_line_color = "#aeb3b7"
p.yaxis.major_label_orientation = "vertical"
p.yaxis.axis_label_text_font_size = "14pt"


# Remove the border. Set the width to 0 does not work so we need
# to set to 0.1 to make it less visible.
p.outline_line_width = 0.1


# Set attributes for the chart title
p.title.align = "center"
p.title.text_font_size ="12pt"



# Set the position and orientation of the legend and remove
# the legend border
#p.legend.orientation = "vertical"
#p.legend.location = "top_right"
#p.legend.border_line_width = 0.1






output_file("boxplot.html", title="boxplot.py example")

show(p)
