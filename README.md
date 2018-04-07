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
the slope fields corresponding to y'=xy+y^2 replace lines 12 and 13 with

dx[0]=1
dx[1]=x[0]*x[1]+x[1]**2

and lines 30-31 with
U=1
V=X*Y+Y**2

Also, the colored curves correspond to plots of solutions obtained by using a numerical integrator. If you don't obtain a plot for these colored curves that you think it is adequate, then just adjust the parameters in lines 17-18

Note also that the file contains a header with a number of libraries that are being used. If you are new to Python and have never worked with these libraries, you will have to install them. For example, if you want to install "numpy", you can use the terminal command line and first call pip by writing the following instructions (all of this once you are using python)

python3.6 (call python, the number 3.6 is the version of python that you have installed)
>>>import pip
>>>pip
>>>pip.main('install','numpy')

In this way you will have installed numpy (do the same for the other libraries). Please let me know if you have any questions 
or issues with the code in this repository.




