"""
1.Tuple : Immutable
ordered sequence of items
Items can be of mixed types, including collection types

2.Strings : Immutable•
Conceptually very much like a tuple

3.List : Mutable
ordered sequence of items of mixed types
"""

tu = (23, 'abc', 4.56, (2, 3), 'def')
print(tu[1])
print(tu[1][2])
print(tu[-2])

# slice to return a copy of a subset
t = tu[1:3]
print(t)

# '+' operator concatenation of sequences produces a new instance
print('foo' + ' ' + 'bar')


# 'in' operator
print(23 in tu)
print('lord lucan' in tu)

# Be careful: the in keyword is also used in the syntax of forloops and list comprehensions.

# * operator produces a new tuple, list, or string that “repeats” the original content.
tu_3x = (1, 2, 3) * 3
print(tu_3x)

# more about lists
li = ['a', 'd', 'a', 'm']
print(li.index('a'))
print(li.count('a'))

# dir() lists the attributes and methods available to an object.
print(dir(li))

# other methods available to lists
# li.sort()
# print(li)
# li.reverse()

# alternative to dir()
# help(li)

