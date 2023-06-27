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
numbers = [1, 2, 3, 4]
numbers.length()
def add_taxes(item):
    new_item= item.copy
    new_item['taxes']=item['price']*.19
    return new_item
new_items = list(map(add_taxes,items))
print(new_items)
print(items)
