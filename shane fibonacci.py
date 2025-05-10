import turtle

def  fiseq(a):
    if(a<3):
        return 1
    else:
         return fiseq(a-1)+fiseq(a-2)
    
def drawfibo(input):
    turtle1=turtle.Turtle()
    turtle1.color(1,0,0)
    turtle1.begin_fill()
    i = 1
    while(i < input):
        radius = fiseq(i)
        turtle1.circle(radius *4, 90)
        i = i + 1

    turtle1.hideturtle() 

drawfibo(50) 