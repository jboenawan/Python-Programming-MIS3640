############################## EXERCISE 3 #############################
str = "i like big dogs and I can't lie"
str.split("and")
str.strip("lie")
str.replace("and","&")
str.lstrip("i") #left of the string. 

############################## EXERCISE 4 #############################

def price(ok):
    ok = str(ok)
    pp = 0 
    for i in ok:
        i = ord(i) + pp
        pp += 1
    return i

price("banana")
# studio code is broken ._. cannot run function. 

print("bananas $",price("bananas"))
print("rice $",price("rice"))
print("paprika $",price("paprika"))
print("potato chips $",price("potato chips"))
print("--------------------------")
print("Total $", price("bananas")+price("rice")+price("paprika")+price("potato chips"))

print(len("potato chips"))

print("{:13} {:1} {:5.2f}".format("bananas","$",price("bananas")))
print("{:13} {:1} {:5.2f}".format("rice","$",price("rice")))
print("{:13} {:1} {:5.2f}".format("paprika","$",price("paprika")))
print("{:13} {:1} {:5.2f}".format("potato chips","$",price("potato chips")))
print("--------------------------")
print("{:6} {:1} {:6}". format("Total", "$", "237.00"))
