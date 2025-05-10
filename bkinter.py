from tkinter import *

def apple():
    print ("hi ")
    
def bananana(canObject):
    print("bye")
    canObject.create_line(0,500,500,0)

def canvas_hello(canObject):
    canObject.create_line(0,0,500,500)

tk=Tk(className="tk2")
canvas=Canvas(tk,width=500,height=500)
canvas.pack()

btn=Button(tk,text="yes",command=lambda: canvas_hello(canvas) )
etn=Button(tk,text="no",command=lambda: bananana(canvas))
btn.pack()
etn.pack()
tk.mainloop()