#how many seconds is 42 minutes and 42 seconds?
seconds = int(42*60+42)
print(seconds)

""" how many miles are there in 10 km? Hint: 1.61km
equals to a mile."""
miles = int(10/1.61)
print(miles)

#What is your average pace? (time per mile in minutes and sec)#
pace_in_sec = int((seconds/miles))
print(pace_in_sec)

pace_in_min = int(((seconds/miles)/60))
print(pace_in_min)


#What is your average speed in miles per hour?#
print(miles/seconds*60*60)

###EXERCISE 1 - Variable, Expresions, and Statements###

#What is the volume of a sphere with radius 5?

"""pi = 3.14
rad = int(input("Radius?"))
sphere = (4/3)*pi*(rad**3)

print ("The volume of a sphere with " rad " radius is %d", sphere)"""

#What is the total wholesale cost for 60 copies? 

def wholesale_cost():
    price = 24.95
    bookstore = 0.40
    books_amount = int(input("How many books are you buying?"))
    if books_amount == 1:
        print(price - 3)
    elif books_amount > 1:
        print((price - 3)+((books_amount-1)*price)*0.75)
