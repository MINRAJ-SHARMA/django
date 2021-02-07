fruit=['apple','orange','mango','banana']
print(fruit)
print(type(fruit))
print(fruit[0])
#add item in list
fruit.append('lytchee')
print(fruit)
#add item in particular list
fruit.insert(1,'avocada')
print(fruit)
#extend list
fruit1=['papya','cherry','pineapple']
fruit1.extend(fruit)
print(fruit1)
#remove item
fruit1.remove('papya')
print(fruit1)
fruit.pop()
print(fruit)
del fruit
print(fruit)
fruit.clear()
print(fruit)

