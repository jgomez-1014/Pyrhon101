#dictionary
my_dict = {}
print(type(my_dict))

my_dict = {
  "Nombre": "Jorge",
  "Edad": 32,
  "Ocupación": "Ingeniero"
}
print(my_dict)
print(len(my_dict))

print(my_dict['Edad'])
print(my_dict.get('unvalor'))

print('Nombre' in my_dict)
print('Apellido' in my_dict)