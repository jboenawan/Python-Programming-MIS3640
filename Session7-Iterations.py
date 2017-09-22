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

# countdown(10)

iteration = 0 
count = 0 
while iteration < 5: 
    for letter in "Hello, world":
        count +=1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration +=1

iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
# count resets to 0

iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 


while True: 
    line = input('> ')
    if line == "done":
        break
    print(line)

mysum = 0
for i in range(5,11,2):
    mysum += i
    if mysum ==5:
        break

print(mysum)
