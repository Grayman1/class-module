#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 20:02:06 2018
#TSB - module, class - use a class from a module created in another program
@author: hsantanam
"""

import matplotlib.pyplot as plt
import matplotlib.lines as pltl
# rocket_game is our own module
import rocket_game as rg

#create an instance of class rocket from module Rocket with x,y=10,5
rocket_1 = rg.Rocket(10,5)
#plot on simple graph
plt.plot(rocket_1.x, rocket_1.y, 'bo', label='line 1', linewidth=2, linestyle='dashed', markersize=12)
print(rocket_1.x, rocket_1.y)
#use the move functions from our module to move the rocket up, then left
#print the new position
# then plot each new position on the same graph in a different color

rocket_1.move_rocket('up',0,1)
print(rocket_1.x, rocket_1.y)
plt.plot(rocket_1.x, rocket_1.y, 'ro', label='line 1', linewidth=2, linestyle='dashed', markersize=12)

rocket_1.move_rocket('left', 2,0)
plt.plot(rocket_1.x, rocket_1.y, 'yo', label='line 1', linewidth=2, linestyle='dashed', markersize=12)
print(rocket_1.x, rocket_1.y)

#move the rocket down one
rocket_1.move_rocket('down',0.2)

#create a new instance called rocket_2

rocket_2 = rg.Rocket(5,10)
#use the get distance function from the module to calculate the distance
#and print it
print("distance is: ", rocket_2.get_distance(rocket_1))
