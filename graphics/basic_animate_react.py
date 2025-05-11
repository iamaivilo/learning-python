import time
from tkinter import*

def move_car(event):
    if event.keysym == "Up":
        canvas.move(1,0,-3)
    elif event.keysym == "Down":
        canvas.move(1,0,3)
    elif event.keysym == "Left":
        canvas.move(1,-3,0)
    elif event.keysym == "Right":
        canvas.move(1,3,0)

tk=Tk()
canvas = Canvas(tk,width=3000,height=1000)
canvas.pack()
car_image = PhotoImage(file="/Users/aivilo/Documents/code/car.png")
canvas.create_image(0,0, anchor = NW, image = car_image)



canvas.bind_all('<KeyPress-Up>',move_car)
canvas.bind_all('<KeyPress-Down>',move_car)
canvas.bind_all('<KeyPress-Left>',move_car)
canvas.bind_all('<KeyPress-Right>',move_car)

tk.mainloop()
