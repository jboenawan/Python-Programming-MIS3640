def print_twice(a):
    print(a)
    print(a)

def cat_twice(p1,p2):
    cat = p1+p2
    print_twice(cat)

l1 = 'Bing'
l2 = 'Chandler'
#cat_twice(l1,l2)

def gmab():
    str1 = 'break'
    return str1
    print ('another break') #return = end of function.
    #will not be executed.

print(gmab()*10)


############################### DRAWING EXERCISE ##################################
import turtle 

tt = turtle.Turtle()

#print (tt)
#tt.fd(100)
#tt.lt(90)
#tt.fd(100)
#tt.lt(90)
#tt.fd(100)
#tt.lt(90)
#tt.fd(100)



for i in range(4):
    print("hello,world")

def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)
#square(tt)

def squarel(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

#squarel(tt, 200)

def polygon(t, length, n):
    for i in range(n+1):
        t.fd(length)
        t.lt(360/n)

#polygon(tt, 150, 8)

import math 

def circle(t, r):
    circumference = 2 *math.pi*r
    n = int(circumference/2)
    length = circumference / n 
    polygon(t, length, n)

# circle(tt, 20)

def arc(t, r, angle):
    arc_length = 2*math.pi*r*angle/360
    n = int(arc_length/3) +1 
    step_length = arc_length/n
    step_angle = angle/n
    for i in range (n):
        t.fd(step_length)
        t.lt(step_angle)

arc(tt, 100, 70)



turtle.mainloop()

