#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#Created on Thu Nov  1 17:03:14 2018

@author: hsantanam
"""
#TSB - Create Class in Python - rocket positions (x,y)
import matplotlib.pyplot as plt

class Rocket():
  def __init__(self, x=0, y=0):
    #each rocket has (x,y) position; user or calling function has choice
    #of passing in x and y values, or by default they are set at 0
    self.x = x
    self.y = y
    
  def move_up(self):
    self.y += 1
    
  def move_down(self):
    self.y -= 1
    
  def move_right(self):
    self.x += 1
    
  def move_left(self):
    self.x -= 1
    

#Make a series of rockets
rockets=[]
rockets.append(Rocket())
rockets.append(Rocket(0,2))
rockets.append(Rocket(1,4))
rockets.append(Rocket(2,6))
rockets.append(Rocket(3,7))
rockets.append(Rocket(5,9))
rockets.append(Rocket(8, 15))
  
#Show where each rocket is

for index, rocket in enumerate(rockets):
  #original position of rockets
  print("Rocket %d is at (%d, %d)." % (index, rocket.x, rocket.y))
  plt.plot(rocket.x, rocket.y, 'ro', linewidth=2, linestyle='dashed', markersize=12)
  #move the 'rocket' one up
  rocket.move_up()
  print("New Rocket position %d is at (%d, %d)." % (index, rocket.x, rocket.y))
  #plot the new position
  plt.plot(rocket.x, rocket.y, 'bo', linewidth=2, linestyle='dashed', markersize=12)
  #move the rocket left
  rocket.move_left()
  plt.plot(rocket.x, rocket.y, 'yo', linewidth=2, linestyle='dashed', markersize=12)

#show graph legend to match colors with position
plt.title("Positions from using Python Class")
plt.gca().legend(('original position','^ - Moved up', '< - Moved left'))
plt.show()
#plt.legend(loc='upper left')
