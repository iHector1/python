def right_justify(name):
    i=0
    leng=int(len(name))
    while i<leng+1:
        print('',end="\t")
        i+=1
    print(name)

if __name__=='__main__':
    print("Insert a name")
    name=str(input())
    right_justify(name)
