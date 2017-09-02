#how many seconds is 42 minutes and 42 seconds?
seconds = int(42*60+42)
print(seconds)

""" how many miles are there in 10 km? Hint: 1.61km
equals to a mile."""

miles = float(10/1.61)
print(miles)

#What is your average pace? (time per mile in minutes and sec)#
pace_in_sec = (seconds/miles)
print(pace_in_sec)
pace_in_min = ((seconds/miles)/60)
print(pace_in_min)


#What is your average speed in miles per hour?#

print(miles/seconds*60*60)
