#The following code shows how the Python numpy and scipy libraries
#can be used to solve a differential equation using the odeint command.
#This is an effective tool for solving ordinary differential equations.
#The example in this case a differential equation for a damped harmonic oscillator.








#Numeric Python library
import numpy as np



# Plotting library Pyplot from matplot lib
import matplotlib.pyplot as plt



#Bring in the odeint module from the scipy library.
#This is an integration tool for ordinary differential equations.
from scipy.integrate import odeint








#Define the function that describes the differential equation
#of a damped harmonic oscillator.  Inputs include the initial conditions,
#horizontal axis (usually time or x) and equation parameters or constants.
def myModel(init, t, params):


    #Unpack the current values of y as initial values.
    y_init, y_dot_init, y_doubledot_init = init


    #Parameters for the differential equation.
    a,b = params


    #Write out the differential equation in the function.  Need to write out the equations
    #with the initial conditions.  For Python's ODE solver to work, you need to write out
    #a system of differential equations as a first order system.
    #To do this, write out all the initial conditions in terms of the derivative of
    #the dependent variable.
    #However, for the highest order derivative, write it out in terms of the equation
    #to be solved.
    y_prime = y_dot_init
    y_doubleprime = y_doubledot_init
    y_tripleprime = b*t - a*y_prime



    #Return the differential equation.  The ode solver will integrate this entire system up one level.
    #In this case, the solver will provide the solutions of y, y' and y''.
    return y_prime, y_doubleprime, y_tripleprime








#Parameters to be used for the differential equation.
a = 4.0
b = 1.0



#Bundle the parameters into a list for the ODE solver.
#Can also bundle initial conditions into a list for the ODE solver
#if there is more than one initial condition needed.
params = [a,b]



#Time range needed for the function.
t = np.linspace(0, 10, 1000)



#Initial values.  The initial values need to match the type of quantity that is being solved
#for by the ode solver.  In this, an inital value of displacement and velocity are provided.
init = [0, 0, 1]



#Solve the differential equation using the odeint function, with a function
#call to the myModel function.  The parameters can be passed into the solver
#as a tuple.  Note that to define a tuple, normal brackets need to be used
#and a comma is required after the parameter list.  Tuples are immutable
#and cannot be changed, unlike lists.  Lists uses square brackets.
#The ode solver basically integrates whatever is put into it with the equation model function.
#It can do more than one integration at the same time, depending on what the function returns.
state = odeint(myModel, init, t, args = (params,))








#Open up a figure for plotting the solution to the equation of displacement vs. time.
plt.figure(1)



#Plot the solution to the differential equation.  In this case, the first column of the solution is plotted,
#which is displacement, versus time.
plt.plot(t, state[:,0], '-', lw = 2)



#Label the x axis.
plt.xlabel('Time(s)')



#Label the y axis
plt.ylabel('Position(cm)')



#Title of the plot
plt.title('ODE solver Solution: Displacement')



#Show the plot
plt.show()









#Open up a figure for plotting displacement vs. velocity.
plt.figure(2)



#Plot the solution to the differential equation.  In this case, the second column is plotted with
#respect to time, which is velocity vs. time.
plt.plot(t, state[:,1], '-', lw = 2)


#Label the x axis.
plt.xlabel('Time(s)')



#Label the y axis
plt.ylabel('Velocity(cm/s)')



#Title of the plot
plt.title('ODE solver Solution: Velocity')



#Show the plot
plt.show()








#Open up a figure for plotting displacement vs. velocity.
plt.figure(3)



#Plot the solution to the differential equation.  In this case, the third column is plotted with respect
#to time, which is
plt.plot(t, state[:,2], '-', lw = 2)



#Label the x axis.
plt.xlabel('Time(s)')



#Label the y axis
plt.ylabel('Acceleration(cm/s' + r'$^2$' + ')')



#Title of the plot
plt.title('ODE solver Solution: Acceleration')



#Show the plot
plt.show()







#Print out all columns of the solution to the ODE.  This will include displacement, velocity and acceleration.
print(state)