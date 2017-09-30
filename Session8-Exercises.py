############################## EXERCISE 3 #############################
str = "i like big dogs and I can't lie"
str.split("and")
str.strip("lie")
str.replace("and","&")

############################## EXERCISE 4 #############################
def iya(n):
    for i in n:
        i += ord(i)
        return i 

def price(ok):
    ok = str(ok)
    pp = 0 
    for i in ok:
        i = ord(i)
    return i

# studio code is broken ._.

print("bananas $",price("bananas"))
print("rice $",price("rice"))
print("paprika $",price("paprika"))
print("potato chips $",price("potato chips"))
print("--------------------------")
print("Total $", price("bananas")+price("rice")+price("paprika")+price("potato chips"))