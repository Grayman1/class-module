#TSB
#simple module to calculate rocket class and move it up, down, left, right on demand
#also calculate distance from this rocket to other rocket

from math import sqrt

class Rocket():
  #create and init the class
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
    
  def move_rocket(self, dir, x_increment=0, y_increment=0):
    
    if dir == 'up':
      self.y += y_increment
    elif dir == 'down':
      self.y -= y_increment
    elif dir == 'left':
      self.x -= x_increment
    elif dir == 'right':
      self.x += x_increment
    else:
      print("no change")

  def get_distance(self, other_rocket):
    distance = sqrt((self.x-other_rocket.x)**2+(self.y-other_rocket.y)**2)
    return distance