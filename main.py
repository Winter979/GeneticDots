#! python3

import array as arr
import random

from army import Army

from tkinter import Tk, Canvas, W

def move():
   army.move()
   window.after(33, move)

window = Tk()
canvas = Canvas(window, bg="white", height = 1000, width = 1000)
canvas.grid(row = 0, column = 0, sticky=W)

army = Army(window, canvas, x = 500, y = 50)

move()

canvas.pack()
window.mainloop()