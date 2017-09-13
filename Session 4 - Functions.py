#def function (input): 
#return output / print output. 

#functions: name()
#   has a docstring; need in project. 
#   has a body 

type(42)
# <class 'int'>
type(42.5)
#<class 'float'>
# type = function name 
# 42 is an argument. Takes argument, returns result. 

msg = 'hello'
type (msg)
# <class 'str'>

#int('hello')
# valueError: cannot do strings. 
#   use float() first to convert strings to number.
#   always assume input from users are strings. 
#   int('3.14') --> cannot. have to be float('3.14')

#typeError: abs() takes exactly one argument. 

#play with functions round(), chr(), min(), ord()
round(2.712, 2) #the 2 is how many digits you want rounded. round(number, [ndigits])
min(-123, -103, 23, 423, 948, 231, 543) # more than one argument. 
ord('a') #each a corresponds to a number = 97 
chr(97) # returns 'a' 

isinstance(100,int)
#True
isinstance(100.0, int) #is it true or not? 
#False 

len('hello') # prints out the length of the string 

##################### MATH FUNCTIONS ######################

import math 
ratio = 100 
math.log10(ratio) #returns log of 100 = 2
d = 45 
r = d/180 *math.pi 
print (r)
math.sin(r)

def lyr_beatles():
    print("Hey Jude, \nDon\'t make it bad.")
lyr_beatles()

print(type(lyr_beatles))

def repeat():
    lyr_beatles()
    print('Na na na na na na na na na')
    lyr_beatles()
repeat()

def twice(name):
    print(name)
    print(name)
twice("Josie Boe")

def my_abs(number):
    print(abs(number))
my_abs(-132)

def quad(a, b, c):
    first = (-b+math.sqrt(b**2- 4*a*c))/2*a
    second = (b+math.sqrt(b**2 - 4*a*c))/2*a
    print("The square root of {:d}, {:d}, {:d} is {:.2f}, {:.2f}.".format(a,b,c,first,second))
quad(-1, 2, 1)
