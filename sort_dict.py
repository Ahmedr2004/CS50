people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]
#def f(people):
#   return people["name"]

people.sort(key= lambda person: person["name"])

print(people)