"""
Binding a variable in Python means setting a name to hold a reference to some object.

Assignment creates references, not copies

Names in Python do not have an intrinsic type. Objects have types.

Python determines the type of the reference automatically based on the data object assigned to it.

You create a name the first time it appears on the left side of an assignment expression
"""


x = 34 - 23  # A comment.
s1 = 'Hello'  # A sting.
s2 = [1, 2, 3]  # a list


s3 = """Hello 
'on' 
"many" 
lines"""  # triple quote

z = 3.45

#  == is used for comparison
#  logical operators are words (and, or , not) and not symbols
#  whitespace defines the code block - typically 4 spaces
if z == 3.45 or s1 == 'Hello':
    x += 1
    s2 = s1 + "World"  # String concat, s2 is now a string

# basic printing via the "builtin" print functions
# https://docs.python.org/3/library/functions.html#built-in-funcs
print(x)
print("y output:", s2)  # print function can accept many arguments
print(s3)


# a bit more about references
t1 = 'this'
v1 = len(t1) + 11
r1 = r2 = [t1, v1, 'a', 'list']
print(id(r1), r1, type(r1))  # id() shows memory address that a variable refers to
print(id(r2), r2, type(r2))
r1.append({'key1': 1, 'another_key':2, z: 3})
print(id(r2), r2)
r1 = 'foobar'
print(id(r1), r1, type(r1))

#
print(id(v1), v1)
v1 += 1
print(id(v1), v1)
# the old data 15 is garbage collected as no variable refers to it
# In Python, the datatypes integer, float, and string (and tuple)
# are "immutable"