def keywords_dict():
    fin = open("words.txt")
    keydict = dict()
    for w in fin:
        word = w.strip()
        keydict[word] = keydict.get(word,0) 
    return keydict

# print(keywords_dict())

liti = ['nodup','licates']
litu = ['asdf','asdf','apple','asdf']

def has_duplicates(lit):
    counter = 0
    d = dict()
    for i in lit:
        if i not in d:
            d[i] = 1
        elif i in d:
            d[i] += 1
            return True
    return False

print(has_duplicates(litu))
print(has_duplicates(liti))