
library(plotly)


###############Set working Direcgtory##################################
setwd("/Users/jonathandunne/Dropbox/Data_Viz_101/Chart_Workshop")
getwd()

###############Read Data from csv ##################################
xpts <- c(1.1 ,2,3.3,4,5.5,6,7.7)
ypts <- c(1,2.2 ,3,4.4,5,6.6,7)

fit <- lm(ypts ~ xpts)


p1.slr <- plot_ly(x = ~xpts) %>% 
          add_markers(y = ~ypts) %>% 
          add_lines(x = ~xpts, y = fitted(fit))

p1.slr


# Added Axis Labels and Title and clear gridlines
p2.slr <- plot_ly(x = ~xpts) %>% 
  add_markers(y = ~ypts) %>% 
  add_lines(x = ~xpts, y = fitted(fit)) %>%
  layout(title = "Scatterplot with fitted regression line",
         xaxis = list(title = "Independent Variable", showgrid = FALSE),
         yaxis = list(title = "Dependent Variable", showgrid = FALSE))

p2.slr


# Added Legend
p3.slr <- plot_ly(x = ~xpts) %>% 
  add_markers(y = ~ypts, name = "Observations") %>% 
  add_lines(x = ~xpts, y = fitted(fit), name="Fitted Regression line") %>%
  layout(title = "Scatterplot with fitted regression line",
         xaxis = list(title = "Independent Variable", showgrid = FALSE),
         yaxis = list(title = "Dependent Variable", showgrid = FALSE))

p3.slr


# Adjust Colours
p4.slr <- plot_ly(x = ~xpts) %>% 
  add_markers(y = ~ypts, name = "Observations",
              marker = list(color = '#e5a639', size=10)) %>% 
  add_lines(x = ~xpts, y = fitted(fit), name="Fitted Regression line",
            line = list(color = '#3a6587', dash = 'dot')) %>%
  layout(title = "Scatterplot with fitted regression line",
         xaxis = list(title = "Independent Variable", showgrid = FALSE),
         yaxis = list(title = "Dependent Variable", showgrid = FALSE))

p4.slr