import turtle
import math

#################### no. 1 #######################

jo = turtle.Turtle()


turtle.speed(7)
turtle.circle(150)
turtle.penup()
turtle.sety(150)
turtle.pendown()
turtle.lt(30)

for i in range(4):
    turtle.fd(150)
    turtle.rt(120)
    turtle.fd(150)
    turtle.rt(120)
    turtle.fd(150)
    turtle.lt(150)

for i in range(4):
    turtle.penup()

    turtle.pendown()
    turtle.circle(150)



##################### no. 2 #######################

def flo(t,r):
    t.ht()
    t.circle(r)
    t.penup()
    t.sety(r)
    t.pendown()
    for i in range(6):
        t.circle(r,60)
        t.lt(120)
        t.circle(r,60)
        t.lt(60)

# flo(jo,150)

##################### no. 3 #######################
# turtle.ht()
# turtle.pensize(5)
# turtle.lt(180)
# turtle.circle(-50, extent=175)
# turtle.circle(50, extent = 175)
# turtle.circle(100)
# turtle.penup()
# turtle.lt(180)
# turtle.sety(100/3)
# turtle.pendown()
# turtle.circle(100/6)


turtle.mainloop()
