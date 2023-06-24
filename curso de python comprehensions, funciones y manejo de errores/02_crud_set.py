set_contries={'col','mex','bol'}

size = len(set_contries)

print(size)

print('col' in set_contries)

print('pe' in set_contries)

#add
set_contries.add('pe')
print(set_contries)
set_contries.add('pe')
print(set_contries)

#update
set_contries.update({'ar','ecua','pe'})
print(set_contries)

#remove
set_contries.remove('col')
print(set_contries)
set_contries.remove('ar')
print(set_contries)
#set_contries.remove('ar')
set_contries.discard('ar')
print(set_contries)
set_contries.clear()
print(len(set_contries))