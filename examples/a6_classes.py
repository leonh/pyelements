"""
Classes in python
mixture of the class mechanisms found in C++ and Modula-3


"""
from typing import List
from examples.a1_code_blocks import line


# Anatomy of a class


class MyClass:
    my_class_vars = {}

    def __init__(self, **args):
        self.my_class_vars.update(**args)

    def method(self):
        self.my_class_vars['new var'] = 1
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

    #def __repr__(self):
    #    return "<MyClass>"

    #def __str__(self):
    #    return "MyClass: %s" % self.my_class_vars


obj = MyClass(a=1, b=2, c=3)
print(line(), obj)
print(line(), obj.method())
print(line(), obj.my_class_vars)


class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])


import math


class BoxedPizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza({self.radius!r}, '
                f'{self.ingredients!r})')

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi


p = BoxedPizza(4, ['mozzarella', 'tomatoes'])
print(line(), p)
print(line(), p.area())


#py 3.7 Data classes

from dataclasses import dataclass


class RegularBookClass(object):
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __repr__(self):
        return f'RegularBookClass(t' \
            f'title={self.title}, ' \
            f'author={self.author}, ' \
            f'price={self.price})'


r_book = RegularBookClass(
    title="Roger's Profanisaurus: Das Krapital",
    author='Viz',
    price=15.50
)
print(line(), r_book)
r_book.price = "20.00"



@dataclass
class DataclassBook(object):
    title: str
    author: str
    price: float


dc_book = DataclassBook(
    title='The Pearl Necklace: Viz Annual',
    author='Viz',
    price=19.99)

print(line(), dc_book)

dc_book2 = DataclassBook(
    title="The Camel's Toe: Viz Annual",
    author='Viz',
    price=19.99)

dc_book3 = DataclassBook(
    title='Viz 40th Anniversary Profanisaurus: War and Piss',
    author='Viz',
    price=19.99)


@dataclass
class BookShelf:
     books: List[DataclassBook]


bs = BookShelf([dc_book, dc_book2, dc_book3])
print(line(), bs)


class MayBot:
    """
    demonstrates the usage of 'dunder' methods in your classes

    these double underscore methods allow your classes to emulate builitn
    types and be compatible with the rest of python itself.
    """
    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count += 1
        return self.value


may_bot_2019 = MayBot('Brexit means Brexit.', 5)
for soundbite in may_bot_2019:
    print(line(), soundbite)

may_bot_2018 = MayBot('Strong and stable.', 5)
for soundbite in may_bot_2018:
    print(line(), soundbite)
