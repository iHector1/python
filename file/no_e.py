def has_no_e(word):
    if 'e' in word:
        return True
    else:
        return False
fin=open('words.txt')
total_words=0
words_no_e=0
for line in fin:
    list=[]
    word=line.strip()
    total_words+=1
    if has_no_e(word) ==False:
        list.append(word)
        words_no_e+=1
print("Total words: ",total_words)
print("Words without e: ",words_no_e)
