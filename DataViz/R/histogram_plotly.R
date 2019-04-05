
library(plotly)


###############Set working Direcgtory##################################
setwd("/Users/jonathandunne/Dropbox/Data_Viz_101/Chart_Workshop")
getwd()

###############Read Data from csv ##################################
iat.df <- read.csv(file="iat.dat", header=TRUE, sep=",")

colnames(iat.df ) <- c("iat_time")


head(iat.df, 5)

sapply(iat.df, class)


# Vanilla Histogram
p1.hist <- plot_ly(x = ~iat.df$iat_time, type = "histogram")
p1.hist


# Added Axis Labels and Title
p2.hist <- plot_ly(x = ~iat.df$iat_time, type = "histogram",
              marker = list(color = '#3a6587')) %>%
              layout(title = "Histogram of Inter-arrival times",
              xaxis = list(title = "Inter-arrival time", showgrid = FALSE),
              yaxis = list(title = "Frequency", showgrid = FALSE))

p2.hist




