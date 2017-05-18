# -*- coding: utf-8 -*-
''' OGÓLNY POGLĄD NA SYNTAX '''


print("Witamy w Pythonie!")
num_var = 5
limit_var = 10

def first_function():
    print("Iteracja po " + str(limit_var) + " liczbach")  # komentarz!
    for x in range(limit_var):
        if x == num_var:
            print("x równe {}".format(x))
        else:
            print("")



''' DEFINICJE FUNKCJI'''


def print_word(word):
    print(word)


def print_args(*args):
    for index, value in enumerate(args):
        print('{0}. {1}'.format(index, value))

print_args('apple', 'banana', 'carrot')


def print_kwargs(**kwargs):
    for name, value in kwargs.items():
        print('{0} is {1}'.format(name, value))

print_kwargs(fruit='apple', vegetable='carrot')


def print_default_value(fruit, vegetable='carrot', **kwargs):
    print('Fruit is {}'.format(fruit))
    print('Vegetable is {}'.format(vegetable))
    for name, value in kwargs.items():
        print('{0} is {1}'.format(name, value))

print_default_value('apple')
# or
print_default_value(fruit='apple')

print_default_value('apple', 'carrot', meat='bacon')
# or
print_default_value('apple', meat='bacon')


''' IMPORTOWANIE'''


import math
import sys

from django.forms import *

import our_application.module




'''CZESTE OPERACJE NA TYPACH DANYCH'''


# program losuje zbiór 6 unikatowych liczb od 1 do 49
from random import choice

results = set()

while len(results) < 6:
    results.add(choice(range(1,50)))

for x in results:
    print(x)


# przykład iteracji po słownikach
dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}

for val in dishes.values():
    print(val)

for key in dishes.keys():
    print(key)

for key, val in dishes.items():
    print(key, val)



# Lista Ocen Studentów przy wykorzystaniu klas
class Student:
    name = ""
    surname = ""
    mark = 0.0

students = []

print('Podanie pustej wartosci konczy wpisywanie')
while True:
    surname = input('Podaj nazwisko studenta > ')
    name = input('Podaj imie studenta > ')
    mark = input('Podaj ocene studenta > ')

    if not(surname and name and mark):
        break

    student = Student()
    student.surname = surname
    student.name = name
    student.mark = float(mark)
    students.append(student)

for idx, student in enumerate(students):
    print('{}. {} {} {}'.format(idx+1, student.surname, student.name, student.mark))


# DEBUGOWANIE

import pdb; pdb.set_trace()
