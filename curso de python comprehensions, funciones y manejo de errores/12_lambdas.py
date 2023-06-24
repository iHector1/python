def increment(x):
    return x + 1

print(increment(2))


result= lambda x:x+1

print(result(20))

full_name = lambda name,lastName: f'Full name is {name.title()} {lastName.title()}'

text = full_name('macario','bRujo')
print(text)