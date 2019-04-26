from examples.a1_code_blocks import line


# generators use yield something
def integers():
    for i in range(1, 9):
        yield i


integers()
print(line(), integers())
# Generator objects execute when next() is called
print(line(), next(integers()))

chain = integers()
print(line(), list(chain))


def squared(seq):
    for i in seq:
        yield i * i


def negated(seq):
    for i in seq:
        yield -i


chain = negated(squared(integers()))
print(line(), list(chain))

# generator expressions
integers = range(8)
squared = (i * i for i in integers)
negated = (-i for i in squared)
print(line(), list(negated))


s1 = sum((x * 2 for x in range(10)))
print(line(), s1)

# if it is a single call to a function you can drop the outer "()"
s2 = sum(x * 2 for x in range(10))
print(line(), s2)
