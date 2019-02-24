#! python3

import random
from tkinter import Tk, Canvas

class Dot:

   movement_speed = 10

   def __init__(self, circle, window, canvas):
      self.circle = circle
      self.window = window
      self.canvas = canvas
      self.dead = False

      self.updateCoods()

      self.movements = []

   def isDead(self):
      return self.dead

   def move(self):
      if not self.dead:
         x_vel = random.randint(-self.movement_speed,self.movement_speed)
         y_vel = random.randint(-self.movement_speed,self.movement_speed)

         self.canvas.move(self.circle, x_vel, y_vel)

         self.movements.append([x_vel, y_vel])

         self.updateCoods()

         self.checkCollision()

   def checkCollision(self):
      if(self.x < 0 or self.x > 1000 or self.y < 0 or self.y > 1000):
         self.dead = True

   def updateCoods(self):
      coords = self.canvas.coords(self.circle)

      self.x = coords[0]
      self.y = coords[1]