#! python3

import random
from tkinter import Tk, Canvas

class Dot:

   movement_speed = 20

   def __init__(self, circle, window, canvas, goal):
      self.circle = circle
      self.window = window
      self.canvas = canvas
      self.dead = False

      self.goal = goal
      self.reached_goal = False

      self.updateCoods()

      self.movements = []

   def isActive(self):
      return not self.dead and not self.reached_goal

   def move(self):
      if self.isActive():
         x_vel = random.randint(-self.movement_speed,self.movement_speed)
         y_vel = random.randint(-self.movement_speed,self.movement_speed)

         self.canvas.move(self.circle, x_vel, y_vel)

         self.movements.append([x_vel, y_vel])

         self.updateCoods()

         self.checkCollision()

   def checkCollision(self):
      if(self.x < 0 or self.x > 990 or self.y < 0 or self.y > 990):
         self.dead = True
      elif self.x in range(self.goal[0], self.goal[2]) and self.y in range(self.goal[1], self.goal[3]):
         self.reached_goal = True

   def updateCoods(self):
      coords = self.canvas.coords(self.circle)

      self.x = coords[0]
      self.y = coords[1]

   def destroy(self):
      self.canvas.delete(self.circle)