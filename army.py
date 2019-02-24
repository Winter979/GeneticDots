#! python3

from dot import Dot

class Army:
   population = 1000
   mutation_ratio = 0.1

   def __init__(self, window, canvas, x, y, goal):
      self.window = window
      self.canvas = canvas
      self.spawn_x = x
      self.spawn_y = y

      self.goal_coords = goal

      self.goal_center = [(goal[0] + goal[2])/2,(goal[1] + goal[3])/2]

      self.coords = [self.spawn_x-5, self.spawn_y-5, self.spawn_x+5, self.spawn_y+5]

      self.minions = []
      self.populateArmy()

   def populateArmy(self):

      for minion in self.minions:
         minion.destroy
         del minion

      self.minions = []

      for x in range(self.population):
         circle = self.canvas.create_oval(self.coords, outline="red", fill="red")
         new_dot = Dot(circle, self.window, self.canvas, self.goal_coords)
         self.minions.append(new_dot)

      self.alive = True

   def move(self):

      self.alive = False

      for dot in self.minions:
         if(dot.isActive()):
            self.alive = True
            dot.move()

      if not self.alive:
         self.mutateArmy()
         self.populateArmy()

   def mutateArmy(self):
      for minion in self.minions:
         value = self.calcualateReward(minion)
         print(value)


   def calcualateReward(self, minion):
      value = 0

      if minion.reached_goal:
         value = 1000
      else:
         distance_x = pow(abs(self.goal_center[0] - minion.x),2)
         distance_y = pow(abs(self.goal_center[1] - minion.y),2)

         distance_to_goal = pow(distance_x +  distance_y, 0.5)

         value = 1000 - distance_to_goal

      return value
