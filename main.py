#! python3

import array as arr
import random

from army import Army

from tkinter import Tk, Canvas, W


def move(window, army):
   army.move()
   window.after(10, move, window, army)

def main():
   window = Tk()
   canvas = Canvas(window, bg="white", height=1000, width=1000)
   canvas.grid(row = 0, column = 0, sticky=W)

   goal_coords = [500-10,900-10,500+10,900+10]
   goal = canvas.create_oval(goal_coords, outline="blue",fill="blue")

   army = Army(window, canvas, 500, 50, goal_coords)

   move(window, army)

   canvas.pack()
   window.mainloop()

if __name__ == "__main__":
   main()