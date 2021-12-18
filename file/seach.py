def has_no_e(word):
    for letter in word:
        if letter =='e':
            return False
    return True

def avoids (word,forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True
def uses_only(word,available):
    for letter in word:
        if letter not in available:
            return False
    return True
 
