# Import basic math tools
# fsum returns the sum of floating point values in the iterable;
# sum is the same, but fsum adds floating point values with extended precision
from numpy import arange, linspace, pi, e, sin, cos, sqrt
from math import factorial, fsum

# f(x) = e^sin(sqrt(x))
def f(x_value):
    y = e**sin(sqrt(x_value))
    return y

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

# Prints an error report for the passed in function by comparing results of n1
# with those of n2 (note: n1 < n2)
# expected_factor is the expected factor that the error should decrease by.
# Function is evaluated from 0 to 5
# Example: error_report_for("MIDPOINT", MRAM, 100, 200, 4, true_value)
def error_report_for(name, fn, n1, n2, expected_factor, true_val):
    # Preliminary calculations
    val1 = fn(0,5,n1) # for n = n1
    val2 = fn(0,5,n2)
    error1 = abs(val1 - true_val) # error for n=n1
    error2 = abs(val2 - true_val)
    
    # Begin printing
    print name + " for n = " + str(n1) + ", n = " + str(n2)
    print
    print "n | Approximation"
    print str(n1) + " | " + str(val1)
    print str(n2) + " | " + str(val2)
    print
    print "Error for " + str(n1) + ": |" + str(val1) + " - True value| = " + str(error1)
    print "Error for " + str(n2) + ": |" + str(val2) + " - True value| = " + str(error2)
    print
    print "If the number of intervals increases by a factor of q = " + str(n2/n1) + ","
    print "the error should decrease by a factor of "+str(expected_factor)
    print "*Actual error decreased by a factor of " + str(error1/error2)
    print

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

print "--------------------------------------------------"
print "| Error Checking"
print "--------------------------------------------------"

true_value = 12.04438250045100240831629426443002559542604900442770316
print "True value: " + str(true_value)
print
error_report_for("LEFT POINT", LRAM, 20, 40, 2, true_value)
error_report_for("RIGHT POINT", RRAM, 20, 40, 2, true_value)
error_report_for("MIDPOINT", MRAM, 20, 40, 4, true_value)
error_report_for("TRAPEZOIDAL", trap, 20, 40, 4, true_value)
error_report_for("SIMPSONS", simpsons, 20, 40, 16, true_value)