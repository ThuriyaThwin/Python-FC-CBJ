# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 13:30:31 2016

@author: 3200234
"""

import classes as cl
import gestDict as dic
import gestIO as io
import error_tools as err
from copy import deepcopy
import time

dic.recupDictionnaire()

# grid = io.read_file("grille1.txt")[0]
# solver = cl.Solver(grid, dic.DICTIONNAIRE)
# print solver.ac3()

grid = io.read_file("grille1.txt")[0]
print grid
solver = cl.Solver(grid, dic.DICTIONNAIRE, random=False)
solver.ac3()

# start = time.time()
# instance = solver.conflictBackJumping(deepcopy(solver.variables), {})
# print time.time() - start

# print instance
# grid.fillGrid(instance)

start = time.time()
instance = solver.forwardChecking(first=True)
print time.time() - start

print instance
grid.fillGrid(instance)
