from turtle import*

setup(980,860)

Turtle_structure=Turtle()
Turtle_structure.speed(40)
a=['violet','indigo','blue','green','yellow','orange','red']

def art(d,angle,x,y):
    for color in a:
        for i in range(1,30):
            Turtle_structure.pencolor(color)
            Turtle_structure.circle(d)
            Turtle_structure.left(angle)
            d=d+1
art(60,3,0,0)
