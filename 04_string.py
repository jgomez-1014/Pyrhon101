name = "jorge"
lastname = "gomez"

full_name = name + " " + lastname
print(full_name)

quote = "I'm Jorge"
print(quote)

#formato
template = "Mi nomrbe es" + name + "y mi apellido es" + lastname
print(template)

template2 = "Mi nomrbe es {} y mi apellido es {}".format(name, lastname)
print(template2)

template3 = f"Mi nomrbe es {name} y mi apellido es {lastname}"
print(template3)