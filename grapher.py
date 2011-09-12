# A module is a python file that (generally) has only definitions of variables, functions, and classes.
# This module is to help with graphing.

## Define some variables:
x = 1

## Functions:

# Prepares the graph with the given matplotlib.axes.AxesSubplot object
# Calls actions that directly impact the passed in variable!
def prepare_graph(ax):
    # Setting colors - top and right are by default black, which doesn't look good
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_color('none')
    ax.spines['left'].set_color('none')

    # Possibly useful...
    ax.spines['left'].set_smart_bounds(True)
    ax.spines['bottom'].set_smart_bounds(True)

    # Setting position of spines (the ticks and number labels)
    # Commenting this lets the axes labels appear
    # ax.spines['left'].set_position('zero')
    # ax.spines['bottom'].set_position('zero')

    # Place ticks along axes
    ax.xaxis.set_ticks_position('bottom') # prevents ticks from being at top
    ax.yaxis.set_ticks_position('left') # prevents ticks from being at right

    # Setting x and y axes properties
    ax.axhline(linewidth=2, color='black')
    ax.axvline(linewidth=2, color='black')

## UNUSED CODE BELOW

# Calculates the result of a function applied to each
# value in an array. Returns the sum of all such calculations.
def sigma(start,end,x_values,fn):
    if start > end: return 0
    else: 
        sum = 0
        
        return sigma(start+1,end,x)
 
## Define a class
# class Piano:
    # def __init__(self):
    #     self.type = raw_input("What type of piano? ")
    #     self.height = raw_input("What height (in feet)? ")
    #     self.price = raw_input("How much did it cost? ")
    #     self.age = raw_input("How old is it (in years)? ")
    #   
    # def printdetails(self):
    #     print "This piano is a/an " + self.height + " foot",
    #     print self.type, "piano, " + self.age, "years old and costing\
    # " + self.price + " dollars."