AFC_east = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
numbers = [42,123]
empty = []
# print(AFC_east, numbers, empty)

#strings are not immutable but lists can be changed

AFC_east[-1] #prints the last string

print('Buffalo Bills' in AFC_east) #return True 

L = [
        ['Apple', 'Google', 'Microsoft'],
        ['Java', 'Python', ['Ruby','On Rail'], 'PHP'],
        ['Adam', 'Bart', 'Lisa']
    
]

print(L[0][0]) #returns Apple's index 
print(L[1][2][1]) #prints the On Rail index

for team in AFC_east:
    print(team)

numbers = [2,0,1,6,9]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
    
# print(numbers)

my_list = ['spam', 1, ['New England Patriots', \
                       'Buffalo Bills', 'Miami Dolphins', \
                       'New York Giants'], \
           [1, 2, 3]]
# print(len(my_list)) #returns 4 
#print(len(my_list[2])) #returns 4 too 

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
# print(c)

def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res

print(only_upper('Babson collEge'))

list = ['a'.'b','c']
list.append('d')

list.extend('efg')
list.insert(3,'oops')





