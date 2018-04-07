# Slope-Fields

This repository contains files with code in Python that one can run in order to represent
slope fields corresponding to differential equations. The differential equations are 

1)y'=y-3
2)y'=y(y-3)
3)y'=x/x

You can simply modify the code in this repository to draw direction fields of your preference. 
The  idea to think of a differential equation, for example y'=y(y-3) as a system of differential 
equations on (t,y) by simply putting

t'=1
y'=y(y-3)

So that we are now considering the integral curves or flow lines of the vector field (1,y(y-3)) in the plane. 
In order to plot the direction fields of a given differential equation, for example

y'=xy+y^2 

(which is not considered in the above examples), go to the code in the file y(y-3).py and look at lines 12-13 and 30-31 
and note that these are the lines where you have to input the vector field corresponding differential equation. 
Note also that we are using x[0] to represent the variable t and x[1] to represent y. For example, in order to plot 
the slope fields corresponding to y'=xy+y^2, 


