from examples.a1_code_blocks import line

#looping over sequences, 'for' statement is more like 'forEach'
# 'in' acts more like an assignment operator in this context

li = range(0, 10)
print(line(), len(li), list(li))


def is_even(num):
    """
    is an int is even or not
    """
    if num % 2 == 0:
        return True
    else:
        return False


for item in li:
    if is_even(item):
        # ** is a power operator
        print(line(), item ** 2)

# enumerate loop with a counter
for count, item in enumerate('Friday'):
    print(line(), count, item)

# list comprehension
# [output expression   for item in iterable    if condition]
pow = [i**2 for i in li if is_even(i)]
print(line(), pow)

# nested list comprehension
# 'for's are listed in order
matrix = [[item for item in range(5)] for row in range(3)]
print(line(), matrix)


#flatten nested list
flatten = [r for row in matrix for r in row]
print(line(), flatten)

# one line list comprehensions are not always a good idea
numbers = [1, 2, 3, 4, 5, 6, 18, 20]
squares = ["small" if number < 10 else "big" for number in numbers if number % 2 == 0 if number % 3 == 0]
print(line(), squares)

# more readable maintainable -  be kind to your future self!
numbers = [1, 2, 3, 4, 5, 6, 18, 20]
squares = [
    "small" if number < 10 else "big"
    for number in numbers
    if number % 2 == 0
    if number % 3 == 0]
print(line(), squares)

# some times a plain for loop is better...


