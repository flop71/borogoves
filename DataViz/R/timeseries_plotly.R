################## import libraries ###########

library(ggplot2)
library(MASS)
library(vcd)
library(grid)
library(fitdistrplus)
library(ADGofTest)
library(actuar)
library(moments)
library(lubridate)
library(dplyr)
library(knitr)
library(MASS)
library(multcomp)
library(plotly)
library(devtools)
devtools::install_github("rstudio/r2d3")

###############Set working Direcgtory##################################
setwd("/Users/jonathandunne/Dropbox/Data_Viz_101/Chart_Workshop")
getwd()

###############Read Data from csv ##################################
houseprice.df <- read.csv(file="HPI_master.csv", header=TRUE, sep=",")

head(houseprice.df, 5)

#Lets look at 1991 house price index in more detail
index.1991.monthly <- subset(houseprice.df, yr == 1991 & frequency == "monthly", 
                        select=c(yr, period, index_nsa))

sapply(index.1991.monthly, class)

jan.1991 <- subset(houseprice.df, period == 1, select=c(index_nsa))

nrow(jan.1991)

p.timeseries <- plot_ly(index.1991.monthly , x = ~period, y = ~index_nsa, name = 'Index', type = 'scatter', mode = 'lines',
             line = list(color = '#3a6587', width = 4))

p.timeseries





month <- c('January', 'February', 'March', 'April', 'May', 'June', 'July',
           'August', 'September', 'October', 'November', 'December')
high_2000 <- c(32.5, 37.6, 49.9, 53.0, 69.1, 75.4, 76.5, 76.6, 70.7, 60.6, 45.1, 29.3)
low_2000 <- c(13.8, 22.3, 32.5, 37.2, 49.9, 56.1, 57.7, 58.3, 51.2, 42.8, 31.6, 15.9)
high_2007 <- c(36.5, 26.6, 43.6, 52.3, 71.5, 81.4, 80.5, 82.2, 76.0, 67.3, 46.1, 35.0)
low_2007 <- c(23.6, 14.0, 27.0, 36.8, 47.6, 57.7, 58.9, 61.2, 53.3, 48.5, 31.0, 23.6)
high_2014 <- c(28.8, 28.5, 37.0, 56.8, 69.7, 79.7, 78.5, 77.8, 74.1, 62.6, 45.3, 39.9)
low_2014 <- c(12.7, 14.3, 18.6, 35.5, 49.9, 58.0, 60.0, 58.6, 51.7, 45.2, 32.2, 29.1)

data <- data.frame(month, high_2000, low_2000, high_2007, low_2007, high_2014, low_2014)

#The default order will be alphabetized unless specified as below:
data$month <- factor(data$month, levels = data[["month"]])

p.ts.1 <- plot_ly(data, x = ~month, y = ~high_2014, name = 'High 2014', type = 'scatter', mode = 'lines',
             line = list(color = 'rgb(205, 12, 24)', width = 4)) %>%
  add_trace(y = ~low_2014, name = 'Low 2014', line = list(color = 'rgb(22, 96, 167)', width = 4)) %>%
  add_trace(y = ~high_2007, name = 'High 2007', line = list(color = 'rgb(205, 12, 24)', width = 4, dash = 'dash')) %>%
  add_trace(y = ~low_2007, name = 'Low 2007', line = list(color = 'rgb(22, 96, 167)', width = 4, dash = 'dash')) %>%
  add_trace(y = ~high_2000, name = 'High 2000', line = list(color = 'rgb(205, 12, 24)', width = 4, dash = 'dot')) %>%
  add_trace(y = ~low_2000, name = 'Low 2000', line = list(color = 'rgb(22, 96, 167)', width = 4, dash = 'dot')) %>%
  layout(title = "Average High and Low Temperatures in New York",
         xaxis = list(title = "Months"),
         yaxis = list (title = "Temperature (degrees F)"))

p.ts.1


# Lets get rid of the grid lines
p.ts.2 <- plot_ly(data, x = ~month, y = ~high_2014, name = 'High 2014', type = 'scatter', mode = 'lines',
                line = list(color = 'rgb(205, 12, 24)', width = 4)) %>%
  add_trace(y = ~low_2014, name = 'Low 2014', line = list(color = 'rgb(22, 96, 167)', width = 4)) %>%
  add_trace(y = ~high_2007, name = 'High 2007', line = list(color = 'rgb(205, 12, 24)', width = 4, dash = 'dash')) %>%
  add_trace(y = ~low_2007, name = 'Low 2007', line = list(color = 'rgb(22, 96, 167)', width = 4, dash = 'dash')) %>%
  add_trace(y = ~high_2000, name = 'High 2000', line = list(color = 'rgb(205, 12, 24)', width = 4, dash = 'dot')) %>%
  add_trace(y = ~low_2000, name = 'Low 2000', line = list(color = 'rgb(22, 96, 167)', width = 4, dash = 'dot')) %>%
  layout(title = "Average High and Low Temperatures in New York",
         xaxis = list(title = "Months", showgrid = FALSE),
         yaxis = list (title = "Temperature (degrees F)", showgrid = FALSE))

p.ts.2



# Lets emphaise the 2014 values - First lets reduce the width of the 2007 and 2000 lines
p.ts.3 <- plot_ly(data, x = ~month, y = ~high_2014, name = 'High 2014', type = 'scatter', mode = 'lines',
                  line = list(color = 'rgb(205, 12, 24)', width = 4)) %>%
  add_trace(y = ~low_2014, name = 'Low 2014', line = list(color = 'rgb(22, 96, 167)', width = 4)) %>%
  add_trace(y = ~high_2007, name = 'High 2007', line = list(color = 'rgb(205, 12, 24)', width = 1, dash = 'dash')) %>%
  add_trace(y = ~low_2007, name = 'Low 2007', line = list(color = 'rgb(22, 96, 167)', width = 1, dash = 'dash')) %>%
  add_trace(y = ~high_2000, name = 'High 2000', line = list(color = 'rgb(205, 12, 24)', width = 1, dash = 'dot')) %>%
  add_trace(y = ~low_2000, name = 'Low 2000', line = list(color = 'rgb(22, 96, 167)', width = 1, dash = 'dot')) %>%
  layout(title = "Average High and Low Temperatures in New York",
         xaxis = list(title = "Months", showgrid = FALSE),
         yaxis = list (title = "Temperature (degrees F)", showgrid = FALSE))

p.ts.3


# Lets emphaise the 2014 values - Second lets adjust the colours of the 6 lines
p.ts.4 <- plot_ly(data, x = ~month, y = ~high_2014, name = 'High 2014', type = 'scatter', mode = 'lines',
                  line = list(color = '#af2346', width = 4)) %>%
  add_trace(y = ~low_2014, name = 'Low 2014', line = list(color = '#3a6587', width = 4)) %>%
  add_trace(y = ~high_2007, name = 'High 2007', line = list(color = '#bc6077', width = 2, dash = 'dot')) %>%
  add_trace(y = ~low_2007, name = 'Low 2007', line = list(color = '#6a9cc4', width = 2, dash = 'dot')) %>%
  add_trace(y = ~high_2000, name = 'High 2000', line = list(color = '#c68d9b', width = 1, dash = 'dot')) %>%
  add_trace(y = ~low_2000, name = 'Low 2000', line = list(color = '#85a5bf', width = 1, dash = 'dot')) %>%
  layout(title = "Average High and Low Temperatures in New York",
         xaxis = list(title = "Months", showgrid = FALSE),
         yaxis = list (title = "Temperature (degrees F)", showgrid = FALSE))

p.ts.4









