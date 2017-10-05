# def is_abecedarian(word):
#     previous = word[0]
#     for c in word:
#         if c < previous: 
#             return False
#         previous = c
#     return True 



def is_abecedarian(word):
    the = 0
    while the < len(word)-1:
        if word[the+1] < word[the]:
            return False
        the += 1
    return True

print(is_abecedarian("afds"))

team = "idk whoat"

print(len(team))