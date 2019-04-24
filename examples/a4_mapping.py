"""
Basic mapping type in Python.

keys must be hashable
dicts can be nested

"""


my_dict = {"name": "millennial leon", "age": 30, "hair": "flowing"}
print(my_dict['name'],
      my_dict.get('name'),
      my_dict.get('dob', '1989')  # providing a default for dict access
      )

other_dict = {"name": "gen X leon", "age": 45}
my_dict.update(other_dict)
print(my_dict)
my_dict["hair"] = None
print(my_dict)

#mutable objects are not hashable can be used as dict keys
book = {(1, 10): "Introducton", (11, 15): "Notation and Definitions", (16, 30): "Fundamental Algorithms"}
print(book[(1, 10)])

#mutable objects are not hashable
#book = {[1, 10]: "Introducton", [11, 15]: "Notation and Definitions", [16, 30]: "Fundamental Algorithms"}

# looping over a dict using items
iterator = my_dict.items()
print(type(iterator))
print(dir(iterator))
for key, item in iterator:
    print(key, item)

