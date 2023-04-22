person = {
  "name": 'Jorge',
  "last_name": 'Gomez',
  'langs': ['python', 'javascript', 'html'],
  'age': 32  
}

print(person) 

person['name'] = 'Jorge Arturo'
print(person)

person['langs'].append('css')
print(person)

del person['age']
person.pop('langs')
print(person)

print("=" * 30)

print('items')
print(person.items())

print('keys')
print(person.keys())

print('values')
print(person.values())