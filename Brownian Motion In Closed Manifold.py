#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  28 13:53:43 2151

@author: mario
"""


# import two packages
import numpy as np                # for linear algebra and random numbers
import matplotlib.pyplot as plt   # for plotting graphics


# define variables
N = 64                                  # size of array
mi = 100                              # maximum number of temporal iterations
nw = 100                               # number of random walkers

grid = np.zeros([N+2, N+2], dtype = 'int')  # lattice array
grid = grid.transpose((1, 0))
x = np.zeros(nw, dtype = 'int')             # walker x-coordinate in nodal unit
y = np.zeros(nw, dtype = 'int')             # walker y-coordinate in nodal unit

x_step = np.array([-1, 0, 1, 0])        # template arrays for random walk
y_step = np.array([0, -1, 0, 1])        # you might find them uself 
            

# Simulate a flock of random walkers in a closed (compact and unbounded) world
#
# use a definite loop to assign random coordinates to all walkers
#  and place the walkers on the grid
#  use np.random.randint() to generate random integers
#   
# repeat for mi iterations the following 
#   for each walker do the following
#     move the walker one cell in a random direction 
#     (use np.random.choice to generate random direction)
#     you will need to update both grid and the coordinate vectors x, y 
#     DIFFICULT: implement periodic boundary conditions
#     if you give up, you may simply glue walkers to the boundaries as in hw2 
#   print the iteration number
#   plot the grid 
#
# WRITE YOUR CODE HEREINAFTER

# set walkers randomly on the grid
for i in range(nw):
  (x[i], y[i]) = np.random.randint(1,N,2) #two random integers from 1 to N
  grid [x[i], y[i]] = 1

#iterations of brownian motion
for j in range(1, mi):
    #set coordinates for each walker in each iteration
  for i in range(nw):
    #clear the grid  
    grid [x[i], y[i]] = 0
    #update coordinates with random steps + take module
    #to prevent the  walker from stepping out from the grid
    (x[i], y[i]) = ((x[i], y[i]) + np.random.choice(x_step, 2) + (N, N)) % (N, N)
    grid [x[i], y[i]] = 1
    
  
  print (j, 'iteration')
  plt.imshow(grid, origin="lower") 
  plt.show()

# END OF YOUR CODE