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
pi = 3.14
rad = float(input("Radius? \n"))
sphere = (4/3)*pi*(rad**3)

print ("The volume of a sphere with {:.2f} radius is {:04.1f}.".format(rad,sphere))

#What is the total wholesale cost for 60 copies? 
cost = (24.95-24.95*0.4)*60+3+((60-1)*0.75)
print('the total wholesale cost for 60 books is $%.2f' % cost)
print("The total wholesale cost for 60 books is ${:.2f}.".format(cost))

#if i leave my house at 6:52am and run 1 mile at an easy pace (8:15 per mile), 
#then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, 
#what time do I get home for breakfast? (hint: pace is time/miles)



#if my average grade rises from 82 to 89. What is the % of the increase?
yah = (89-82)/82*100
print("the percentage increase is {:04.1f}%.".format(yah)) #4 digits places including the dot. 
print("the percentage increase is %04.1f%%" % yah)

#format the result as 'xx.x%'. Keep one figure after decimal point. 
print("the percentage increase is {:04.1f}%.".format(yah)) #4 digits places including the dot. 
print("the percentage increase is %04.1f%%" % yah)