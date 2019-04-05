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
library(r2d3)

###############Set working Direcgtory##################################
setwd("/Users/jonathandunne/Dropbox/Data_Viz_101/Chart_Workshop/R/01 Barcharts")
getwd()

###############Read Data from csv ##################################
titanic.df <- read.csv(file="train.csv", header=TRUE, sep=",")


r2d3(data = read.csv("flare.csv"), d3_version = 4, script = "bubbles.js")