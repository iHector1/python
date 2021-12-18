def palindrome(word):
    i=0
    j=len(word)-1
    while i<j:
        if word[i] !=word[j]:
            return False
        i+=1
        j-=1
    return True
fin=open('words.txt')
total=0
palin=0
for line in fin:
    list=[]
    word=line.strip()
    total+=1
    if palindrome(word) ==True:
        palin+=1

print("Total words: ",total )
print("palindrome: ",palin)
  
