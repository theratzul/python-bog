#!/usr/bin/python3

capitals = {"USA": "Washington",
            "Romania": "Bucharest",
            "Bulgaria": "Sofia"}

#call dictionary atributes
dir(capitals)

#print dictionary atributes and help
print(dir(capitals))
#print(help(capitals))

print(capitals.get("Romania"))

# if/get of capital print

if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital doesn't exists")

# update map
capitals.update({"Germania": "Munchen"})
print(capitals)

# remove key from map
capitals.pop("Bulgaria")
capitals.popitem()

print(capitals)

# print for loop keys keys

keys = capitals.keys()
print(keys)
for key in capitals.keys():
    print(key)

# print values

values = capitals.values()    
for value in capitals.values():
    print(value)

# transform map in list with items = [(),(),()]    
items = capitals.items()    
for key, value in capitals.items():
    print(f"{key}: {value}")    