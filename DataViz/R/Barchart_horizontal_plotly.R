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
titanic.h.df <- read.csv(file="titanic.csv", header=TRUE, sep=",")

# What is the mean and median age
mean(titanic.h.df$Age, na.rm=TRUE) #29.699
median(titanic.h.df$Age, na.rm=TRUE) #28

# replace all Age NA values with the median value
titanic.h.df$Age[is.na(titanic.h.df$Age)] <- 28

head(titanic.h.df, 5)

# Subset Age by embarkation point
cherbourg.age <- subset(titanic.h.df, Embarked == "Cherbourg", 
                           select=c(Age, Embarked))
queenstown.age <- subset(titanic.h.df, Embarked == "Queenstown (Cobh)", 
                            select=c(Age, Embarked))
southampton.age <- subset(titanic.h.df, Embarked == "Southampton", 
                           select=c(Age, Embarked))


#Calculate the means 
mean(cherbourg.age$Age) #30.1781
mean(queenstown.age$Age) #28.03247
mean(southampton.age$Age) #29.2434


p.bar.h1 <- plot_ly(cherbourg.age, x = ~mean(cherbourg.age$Age), y = ~cherbourg.age$Embarked, type = 'bar')  %>%
  add_trace(queenstown.age, x = ~mean(queenstown.age$Age), y = ~queenstown.age$Embarked, type = 'bar')  %>%
  add_trace(southampton.age, x = ~mean(southampton.age$Age), y = ~southampton.age$Embarked, type = 'bar')  %>%
  layout(title = "Titanic Passenger Average Age by Departure Location",
         xaxis = list(title = "Age (In Years)"),
         yaxis = list(title = "Departure Location"))
p.bar.h1


p.bar.h2 <- plot_ly(cherbourg.age, x = ~mean(cherbourg.age$Age), y = ~cherbourg.age$Embarked, type = 'bar')  %>%
  add_trace(queenstown.age, x = ~mean(queenstown.age$Age), y = ~queenstown.age$Embarked, type = 'bar')  %>%
  add_trace(southampton.age, x = ~mean(southampton.age$Age), y = ~southampton.age$Embarked, type = 'bar')  %>%
  layout(title = "Titanic Passenger Average Age by Departure Location",
         xaxis = list(title = "Age (In Years)", showgrid = FALSE),
         yaxis = list(title = "Departure Location", showgrid = FALSE))
p.bar.h2



p.bar.h3 <- plot_ly(cherbourg.age, x = ~mean(cherbourg.age$Age), y = ~cherbourg.age$Embarked, 
                    type = 'bar',
                    marker = list(color = 'rgba(174, 179, 183,1)'),
                    name = 'Cherbourg')  %>%
  add_trace(queenstown.age, x = ~mean(queenstown.age$Age), y = ~queenstown.age$Embarked, 
            type = 'bar', 
            marker = list(color = 'rgba(58, 101, 135,1)'),
            name = 'Queenstown(Cobh)')  %>%
  add_trace(southampton.age, x = ~mean(southampton.age$Age), y = ~southampton.age$Embarked, 
            type = 'bar',
            marker = list(color = 'rgba(174, 179, 183,1)'),
            name = 'Southampton') %>%
  layout(title = "Titanic Passenger Average Age by Departure Location",
         xaxis = list(title = "Age (In Years)", showgrid = FALSE),
         yaxis = list(title = "Departure Location", showgrid = FALSE))
p.bar.h3

