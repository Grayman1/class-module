#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#module that moves a point (x,y) in 4 different directions, and calculates distance from another existing point
#I called the class Rocket as it could be intended for a rocket game
Created on Thu Nov  1 08:14:42 2018

@author: hsantanam
"""
from math import sqrt


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
    
  #calculate distance from another point
  def get_distance(self, other_rocket):
    distance = sqrt((self.x-other_rocket.x)**2+(self.y-other_rocket.y)**2)
    return distance  