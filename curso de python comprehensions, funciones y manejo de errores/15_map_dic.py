items =[
    {'product': 'shirt',
    'price':120},
    {'product': 'pants',
    'price':160},
    {'product': 'jacket',
    'price':205}
]

prices=list(map(lambda item:item['price'],items))

print(prices)
print(items)

def add_taxes(item):
    item['taxes']=item['price']*19
    return item
new_items = list(map(add_taxes,items))

print(new_items)