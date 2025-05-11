from tkinter import *
import random
from tkinter import colorchooser
class Diaglog:
    pickColor = 'black'
    def draw_random_arc(canObject):
        x1=random.randrange(500)
        y1=random.randrange(500)
        x2=x1+random.randrange(500)
        y2=y1+random.randrange(500)
        canObject.create_arc(x1,y1,x2,y2,extent=180,style=ARC,outline=Diaglog.pickColor)

    def un_draw(canObject: Canvas):
        canObject.delete('all')
        
 
    def color():
        print("this function is called")
        Diaglog.pickColor = colorchooser.askcolor()[1]
    

#main code
tk=Tk(className="tk2")
canvas=Canvas(tk,width=500,height=500)
canvas.pack()

drawBtn=Button(tk,text="Draw Random arc",command=lambda:Diaglog.draw_random_arc(canvas) )
colorBtn=Button(tk,text="Change color",command=lambda:Diaglog.color())
undoBtn=Button(tk,text="Undraw",command=lambda:Diaglog.un_draw(canvas))
drawBtn.pack()
undoBtn.pack()
colorBtn.pack()

tk.mainloop()