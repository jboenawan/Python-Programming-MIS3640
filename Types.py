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

print('\t\\') #why is it like this 

#BOOLEANS - conditional statement

age = int(input("please enter your age:"))

if age >21:
    print("yes you can")
else: 
    print ("no, you are not allowed")
