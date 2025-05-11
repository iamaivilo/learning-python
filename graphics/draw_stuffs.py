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


    def draw_random_rectangle(canObject,fill_color):
        x1=random.randrange(500)
        y1=random.randrange(500)
        x2=x1+random.randrange(500)
        y2=y1+random.randrange(500)
        canObject.create_rectangle(x1,y1,x2,y2,fill=fill_color)

    def draw_random_polygon(canObject,fill_color):
        x1=random.randrange(500)
        y1=random.randrange(500)
        x2=x1+random.randrange(500)
        y2=y1+random.randrange(500)
        x3=x2+random.randrange(500)     
        y3=y2+random.randrange(500)
        canObject.create_polygon(x1,y1,x2,y2,x3,y3,fill=fill_color)


    def un_draw(canObject: Canvas):
        canObject.delete('all')
        
 
    def color():
        print("this function is called")
        Diaglog.pickColor = colorchooser.askcolor()[1]
    

#main code
tk=Tk(className="tk2")
canvas=Canvas(tk,width=500,height=500)
canvas.pack()


drawrecBtn=Button(tk,text="Draw Random Rectangle",command=lambda:Diaglog.draw_random_rectangle(canvas,Diaglog.pickColor) )
drawBtn=Button(tk,text="Draw Random arc",command=lambda:Diaglog.draw_random_arc(canvas) )
colorBtn=Button(tk,text="Change color",command=lambda:Diaglog.color())
undoBtn=Button(tk,text="Undraw",command=lambda:Diaglog.un_draw(canvas))
drawpolBtn=Button(tk,text="draw random polygon ",command=lambda:Diaglog.draw_random_polygon(canvas,Diaglog.pickColor))
drawBtn.pack()
undoBtn.pack()
colorBtn.pack()
drawrecBtn.pack()
drawpolBtn.pack()

tk.mainloop()