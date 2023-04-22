#CRUD: Create, Read, Update & compile

#Create
numbers = [1, 2, 3, 4, 4]
print(numbers)

#Read
print(numbers[1])

#Update
numbers[-1] = 5
print(numbers)

#Agrega un elemento al final de la lista
numbers.append(6)
print(numbers)

numbers.insert(0, "Arrays:")
print(numbers)

task = ["To Do 1", "To Do 2", "To Do 3"]
new_list = numbers + task
print(new_list)

indexToDo2 = new_list.index("To Do 2")
new_list[indexToDo2] = "To Do DOS"
print(new_list)

#Delete

new_list.remove("To Do 1")
print(new_list)

new_list.pop()
print(new_list)

new_list.pop(2)
print(new_list)

new_list.reverse()
print(new_list)

numbers2 = [1, 6, 3, 5, 10, 2]
print("Numeros:", numbers2)
numbers2.sort()
print("Numeros:", numbers2)

strings = ["re", "ab", "zu", "fa" ]
print(strings)
strings.sort()
print(strings)
