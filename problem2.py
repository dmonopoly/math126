# Import basic math tools
# fsum returns the sum of floating point values in the iterable;
# sum is the same, but fsum adds floating point values with extended precision
from numpy import arange, linspace, pi, e, sin, cos, sqrt
from math import factorial, fsum 

# f(x) = e^sin(sqrt(x))
def f(x_value):
    sum = e**sin(sqrt(x_value))
    return sum

# Left-point Rule
def LRAM(a,b,n):
    Xk = (float) (b-a)/n
    x = arange(a, b, Xk) # returns an array range from [a,b) with Xk intervals
    return Xk*fsum(f(x))

# Right-point Rule
def RRAM(a,b,n):
    Xk = (float) (b-a)/n
    x = arange(a+Xk, b+Xk, Xk)
    return Xk*fsum(f(x))

# Midpoint Rule
def MRAM(a,b,n):
    Xk = (float) (b-a)/n
    x = arange( (a+Xk)/2, b, Xk)
    return Xk*fsum(f(x))

# Trapezoidal Rule
def trap(a,b,n):
    Xk = (float) (b-a)/n
    x = arange(a+Xk, b, Xk) # excludes first and last values, which we /2 later
    middle_sum = fsum(f(x))
    return Xk*fsum( (f(a)/2,middle_sum,f(b)/2) )

# Simpson's Rule
def simpsons(a,b,n):
    Xk = (float) (b-a)/n
    x2 = arange(a+2*Xk, b-Xk, 2*Xk) # 3rd, 5th, 7th... (n-2)th x values
    x4 = arange(a+Xk, b, 2*Xk) # 2nd, 4th, 6th... (n-1)th x values
    sum_of_2s = 2*fsum(f(x2))
    sum_of_4s = 4*fsum(f(x4))
    return Xk/3*(f(a) + sum_of_2s + sum_of_4s + f(b))
    
print "--------------------------------------------------"
print "| Part A: 100 subintervals"
print "--------------------------------------------------"

# Left-point rule
print "Left-point rule: " + str(LRAM(0,5,100))

# Right-point rule
print "Right-point rule: " + str(RRAM(0,5,100))

# Midpoint rule
print "Midpoint rule: " + str(MRAM(0,5,100))

# Trapezoidal rule
print "Trapezoidal rule: " + str(trap(0,5,100))

# Simpson's rule
print "Simpson's Rule: " + str(simpsons(0,5,100))

print "--------------------------------------------------"
print "| Part B: 200 subintervals"
print "--------------------------------------------------"

# Left-point rule
print "Left-point rule: " + str(LRAM(0,5,200))

# Right-point rule
print "Right-point rule: " + str(RRAM(0,5,200))

# Midpoint rule
print "Midpoint rule: " + str(MRAM(0,5,200))

# Trapezoidal rule
print "Trapezoidal rule: " + str(trap(0,5,200))

# Simpson's rule
print "Simpson's Rule: " + str(simpsons(0,5,200))

print "--------------------------------------------------"
print "| Part B: 400 subintervals"
print "--------------------------------------------------"

# Left-point rule
print "Left-point rule: " + str(LRAM(0,5,400))

# Right-point rule
print "Right-point rule: " + str(RRAM(0,5,400))

# Midpoint rule
print "Midpoint rule: " + str(MRAM(0,5,400))

# Trapezoidal rule
print "Trapezoidal rule: " + str(trap(0,5,400))

# Simpson's rule
print "Simpson's Rule: " + str(simpsons(0,5,400))