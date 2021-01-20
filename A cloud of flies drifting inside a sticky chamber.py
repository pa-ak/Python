#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 16:33:43 2019

@author: mario
"""


# import two packages
import numpy as np                # for linear algebra and random numbers
import matplotlib.pyplot as plt   # for plotting graphics


# define variables
nw = 4                                       # number of walkers
N = 10                                       # size of array
grid = np.zeros([N+2, N+2], dtype = 'int')   # lattice array
grid = grid.transpose((1, 0))
x = np.zeros(nw, dtype = 'int')              # walker x-coordinate in nodal unit
y = np.zeros(nw, dtype = 'int')              # walker y-coordinate in nodal unit
status = np.ones(nw, dtype = 'int')          # walker status array: all mobile (1)
                      
# set walkers coordinates
x[0] = 7
y[0] = 5         
x[1] = 3
y[1] = 2 
x[2] = 4
y[2] = 8 
x[3] = 9
y[3] = 2 

# sets walker positions on grid
#grid[x[0], y[0]] = 1 
#grid[x[1], y[1]] = 1
#grid[x[2], y[2]] = 1
#grid[x[3], y[3]] = 1


# Part 1
# write a function "setwalkers()" which takes as arguments a grid and two 
#  coordinate vectors x and y of the same length equal to the number of walkers
#  it should place all walkers on the grid by looping through the vectors.
#  Effectively, it should do the same as lines 34-37, and output the new grid. 

# Part 2
# ask and store bearing though console: north, east, south, or west
# using indefinite loop, move all the walkers in the input direction 
# after moving a walker, set its status to glued (status=0)
#   if one of its coordinates is 0 or 11 
# stop loop when no mobile walkers remain

# WRITE YOUR CODE HEREINAFTER

#place all walkers on the grid
def setwalkers(grid, x, y):
    grid[:] = 0 
    for i in range(len(x)):
        grid[x[i], y[i]] = 1
    return grid

setwalkers(grid,x,y)

#console for directions setting
direction = input("Where to move? Press: 'n' for North; 's' for South; 'e' for East; 'w' for West       ")

while direction not in ['North', 'north', 'n', 'N', 'South', 'south', 's', 'S', 'East', 'east', 'e', 'E', 'West', 'west', 'w', 'W']:
    direction = input("Wrong input. Try once again. Where to move?\ Press: 'n' for North; 's' for South; 'e' for East; 'w' for West       ")

d = direction[0]
d = d.lower()
dx = {'n':1, 's':-1}.get(d,0)
dy = {'e':1, 'w':-1}.get(d,0)


#moving walkers
while np.count_nonzero(status):
    for i in range(len(x)):
        if status[i] == 1:
            #clear the grid
            grid[x[i],y[i]] = 0
            #update coordinates
            x[i] += dx
            y[i] += dy
            #set walker to a new position
            grid[x[i], y[i]] = 1
            #update walker's status 
            if ((x[i] in [0, N+1]) or (y[i] in [0, N+1])):
                status[i]=0
    plt.imshow(grid, origin="lower") 
    plt.show()
    
    
# END OF YOUR CODE

# plot grid
print("_==FINISHED==_")
plt.imshow(grid, origin="lower") 
plt.show()