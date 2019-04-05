
library(plotly)


###############Set working Direcgtory##################################
setwd("/Users/jonathandunne/Dropbox/Data_Viz_101/Chart_Workshop")
getwd()

###############Read Data from csv ##################################
school.a <- c(63,61,63,62,46,58,60,62,63,63,60,60,61,68,64)
school.b <- c(53, 55, 50, 51, 53, 56, 51, 53, 54, 52, 56, 56, 58, 56, 54)
school.c <- c(45,48,49, 64, 66, 67, 67, 72, 49, 51, 67, 45, 64, 64, 65)

# Vanilla Histogram
p1.box <- plot_ly(type = "box")  %>%
  add_boxplot(y = school.a) %>%
  add_boxplot(y = school.b) %>%
  add_boxplot(y = school.c)
p1.box
  
  
# Added Axis Labels and Title and clear gridlines
p2.box <- plot_ly(type = "box")  %>%
  add_boxplot(y = school.a) %>%
  add_boxplot(y = school.b) %>%
  add_boxplot(y = school.c) %>%
  layout(title = "Box plot of Aggregate Exam Grades by University",
         xaxis = list(title = "School Name", showgrid = FALSE),
         yaxis = list(title = "Exam Grade", showgrid = FALSE))

p2.box



# Add Legend
p3.box <- plot_ly(type = "box")  %>%
  add_boxplot(y = school.a,
              name = "Maynooth") %>%
  add_boxplot(y = ~school.b, 
            name = 'UCC') %>%
  add_boxplot(y = ~school.c,
            name = 'Trinity') %>%
  layout(title = "Box plot of Aggregate Exam Grades by University",
         xaxis = list(title = "School Name", showgrid = FALSE),
         yaxis = list(title = "Exam Grade", showgrid = FALSE))

p3.box

# Change Colours
p4.box <- plot_ly (type = "box") %>%
  add_boxplot(y = school.a,
              marker = list(color = '#3a6587'),
              line = list(color = '#3a6587'),
              name = "Maynooth") %>%
  add_boxplot(y = school.b,
              marker = list(color = '#aeb3b7'),
              line = list(color = '#aeb3b7'),
              name = "UCC") %>% 
  add_boxplot(y = school.c,
              marker = list(color = '#e5a639'),
              line = list(color = '#e5a639'),
              name = "Trinity") %>%  
  layout(title = "Box plot of Aggregate Exam Grades by University",
         xaxis = list(title = "School Name", showgrid = FALSE),
         yaxis = list(title = "Exam Grade", showgrid = FALSE))

p4.box


