from tkinter import *
import random
from tkinter import colorchooser
class Diaglog:
    pickColor = 'black'
    def draw_random_rectangle(canObject,fill_color):
        x1=random.randrange(500)
        y1=random.randrange(500)
        x2=x1+random.randrange(500)
        y2=y1+random.randrange(500)
        canObject.create_rectangle(x1,y1,x2,y2,fill=fill_color)

    def un_draw(canObject: Canvas):
        canObject.delete('all')
        

    def color():
        Diaglog.pickColor = colorchooser.askcolor()[1]
    

#main code

tk=Tk(className="tk2")
canvas=Canvas(tk,width=500,height=500)
canvas.pack()

drawBtn=Button(tk,text="Draw Random Rectangle",command=lambda:Diaglog.draw_random_rectangle(canvas,Diaglog.pickColor) )
colorBtn=Button(tk,text="Change color",command=lambda:Diaglog.color())
undoBtn=Button(tk,text="Undraw",command=lambda:Diaglog.un_draw(canvas))
drawBtn.pack()
undoBtn.pack()
colorBtn.pack()

tk.mainloop()