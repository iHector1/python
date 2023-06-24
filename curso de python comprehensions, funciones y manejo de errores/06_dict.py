import random
contries = ['col','mex','bol','pe']


population_v2 = {contry:random.randint(1,100) for contry in contries}
print(population_v2)

result ={contry:population for (contry,population) in population_v2.items() if population>20}
print (result)

text='Hola,soy hector'
unique={ c: text.count(c) for c in text if c in 'aeiou'}
print(unique)