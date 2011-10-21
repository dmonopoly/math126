import matplotlib.pyplot as plt
from numpy import arange, linspace, pi, e, sin, cos, sqrt
from math import factorial, fsum # fsum returns the sum of floating point values in the iterable;
# sum is the same, but fsum adds floating point values with extended precision
from grapher import prepare_graph, sigma

## General setup


# e^sin(sqrt(x))
def f(x_value):
    sum = e**sin(sqrt(x_value))
    return sum

def LRAM(a,b,n):
    Xk = (float) (b-a)/n
    x = arange(a, b, Xk)
    return Xk*fsum(f(x))

def RRAM(a,b,n):
    Xk = (float) (b-a)/n
    x = arange(a+Xk, b+Xk, Xk)
    return Xk*fsum(f(x))

def MRAM(a,b,n):
    Xk = (float) (b-a)/n
    x = arange( (a+Xk)/2, b, Xk)
    return Xk*fsum(f(x))

def trap(a,b,n):
    Xk = (float) (b-a)/n
    x = arange(a+Xk, b, Xk) # excludes first and last values, which we /2 later
    middle_sum = fsum(f(x))
    return Xk*fsum( (f(a)/2,middle_sum,f(b)/2) )

def simpsons(a,b,n):
    Xk = (float) (b-a)/n
    x2 = arange(a+2*Xk, b-Xk, 2*Xk) # 3rd, 5th, 7th... (n-2)th x values
    x4 = arange(a+Xk, b, 2*Xk) # 2nd, 4th, 6th... (n-1)th x values
    print len(x2)
    print len(x4)
    sum_of_2s = 2*fsum(f(x2))
    sum_of_4s = 4*fsum(f(x4))
    return Xk/3*(f(a) + sum_of_2s + sum_of_4s + f(b))
    
# Part A --------------------------------------------------
print "Part A: 100 subintervals"

# Calculate delta Xk, a useful value for definite integrals
Xk = 5.0/100 # (b-a)/n = (5-0)/100
print 'Xk: ' + str(Xk)

# Left-point rule
x_left = arange(0,5,.05) # Array range of 0..4.95 (we don't want 5.00), which is 100 values
print "Left-point rule: " + str(Xk*fsum(f(x_left))) # Left-point rule
print "Left-point rule: " + str(LRAM(0,5,100)) # Left-point rule

# Right-point rule
x_right = arange(.05,5.05,.05) # Array range of .05..5.0, which is 100 values
print "Right-point rule: " + str(Xk*fsum(f(x_right))) # Right-point rule
print "Right-point rule: " + str(RRAM(0,5,100)) # Right-point rule

# Mid-point rule
x_mid = arange(.025,5,.05) # check this...
print "Mid-point rule: " + str(Xk*fsum(f(x_mid))) # Mid-point rule
print "Mid-point rule: " + str(MRAM(0,5,100)) # Mid-point rule

# Trapezoidal rule
x_trap = arange(.05,5,.05) # x values .05, .10, .15... 4.95; exclude first and last on purpose
middle_sum = fsum(f(x_trap))
print "Trapezoidal rule: " + str( Xk*sum( (f(0)/2,middle_sum,f(5)/2) ))
print "Trapezoidal rule: " + str(trap(0,5,100))

# Simpson's rule
x_sim2 = arange(.10,5,.10) # x values from .10, .20, .30... 4.80, 4.90, which is for x2, x4, x6...x98
x_sim4 = arange(.05,5.05,.10) # x values .05, .15, .25... 4.85, 4.95, which is x1, x3, x5...x99
sum_of_2s = 2*sum(f(x_sim2))
sum_of_4s = 4*sum(f(x_sim4))
print "Simpson's Rule: " + str( Xk/3 * (f(0) + f(5) + sum_of_2s + sum_of_4s) )
print "Simpson's Rule: " + str(simpsons(0,5,100))

# Part B --------------------------------------------------
print "--------------------------------------------------"
print "Part B: 200 subintervals"

# Calculate delta Xk, a useful value for definite integrals
Xk = 5.0/200 # (b-a)/n = (5-0)/200
print 'Xk: ' + str(Xk)

# Left-point rule
x_left = arange(0,5,.025) # Array range of 0..4.95 (we don't want 5.00) by .025, which is 200 values
print "Left-point rule: " + str(Xk*fsum(f(x_left))) # Left-point rule
print "Left-point rule: " + str(LRAM(0,5,200)) # Left-point rule

# Right-point rule
x_right = arange(.025,5.025,.025) # Array range of .05..5.0 by .025, which is 200 values
print "Right-point rule: " + str(Xk*fsum(f(x_right))) # Right-point rule
print "Right-point rule: " + str(RRAM(0,5,200)) # Right-point rule

# Mid-point rule
x_mid = arange(.0125,5,.025)
print "Mid-point rule: " + str(Xk*fsum(f(x_mid))) # Mid-point rule
print "Mid-point rule: " + str(MRAM(0,5,200)) # Mid-point rule

# Trapezoidal rule
x_trap = arange(.025,5,.025) # x values from .025 to 5-.025; exclude first and last on purpose
middle_sum = fsum(f(x_trap))
print "Trapezoidal rule: " + str( Xk*sum( (f(0)/2,middle_sum,f(5)/2) ))
print "Trapezoidal rule: " + str(trap(0,5,200))

# Simpson's rule
x_sim2 = arange(.05,5,.05) # x values from .10 to 4.90, which is for x2, x4, x6...x198
x_sim4 = arange(.025,5,.05) # x values from .05 to 4.95, which is x1, x3, x5...x199
sum_of_2s = 2*sum(f(x_sim2))
sum_of_4s = 4*sum(f(x_sim4))
print "Simpson's Rule: " + str( Xk/3 * (f(0) + f(5) + sum_of_2s + sum_of_4s) )
print "Simpson's Rule: " + str(simpsons(0,5,200))

# All this is good!!