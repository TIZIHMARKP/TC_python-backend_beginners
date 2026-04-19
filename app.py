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
import math

print(math.sqrt(16))   # Using the math module to find the square root

x = math.ceil(2.4)
y = math.floor(2.4)

print(x)      # returns 3
print(y)      # returns 2



