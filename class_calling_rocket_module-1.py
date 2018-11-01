#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 20:02:06 2018
#TSB - module, class - use a class from a module created in another program
@author: hsantanam
"""

#TSB - Create Class in Python - rocket positions (x,y)
import matplotlib.pyplot as plt
import simple_module1 as rg

#Make a series of rockets
rockets=[]
rockets.append(rg.Rocket())
rockets.append(rg.Rocket(0,2))
rockets.append(rg.Rocket(1,4))
rockets.append(rg.Rocket(2,6))
rockets.append(rg.Rocket(3,7))
rockets.append(rg.Rocket(5,9))
rockets.append(rg.Rocket(8, 15))

#Show where each rocket is

for index, rocket in enumerate(rockets):
  #original position of rockets
  print("Rocket %d is at (%d, %d)." % (index, rocket.x, rocket.y))
  plt.plot(rocket.x, rocket.y, 'rs', linewidth=2, linestyle='dashed', markersize=12)
  #move the 'rocket' one up
  rocket.move_up()
  print("New Rocket position %d is at (%d, %d)." % (index, rocket.x, rocket.y))
  #plot the new position
  plt.plot(rocket.x, rocket.y, 'bs', linewidth=2, linestyle='dashed', markersize=12)
  #move the rocket left
  rocket.move_left()
  plt.plot(rocket.x, rocket.y, 'ys', linewidth=2, linestyle='dashed', markersize=12)

#show graph legend to match colors with position
plt.title("Positions from using Module")
plt.gca().legend(('original position','^ - Moved up', '< - Moved left'))
plt.show()
