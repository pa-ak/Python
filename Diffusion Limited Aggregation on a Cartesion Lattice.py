# DIFFUSION LIMITED AGGREGATION ON A CARTESION LATTICE 
import numpy as np
import matplotlib.pyplot as plt
#------------------------------------------
N  = 128
mi = 10000                                    # maximum number of temporal iterations
nw = 1000                                      # number of random walkers
#------------------------------------------
x_step = np.array([-1, 0, 1, 0])               # template arrays for random walk
y_step = np.array([0, -1, 0, 1])  
grid   = np.zeros([N+2, N+2], dtype = 'int')   # lattice array
grid   = grid.transpose((1, 0))
x      = np.zeros(nw, dtype = 'int')           # walker x-coordinate in nodal unit
y      = np.zeros(nw, dtype = 'int')           # walker y-coordinate in nodal unit
status = np.ones(nw, dtype = 'int')            # walker status array: all mobile

nix    = np.array([-1, 0, 1, 0,-1, 1, 1,-1])    # arrays containing 
niy    = np.array([ 0,-1, 0, 1,-1,-1, 1, 1])    # all neighbors indices


# hw4: Diffusion-limited aggregation (DLA)
#  write an algorithm that simulates DLA. DLA is the physical process whereby
#   random walkers  (particles udner Brownian motion) stick to each other or to
#   an aggregation nucleus (nucleation site). As a result, fractal clusters are 
#   formed.this or similar processes underlie the formation of snowflakes, 
#   Browninan trees, Lichtenberg figures, and in general any cluster formed by 
#   aggregation of random walkers.
#
# first, we set one nucleation site in the center 
#  this is the site to which walkers stick
grid[N//2, N//2] = 2                    # 2: make central node sticky (2)
# remember that in the grid, 0 denotes empty cell, and 1 denotes walker in cell
#  now, 2 will denote sticky cell
#
# then, create two nested loops (for or while, as you like):
#   one for mi temporal iterations and 
#   another (nested inside) for the nw random walkers
#  and repeat hw3 (simulate a cloud of random walkers in a closed universe)
#  using the new grid size N  
# the loops should stop either when no more mobile walkers are left, or
#  when the maximum number of iterations (mi) is reached 
#
# you can initialize the random walkers positions with this code (as in hw3)
for i in range(nw):
    x[i] = np.random.randint(0, N-1)
    y[i] = np.random.randint(0, N-1)
   
    #I'd better check if someone is glued from the very begining. to prevent overwriting of central glued point
    if (x[i], y[i]) == (N//2, N//2): 
      status[i] == 0
    else:
      grid[x[i], y[i]] = 1
# 
# next, the actual hw4 
#  we will simulate aggregation to the nucleation site (center: N/2, N/2)  
#   for this, remember to use the walker status array by denoting walkers as 
#   0: glued (stuck) walker
#   1: mobile walker
# 
# now the heart of the DLA process: 
#  for every temporal iteration, and
#  for every walker in the walker loop,
#   (after implementing the random walker motion as in hw3)
#   check whether any of its neighbor grid cells is sticky: you can 
#    do this by checking all eight neighboring grid cells (2)
#    the arrays in lines 17-18 might be handy for this purporse
#   if any of the current walker neighbor cells is sticky, 
#    glue the walker and make its grid cell sticky
#   otherwise, check the next walker
#  this simulates the  aggregation of particles
#
#  at the end of every loop over the walkers, 
#   print the temporal iteration number and number of glued walkers
#   and plot the grid
# 
#
# WRITE YOUR CODE HEREINAFTER

#iterations of random motion
for j in range(mi):
    #set coordinates for a moving walker in each iteration
  for i in range(nw):
    if status[i]:
      #clear the grid position
      grid[x[i], y[i]] = 0

       #update coordinates with random steps + take module
       #to prevent the  walker from stepping out from the grid
      x[i] = (x[i] + np.random.choice([0,1,-1]) + N) % N
      y[i] = (y[i] + np.random.choice([0,1,-1]) + N) % N
      grid[x[i], y[i]] = 1

      #Check the glued neighbors
      for i_nix in range(len(nix)):
        if grid [x[i] + nix[i_nix], y[i] + niy[i_nix]] == 2:
          grid  [x[i], y[i]] = 2  
          status[i] = 0
          break     #stopz
  
  #just for the convenience let plot the grid not at each iteration but once in 100 iterations + the last one  
  if (j % 100) == 0:
      print ( j, "iteration", " glued:", (nw - sum(status)))
      plt.imshow (grid, origin="lower") 
      plt.show()
  elif (nw - sum(status)) == 1000:
      print ( j, "iteration", " glued:", (nw - sum(status)))
      plt.imshow (grid, origin="lower") 
      plt.show()
  elif j == 9999:
      print ( j, "iteration", " glued:", (nw - sum(status)))
      plt.imshow (grid, origin="lower") 
      plt.show()
    
  if (sum(status)==0):
      break
   

# END OF YOUR CODE

    

