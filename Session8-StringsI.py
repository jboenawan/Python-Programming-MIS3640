team = "New England Patriots"

letter = team[1]
print(letter)

print(team[len(team)-1])
print(team[-1]) #shorter version of the above one. 


for i in range(len(team)):
    if team[i] != " ":
        print(team[i])


for letter in team: 
    if letter.isalpha():
        print(letter)

letter = "JKLMNOPQ"
suffix = "ack"
for i in letter:
    if i == "O" or i == "Q":
        print(i+"u"+suffix)
    else:
        print(i+suffix)

print(team[::-1]) #reverse the words. 

print(team[::-2]) #skips over one word starting from the end. 

print(team[::1])

print(team[::2])

new_team = team[:12] + "Beavers"
print(new_team)

def find(word, letter):
    index = 0 
    while index < len(word):
        if word[index] == letter:
            return index 
        index = index + 1
    return -1 #if letter isn't in the word, return -1 

print(find(team, "W"))

def count(word, letter):
    word = str(word.lower())
    count = 0
    for i in word: 
        if i == letter:
            count = count +1
    return count

print(count("I Love eating and Sharing", "a"))

############# Counting the Vowels ##############

c = 0
vowels = "aeiou"
for i in vowels: 
    c += count(team,letter)


