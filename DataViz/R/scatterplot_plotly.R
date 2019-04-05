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


###############Set working Direcgtory##################################
setwd("/Users/jonathandunne/Dropbox/Data_Viz_101/Chart_Workshop")
getwd()

###############Read Data from csv ##################################
titanic.sp.df <- read.csv(file="titanic.csv", header=TRUE, sep=",")


# What is the mean and median age
mean(titanic.sp.df$Age, na.rm=TRUE) #29.699
median(titanic.sp.df$Age, na.rm=TRUE) #28

# replace all Age NA values with the median value
titanic.sp.df$Age[is.na(titanic.sp.df$Age)] <- 28


col_scheme <- c("#3a6587", "#aeb3b7")

p.scatter2 <- plot_ly(data = titanic.sp.df, x = ~Fare, y = ~Age,
                     type = 'scatter', mode = 'markers',
                     color = ~Survived, colors = col_scheme) %>%
                     layout(title = "Titanic Passenger Age & Fare by Survial Type",
                     xaxis = list(title = "Fare (In Pounds)", showgrid = FALSE),
                     yaxis = list(title = "Age (In Years)", showgrid = FALSE),
                     legend = l)


p.scatter2


p.scatter3 <- plot_ly(data = titanic.sp.df, x = ~Fare, y = ~Age,
                      type = 'scatter', mode = 'markers',
                      color = ~factor(Survived), colors = col_scheme) %>%
  layout(title = "Titanic Passenger Age & Fare by Survial Type",
         xaxis = list(title = "Fare (In Pounds)", showgrid = FALSE),
         yaxis = list(title = "Age (In Years)", showgrid = FALSE),
         legend = l)


p.scatter3

#Replace Survived 1 and 0 with TRUE and FALSE to make the
# Legend more legible

titanic.sp.df$Survived [titanic.sp.df$Survived == 1] <- "Survived"
titanic.sp.df$Survived [titanic.sp.df$Survived == 0] <- "Died"


p.scatter4 <- plot_ly(data = titanic.sp.df, x = ~Fare, y = ~Age,
                      type = 'scatter', mode = 'markers',
                      color = ~factor(Survived), colors = col_scheme) %>%
  layout(title = "Titanic Passenger Age & Fare by Survial Type",
         xaxis = list(title = "Fare (In Pounds)", showgrid = FALSE),
         yaxis = list(title = "Age (In Years)", showgrid = FALSE))


p.scatter4


titanic.sp.df$Fare

