names = ['Rose','Jerry','Alex']
scores = [95,75,85]

grades = dict()
type(grades) #gets dict

grades = {'Zach':75, 'Alex':85, 'Julian': 95}

#add a new item 
grades['Xiang'] = 88

'Zach' in grades #returns True 

#counting the alphabets 
letters = [0,0,0,0,0,0,0]
s = 'abbbccddee'

for letter in s:
    if letter == 'a':
        letters[0] += 1
    elif letter == 'b':
        letters[1] += 1
    
for letter in s:
    letters[ord(letter)-97] += 1

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1 #have to do this first. the key doesn't exist; so we create one.  
        else:
            d[c] += 1
    return d

print(histogram('Bookkeeper'))

h = histogram ('Bookbookkeeper')

print(sorted(h))

def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c,0) + 1 
    return d

def print_hist():
    for c in h:
        print(c,h[c])

print_hist()

#can do multiple columns thing 
for k,v in d.items():
    print(k,v)
#returns two columns with key and values. 


lst = [1,2,3,3]
len(lst)

s = set(lst) #return {1,2,3}
d = {'a': 1, 'b': 1}
set(d.values()) # returns unique values of {1}

t = {2,3,4}
s.union(t) #overlapping of sets. {1,2,3,4}

