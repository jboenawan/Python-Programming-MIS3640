#Numbers 
import math 

import random 
print (random.random())
random.choice([1,2,3,4])

#string 
print('I\'m \"ok\".')
print ("I\'m learning\nPython.") #\n enters it in another line
print('\\n')
print(r'\\\t\\') #print whatever it is after r 

print('\t\\')

#BOOLEANS - conditional statement

age = int(input("please enter your age:"))

if age >21:
    print("yes you can")
else: 
    print ("no, you are not allowed")

##################### EXERCISE ##########################
import time 
time.time()
print time.time()
current = time.time()
second = current % 60 
minutes = (current//60) % 60 # // gives you the integer part of the division 
hours = (current//60)//60 % 24# % gives you the remainder of the division. 
days = current// 60 //60 //24
print ('Current time: %d days, %d hours, %d minutes, %d seconds from Epoch.' % (days, hours, minutes, second))