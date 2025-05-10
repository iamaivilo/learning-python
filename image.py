from tkinter import*
tk=Tk()
canvas = Canvas(tk,width = 3000,height = 2800)
canvas.pack()
my_image = PhotoImage(file="/Users/aivilo/Documents/code/car.png")
canvas.create_image(0,0, anchor = NW, image = my_image)
tk.mainloop()

