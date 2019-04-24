"""
Binding a variable in Python means setting a name to hold a reference to some object.

Assignment creates references, not copies

Names in Python do not have an intrinsic type. Objects have types.

Python determines the type of the reference automatically based on the data object assigned to it.

You create a name the first time it appears on the left side of an assignment expression
"""


# ###Literal assignment of types####
x = 34 - 23  # A comment.
z = 3.45

s1 = 'Hello'  # A string.
s2 = [1, 2, 3]  # a list
st = {1, 2, 3}
tu = (1, 2, 3)

dic = {1: 'one', 2: 'two', 3: 'three'}

s3 = """Hello 
'on' 
"many" 
lines"""  # triple quote

# basic printing via the "builtin" print functions
# more builtins https://docs.python.org/3/library/functions.html#built-in-funcs
print(x)
print("y output:", s2)  # print() accept many arguments
print(s3)


# ##### a bit more about variables - var names reference memory address
t1 = 'this'
v1 = len(t1) + 11
r1 = r2 = [t1, v1, 'a', 'list']  # r1 and r2 refer to same address
print(id(r1), r1, type(r1))  # id() shows memory address referred to
print(id(r2), r2, type(r2))

# an update to the object referred to will update value of both variables
r1.append({'key1': 1, 'another_key': 2, z: 3})
print(id(r2), r2)

# update an immutable type creates a new version of the object
print(id(v1), v1)
v1 += 1
print(id(v1), v1)
# the old data 15 is garbage collected as no variable refers to it
# In Python, the datatypes integer, float, and string (and tuple)
# are "immutable"


# type hinting python 3.6 and above
# https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html
adult_age: int = 18
adult_age = 'foo'

