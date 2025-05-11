import time
from tkinter import*
tk=Tk()
canvas = Canvas(tk,width=3000,height=1000)
canvas.pack()
car_image = PhotoImage(file="/Users/aivilo/Documents/code/car.png")
canvas.create_image(0,0, anchor = NW, image = car_image)
for x in range(1,181):
    canvas.move(1,5,0)
    tk.update()
    time.sleep(0.01)
