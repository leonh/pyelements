"""
1.Tuple : Immutable
ordered sequence of items
Items can be of mixed types, including collection types

2.Strings : Immutable•
Conceptually very much like a tuple

3.List : Mutable
ordered sequence of items of mixed types
"""
from examples.a1_code_blocks import line  # import from this package

# import sys
# print(sys.path)
tu: tuple = (23, 'abc', 4.56, (2, 3), 'def')
print(line(), tu[1])
print(line(), tu[1][2])
print(line(), tu[-2])
# print(line(), tu[2][1]) # what will this do?

# slice to return a copy of a subset
t = tu[1:3]
print(line(), t)

# '+' operator concatenation of sequences produces a new instance
print(line(), 'foo' + ' ' + 'bar')

# 'in' operator
print(line(), 23 in tu)
print(line(), 'lord lucan' in tu)

# Be careful: the in keyword is also used in the syntax
# of for loops and list comprehensions.

# * operator produces a new tuple, list, or string
# that “repeats” the original content.
tu_3x = (1, 2, 3) * 3
print(line(), tu_3x)

# more about lists
li = ['a', 'd', 'a', 'm']
print(line(), li.index('a'))
print(line(), li.count('a'))

# dir() lists the attributes and methods available to an object.
print(line(), dir(li))

# other methods available to lists
# li.sort()
# print(li)
# li.reverse()

# alternative to dir()
# help(li)

