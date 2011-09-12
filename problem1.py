import matplotlib.pyplot as plt
from numpy import arange, linspace, pi, e, sin
from math import factorial
from grapher import prepare_graph, sigma

## General setup
# plt.ylabel('y-axis')
# plt.xlabel('x-axis')

# This is the function "sigma from k=1 to 10 of sin( (k!)^2*x ) / k!"
def f(x_value):
    array = arange(1,11,1) # Array range of 1..10
    sum = 0
    for k in array:
        sum += sin(factorial(k)**2*x_value) / factorial(k)
    return sum

## Setting up x & y
# 1. x E [0,1]
x1 = linspace(0,1.,100) # 100 x-values from [0,1]
y1 = f(x1)

# 2. x E [0,0.1]
x2 = linspace(0,.1,100) # 100 x-values from [0,0.1]
y2 = f(x2)

# 3. x E [0,0.01]
x3 = linspace(0,.01,100) # 100 x-values from [0,0.01]
y3 = f(x3)

# 4. x E [0,0.001]
x4 = linspace(0,.001,100) # 100 x-values from [0,0.001]
y4 = f(x4)

## Preparing the figure for all plots
fig = plt.figure()
fig.subplots_adjust(hspace=.4) # add space vertically between subplots
fig.subplots_adjust(wspace=.4) # add space horizontally between subplots

# Create subplots
ax1 = plt.subplot(221)
ax2 = plt.subplot(222)
ax3 = plt.subplot(223)
ax4 = plt.subplot(224)
axs = [ ax1, ax2, ax3, ax4 ]

# Set labels for axes
y_label = 'y-axis'
x_label = 'x-axis'

for ax in axs:
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

# Set titles
ax1.set_title('Graph over [0,1]')
ax2.set_title('Graph over [0,0.1]')
ax3.set_title('Graph over [0,0.01]')
ax4.set_title('Graph over [0,0.001]')

# Plot graphs in various subplots
ax1.plot(x1,y1)
ax2.plot(x2,y2)
ax3.plot(x3,y3)
ax4.plot(x4,y4)

# Prepare axes
for ax in axs:
    prepare_graph(ax)

plt.show() # Shows the graph