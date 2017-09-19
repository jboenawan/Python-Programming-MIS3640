import turtle
import math

#################### no. 1 #######################

jo = turtle.Turtle()
def arc(t, r, angle):
    jo.speed(0)
    arc_length = 2*math.pi*r*angle/360
    n = int(arc_length/3) +1 
    step_length = arc_length/n
    step_angle = angle/n
    for i in range (n):
        t.fd(step_length)
        t.lt(step_angle)
    jo.setposition()
arc(jo, 100, 360)



##################### no. 2 #######################

def arc(t, r, angle):
    arc_length = 2*math.pi *r*angle/360
    n = int(arc_length/3) + 1
    step_length = arc_length/n
    step_angle = angle/n
    




##################### no. 3 #######################




turtle.mainloop()
