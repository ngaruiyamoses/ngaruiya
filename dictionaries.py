#A dictionary is a collectionof key value pair
#syntax: dictionary = {'key':'value'}
colours={'colour':'red'}
vehicle= {'type':'cadillac','plate number':'saba'}
print(colours)
print(vehicle)
#print(type(names)) #we use the type method to read the data
#accessing values in a dictionary
print(vehicle['type'])#you can access the value of an element inside the dictionary using the key
print(vehicle['plate number']) 


person={"name":"Moses Ngaruiya","ID number":"67899"}
print(person)
print(person["name"])
person["age"]="21"
print(person)
print(type(person))
del person["ID number"]
print(person)


#looping over dictionaries
for key, value in person.items():
    print(f"{value}:{key}")