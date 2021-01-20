#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 16:49:55 2019

@author: mario
"""

# import two packages
import numpy               # for linear algebra and random numbers
import matplotlib.pyplot   # for plotting graphics


# define variables
N = 10                                          # size of array
grid = numpy.zeros([N+2, N+2], dtype = 'int')   # lattice array
x = 7                                           # x coordinate of creature
y = 3                                           # y coordinate of creature


# ask name (use function input())
#  if input is not a string, display "name should be a string" 
#   you can check if the object type of name is string with  -->  isinstance(name, str) 
#  if the input name is larger than 5 characters, move up, otherwise down
#                                                display "your name is long/short"
# ask age
#  if input is not an int or float, display "name should be a number" 
#   you can check if the object type of age is int with  -->  isinstance(age, int)
#   you can check if the object type of age is float with  -->  isinstance(age, float)
#  if the input age is even, move right, otherwise left
#                           display "your age is even / odd"
#
# WRITE YOUR CODE HEREINAFTER

name = input('What is your name?    ')

while name:
    try:
        float(name)
        print ("Name should be a string!")
        name = input('What is your name?    ')
    except:    
         break

if len(name) >= 6:
    x = x + 1
    print("your name is long")
else:
    x = x - 1
    print("your name is short")



age = (input('Write your age    '))

while age:
    try:
        float(age)
        break
    except:    
        print ("Age should be a number, for god's sake!")
        age = (input('Write your age    '))

age = int(round(float(age)))
if (age % 2) == 0:
    y = y + 1
else:
    y = y - 1       

# END OF YOUR CODE


grid[x, y] = 1                                  # set creature position on grid

# plot grid
matplotlib.pyplot.imshow(grid, origin= "lower") 
matplotlib.pyplot.show()
