# fin = open('words.txt')
# line = fin.readline()
# print(line)
# print(repr(line)) #prints the /n after the word. 

fin = open('C:/Users/jboenawan1/Documents/Fall 2017/Problem Solving & Design/Python-Programming-MIS3640/session10-dictionary_exercise/words.txt')
for line in fin:
    word = line.strip()
    # print (word)

############ EXERCISE 1 ############

def findlongwords():
    """
    prints only the words with more than 20 characters
    """
    fin = open("words.txt")
    for line in fin: 
        word = line.strip()
        if len(word) > 20:
            return word, len(word)

# print(findlongwords())

def has_no_e(word):
    """
    returns true if the given word doesn't have the letter "e" 
    in it 
    """
    word = str(word)
    # for letter in word: 
    #     if letter.lower() != "e":
    #         return True
    #     return False 
    return not "e" in word.lower()

# print(has_no_e("Babson"))
# print(has_no_e("College"))

def find_words_no_e():
    fin = open("words.txt")
    counter_no_e = 0 
    counter_total = 0
    for line in fin:
        counter_total +=1
        word = line.strip()
        if has_no_e(word):
            # print(word)
            counter_no_e += 1
    return (counter_no_e/counter_total)*100

# print("The percentage of the words with no 'e' is {.2f}%.".format(find_words_no_e()))

def avoids(word, forbidden):
    for letter in word: 
        if letter.lower() in forbidden:
            return False
    return True

forbidden = input("Enter a string of forbidden words: ")
print(avoids("string babble", forbidden))
# print(avoids("Babson", "ab"))
# print(avoids("College", "ab"))

def find_words_no_vowel():
    fin = open("words.txt")
    counter_no_vowel = 0 
    counter_total = 0
    for line in fin:
        counter_total +=1
        word = line.strip()
        if avoids(word, "aeiou"):
            # print(word)
            counter_no_vowel += 1
    return (counter_no_vowel/counter_total)*100

# print("The percentage of the words with no vowel is {.2f}%.".format(find_words_no_vowel()))

############## EXERCISE 2 ###############
