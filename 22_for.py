'''
for element in range(10, 21):
  print(element)
'''

my_list = [23, 45, 67, 89, 43]
for element in my_list:
  print(element)

my_tuple = ('Jorge', 'Andres', 'Manu',)
for element in my_tuple:
  print(element)

prodcut = ('Jorge', 'Andres', 'Manu',)
for element in my_tuple:
  print(element)

product = {
  'name': 'Camisa',
  'price': 100,
  'stock': 50
}
for key in product:
  print(key, '==', product[key])

for key, value in product.items():
  print(key, '==', value)

people = [
  {
    'name': 'Jorge',
    'lastName': 'Gomez',
    'age': 32
  },
  {
    'name': 'Gustavo',
    'lastName': 'Petro',
    'age': 55
  },
  {
    'name': 'Irma',
    'lastName': 'Moontalvo'
  }
]

for person in people:
  print(person)
  for key in person:
    print(key, '==', person[key])
  