fruitname={'apple','banana','cherry'}
for y in fruitname:
  print(y)
  #add item to sets
  fruitname={'apple','banana','cherry'}
  fruitname.add('shakti')
  print(fruitname)

  fruit1={'mango','strawberry','lytchee'}
  fruitname.update(fruit1)
  print(fruitname)
  #remove item
  fruit1={'mango','strawberry','lytchee'}
  fruit1.remove('mango')
  print(fruit1)


