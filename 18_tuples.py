#Tuples: Arrays Unmutable
numbers = (1, 2, 3, 4, 4)
strings = ("nico", "jorgi", "guru", "jorgi")
print(numbers)
print(type(numbers))
print(strings)

print(strings[1])
print(strings.index("nico"))
print(strings.count("jorgi"))

#Transformacion a Array
print(type(strings))
my_list = list(strings)
print(type(my_list))

my_list[1] = "petro"
print(my_list)

#Transformacion a Tuple
my_tuple = tuple(my_list)
print(my_tuple)