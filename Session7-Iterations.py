# def sum(n):
#     n = 0
#     for i in range (n):
#         return n = n + i + 1

# print(sum(10))

####################################
result = 0
for i in range(10):
     result = result + i + 1
     print("in the {}th iteration, new result = {}".format(i,result))
    
#result  i   new result 
# 0      1       1
# 1      2       3

# if multiplication, then change initial condition (result) = 1

# SUM OF ODD NUMBERS 
result = 0
for i in range(1,1000,2):
    result = result + i

# SUM OF EVEN NUMBERS 
result = 0 
for i in range(0, 1001, 2):
    result = result + i 
# print(result)

########### WHILE STATEMENT ###########
def countdown(n):
    while n > 0:
        print(n)
        n = n-1
    print("Blastoff!")

countdown(10)