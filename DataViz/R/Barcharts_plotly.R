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
titanic.df <- read.csv(file="train.csv", header=TRUE, sep=",")

# What is the mean and median age
mean(titanic.df$Age, na.rm=TRUE) 29.699
median(titanic.df$Age, na.rm=TRUE) 28

# replace all Age NA values with the median value
titanic.df$Age[is.na(titanic.df$Age)] <- 28

# Subset Fare by classtype
first.class.fare <- subset(titanic.df, Pclass == 1, 
                  select=c(Fare, Pclass))
second.class.fare <- subset(titanic.df, Pclass == 2, 
                           select=c(Fare, Pclass))
third.class.fare <- subset(titanic.df, Pclass == 3, 
                            select=c(Fare, Pclass))

# Plot average fare by class

p <- plot_ly(first.class.fare, x = ~first.class.fare$Pclass, y = ~mean(first.class.fare$Fare), type = 'bar')  %>%
     add_trace(second.class.fare, x = ~second.class.fare$Pclass, y = ~mean(second.class.fare$Fare), type = 'bar')  %>%
     add_trace(third.class.fare, x = ~third.class.fare$Pclass, y = ~mean(third.class.fare$Fare), type = 'bar')  %>%
              layout(title = "Average Titanic Fare by Class",
                xaxis = list(title = "Class Type"),
                yaxis = list(title = "Fare Price (in Pounds)"))
p

# Spot the problems with the chart
# 1. Remove chart junk (Remove horizonal grid lines)
# 2. Using pre-attentative attributes lets adjust the colour of 2nd and 3rd class fare

# 3. Lets change the colour of the legend test and employ Gestalt association
# 4. X axis line is black, lets adjust the colour to dark grey
# 5. Gap between colums is too large, lets reduce the gap
# 6. Lets adjust the class names to a more meaningful name (e.g. First, Second and Third)

# 1. Remove chart junk (Remove horizonal grid lines)
p1 <- plot_ly(first.class.fare, x = ~first.class.fare$Pclass, y = ~mean(first.class.fare$Fare), type = 'bar',
              name = '1st Class')  %>%
  add_trace(second.class.fare, x = ~second.class.fare$Pclass, y = ~mean(second.class.fare$Fare), type = 'bar',
            name = '2nd Class')  %>%
  add_trace(third.class.fare, x = ~third.class.fare$Pclass, y = ~mean(third.class.fare$Fare), type = 'bar',
            name = '3rd Class')  %>%
  layout(title = "Average Titanic Fare by Class",
         xaxis = list(title = "Class Type"),
         yaxis = list(title = "Average Fare Price (in Pounds)", showgrid = FALSE))
p1

# 2. Using pre-attentative attributes lets adjust the colour of 2nd and 3rd class fare
p2 <- plot_ly(first.class.fare, x = ~first.class.fare$Pclass, y = ~mean(first.class.fare$Fare), 
              type = 'bar', marker = list(color = 'rgba(58, 101, 135,1)'),
              name = '1st Class')  %>%
  add_trace(second.class.fare, x = ~second.class.fare$Pclass, y = ~mean(second.class.fare$Fare), 
            type = 'bar', marker = list(color = 'rgba(174, 179, 183,1'),
            name = '2nd Class')  %>%
  add_trace(third.class.fare, x = ~third.class.fare$Pclass, y = ~mean(third.class.fare$Fare), 
            type = 'bar', marker = list(color = 'rgba(174, 179, 183,1'),
            name = '3rd Class')  %>%
  layout(title = "Average Titanic Fare by Class",
         xaxis = list(title = "Class Type"),
         yaxis = list(title = "Fare Price (in Pounds)", 
                      showgrid = FALSE))
p2








