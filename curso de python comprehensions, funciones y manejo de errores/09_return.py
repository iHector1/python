def find_volume(length=1,width=1,depth=1):
    return length*width*depth,width,'hola'


result = find_volume(2,6,9)
print(result[0])

result,width,text = find_volume()
print(result)
print(width)
print(text)

