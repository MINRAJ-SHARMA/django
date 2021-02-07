person={
    'name':'shakti',
    'age':'twenty'

}
print(person['age'])
##
print(person.get('name'))
print(person.keys()) #list of all keys
print(person.values())
print(person.items())
person['age']=25
print(person['age'])
#update method
person.update({'name':'manoj'})
print(person)
#add item
person['height']=5.6
print(person)
#remove item
person.pop('age')
print(person)
#pop item
person.popitem()
print(person)
#loop
for x in person:
    print(x)
for  x in person:
    print(person[x])
    #print both

for x,y in person.items():
    print(x,y) 
    ##
    name=person.copy()
    print(name)
    