from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.plotting import figure, output_file, show
from bokeh.transform import factor_cmap

output_file("bar_v_initial.html")

ticket= ['First', 'Second', 'Third']
counts = [84.15, 20.66, 13.68]

source = ColumnDataSource(data=dict(fruits=fruits, counts=counts))

p = figure(x_range=fruits, plot_height=250,
    title="Average Titanic Fare, by Class")

p.vbar(x='ticket', top='counts', width=0.9,
    source=source, legend="ticket,
    line_color='white',
    fill_color=factor_cmap('ticket', palette=Spectral6, factors=fruits))

p.xgrid.grid_line_color = None
p.y_range.start = 0
p.y_range.end = 90
p.legend.orientation = "horizontal"
p.legend.location = "top_center"

show(p)
