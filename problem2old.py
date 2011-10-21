import matplotlib.pyplot as plt
from numpy import arange, linspace, pi, e, sin, cos, sqrt
from math import factorial, fsum # fsum returns the sum of floating point values in the iterable
from grapher import prepare_graph, sigma

## General setup


# e^sin(sqrt(x))
def f(x_value):
    sum = e**sin(sqrt(x_value))
    return sum

# Part A --------------------------------------------------
print "Part A: 100 subintervals"

# Calculate delta Xk, a useful value for definite integrals
Xk = 5.0/100 # (b-a)/n = (5-0)/100
print 'Xk: ' + str(Xk)

# Left-point rule
x_left = arange(0,5,.05) # Array range of 0..4.95 (we don't want 5.00), which is 100 values
print "Left-point rule: " + str(Xk*fsum(f(x_left))) # Left-point rule

print len(x_left)

# Right-point rule
x_right = arange(.05,5.05,.05) # Array range of .05..5.0, which is 100 values
print "Right-point rule: " + str(Xk*fsum(f(x_right))) # Right-point rule

print len(x_right)

# Mid-point rule
x_mid = arange(.025,5,.05) # check this...
print "Mid-point rule: " + str(Xk*fsum(f(x_mid))) # Mid-point rule

print len(x_mid)

# Trapezoidal rule
x_trap = arange(.05,5,.05) # x values .05, .10, .15... 4.95; exclude first and last on purpose
middle_sum = fsum(f(x_trap))
print "Trapezoidal rule: " + str( Xk*sum( (f(0)/2,middle_sum,f(5)/2) )) # check boundary x-values

print len(x_trap)

# Simpson's rule
x_sim2 = arange(.10,5,.10) # x values from .10, .20, .30... 4.80, 4.90, which is for x2, x4, x6...x98
x_sim4 = arange(.05,5.05,.10) # x values .05, .15, .25... 4.85, 4.95, which is x1, x3, x5...x99
print x_sim2
print x_sim4
sum_of_2s = 2*sum(f(x_sim2))
sum_of_4s = 4*sum(f(x_sim4))
print "Simpson's Rule: " + str( Xk/3 * (f(0) + f(5) + sum_of_2s + sum_of_4s) )

# Part B --------------------------------------------------
print "--------------------------------------------------"
print "Part B: 200 subintervals"

# Calculate delta Xk, a useful value for definite integrals
Xk = 5.0/200 # (b-a)/n = (5-0)/200
print 'Xk: ' + str(Xk)

# Left-point rule
x_left = arange(0,5,.025) # Array range of 0..4.95 (we don't want 5.00) by .025, which is 200 values
print "Left-point rule: " + str(Xk*fsum(f(x_left))) # Left-point rule

print len(x_left)

# Right-point rule
x_right = arange(.025,5.025,.025) # Array range of .05..5.0 by .025, which is 200 values
print "Right-point rule: " + str(Xk*fsum(f(x_right))) # Right-point rule

print len(x_right)

# Mid-point rule
x_mid = arange(.0125,5,.025)
print "Mid-point rule: " + str(Xk*fsum(f(x_mid))) # Mid-point rule

print len(x_mid)

# Trapezoidal rule
x_trap = arange(.025,5,.025) # x values from .025 to 5-.025; exclude first and last on purpose
middle_sum = fsum(f(x_trap))
print "Trapezoidal rule: " + str( Xk*sum( (f(0)/2,middle_sum,f(5)/2) ))

print len(x_trap)

# Simpson's rule
x_sim2 = arange(.05,5,.05) # x values from .10 to 4.90, which is for x2, x4, x6...x198
x_sim4 = arange(.025,5,.05) # x values from .05 to 4.95, which is x1, x3, x5...x199
print len(x_sim2)
print len(x_sim4)
sum_of_2s = 2*sum(f(x_sim2))
sum_of_4s = 4*sum(f(x_sim4))
print "Simpson's Rule: " + str( Xk/3 * (f(0) + f(5) + sum_of_2s + sum_of_4s) )

# All this is good!!