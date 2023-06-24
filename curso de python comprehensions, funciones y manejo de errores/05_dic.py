import random
'''
dic = {}

for i in range(1,5):
    dic[i]= i*2

print(dic)

dic_v2 = { i:i*2 for i in range(1,5)}
print(dic_v2)
contries = ['col','mex','bol','pe']
population = {}

for contry in contries:
    population[contry]= random.randint(1,100)
    
    
print(population)

population_v2 = {contry:random.randint(1,100) for contry in contries}
print(population_v2)

'''
names = ['nico', 'zule', "santi"]
ages = [12,56,98]

print(list(zip(names,ages)))

new_dic= {name: age for (name,age) in zip(names,ages)}
print(new_dic)



