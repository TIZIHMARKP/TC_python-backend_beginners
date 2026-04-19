'''
# What is a Module?
A module is a file containing Python definitions and statements. It can include:
 ->   Functions
 ->   Variables
 ->   Classes
 ->   Imports of other modules

 Modules allow you to organize your code into logical sections, making it reusable and easier to manage. YOur modules should contain related logic
'''
# How to Import a Module


# We have 3 types of modules: 3rd party, build in and custom muldes
# Built-in modules are the onces build into python directly. You do not have to install or write them
# Third-party modules are modules written by other developers to make work easier. They are made available for others to install.
# Custom modules are the ones you wrote yourself for different implementationsin your codebase

# To use a module, you can import it:
# import math

# print(math.sqrt(16))   # Using the math module to find the square root

# x = math.ceil(2.4)
# y = math.floor(2.4)
# print(round(2.6))

# print(x)      # returns 3
# print(y)      # returns 2

# ======   Date and time Module  =====
# import datetime

# a = datetime.datetime.now()
# print(a)

# b = datetime.datetime(2020, 5, 17)

# print(b)

# You can also import specific functions or variables from a module:
# from math import pi

# print(pi)   # Direct access to pi

'''
# Some common built-in modules include:
 ->    math: Provides mathematical functions like sqrt(), factorial(). (https://www.w3schools.com/python/module_math.asp)
 ->    os: Provides functions for interacting with the operating system (e.g, file manipulations, working with dirctories).
 ->    datetime: Provides functions for working with dates and times. 
 ->    logging: Provides functions for logging eecutions, actions, exceptions, and etc
'''

# example
# import os

# print(os.listdir())  # List files and directories in the current directory


'''
What is package?
A package is a collection of modules in a directory.
It must include a special file called __init__.py which can be empty or include initialization code for the package.

# ==== Structure of a Package  ====
my_package/
    __init__.py
    module1.py
    module2.py
'''

# To import a module from a package:
# from my_package import module1

## Renaming an import
# import mymodule as mx

# a = mx.person1["age"]
# print(a)


# ==== Creating a custom module circle.py =====
# circle.py  -  we have the following in the circle.py file
# import math

# def area(radius):
#     return math.pi * radius ** 2

# = Let us create a script that imports and uses circle.py =
import circle   # This line works
import circle as circlecalculations  # This line works


radius = 5
area = circlecalculations.area(radius)
shape = circlecalculations.shape()
print(f"The area of the {shape} with radius {radius} is {area}")