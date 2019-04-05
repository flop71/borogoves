import numpy as np
from numpy import genfromtxt
import scipy.special
import random

import matplotlib.pyplot as plt

from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file

def make_plot(title, hist, edges, x, pdf, cdf):
    p = figure(title=title, tools='')
    p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:],
           fill_color="#aeb3b7", line_color="white", alpha=0.5)
    p.line(x, pdf, line_color="#2171b5", line_width=3, alpha=0.7, legend="PDF")
    p.line(x, cdf, line_color="#6baed6", line_width=2, alpha=0.7, legend="CDF",
        line_dash='dotted')

##aeb3b7

    p.y_range.start = 0
    p.legend.location = "center_right"
    p.legend.background_fill_color = "#fefefe"
    p.xaxis.axis_label = 'x'
    p.yaxis.axis_label = 'Pr(x)'
    p.grid.grid_line_color="white"
    # Remove the border. Set the width to 0 does not work so we need
    # to set to 0.1 to make it less visible.
    p.outline_line_width = 0.1
    p.legend.border_line_width = 0.1
    return p

# Normal Distribution

mu, sigma = 0, 0.5

measured = np.random.normal(mu, sigma, 1000)
hist, edges = np.histogram(measured, density=True, bins=25)

x = np.linspace(-2, 2, 1000)
pdf = 1/(sigma * np.sqrt(2*np.pi)) * np.exp(-(x-mu)**2 / (2*sigma**2))
cdf = (1+scipy.special.erf((x-mu)/np.sqrt(2*sigma**2)))/2

p1 = make_plot("Normal Distribution (μ=0, σ=0.5)", hist, edges, x, pdf, cdf)

# Log-Normal Distribution

mu, sigma = 0, 0.5

measured = np.random.lognormal(mu, sigma, 1000)
hist, edges = np.histogram(measured, density=True, bins=25)

x = np.linspace(0.0001, 8.0, 1000)
pdf = 1/(x* sigma * np.sqrt(2*np.pi)) * np.exp(-(np.log(x)-mu)**2 / (2*sigma**2))
cdf = (1+scipy.special.erf((np.log(x)-mu)/(np.sqrt(2)*sigma)))/2

p2 = make_plot("Log Normal Distribution (μ=0, σ=0.5)", hist, edges, x, pdf, cdf)

# Gamma Distribution

k, theta = 7.5, 1.0

measured = np.random.gamma(k, theta, 1000)
hist, edges = np.histogram(measured, density=True, bins=25)

x = np.linspace(0.0001, 20.0, 1000)
pdf = x**(k-1) * np.exp(-x/theta) / (theta**k * scipy.special.gamma(k))
cdf = scipy.special.gammainc(k, x/theta)

p3 = make_plot("Gamma Distribution (k=7.5, θ=1)", hist, edges, x, pdf, cdf)

# Weibull Distribution

lam, k = 1, 1.25
measured = lam*(-np.log(np.random.uniform(0, 1, 1000)))**(1/k)
hist, edges = np.histogram(measured, density=True, bins=25)

x = np.linspace(0.0001, 8, 1000)
pdf = (k/lam)*(x/lam)**(k-1) * np.exp(-(x/lam)**k)
cdf = 1 - np.exp(-(x/lam)**k)

p4 = make_plot("Weibull Distribution (λ=1, k=1.25)", hist, edges, x, pdf, cdf)



output_file('histogram.html', title="histogram.py example")

#show(gridplot([[p1,p2],[p3, p4]], plot_width=671, plot_height=400))
show(p2)
