#! python3

from dot import Dot

class Army:
   population = 20
   def __init__(self, window, canvas, x, y):
      self.window = window
      self.canvas = canvas
      self.spawn_x = x
      self.spawn_y = y

      self.minions = []

      self.coords = [self.spawn_x-5, self.spawn_y-5, self.spawn_x+5, self.spawn_y+5]

      for x in range(self.population):
         circle = canvas.create_oval(self.coords, outline="red", fill="red")
         newDot = Dot(circle, window, canvas)
         self.minions.append(newDot)


   def move(self):
      for dot in self.minions:
         dot.move()




