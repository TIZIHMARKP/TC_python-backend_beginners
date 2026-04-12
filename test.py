# =================== Functions ===================
# It is a block of code that does a specific task

# def greetBasic():
#     return "Hello"

# greet = greetBasic()   # I have called my function

# print(greet)


# def greet(name, age):
#     return f"Hello, {name} ({age})!"

# greetings = greet("John", 36)
# print(greetings)

# def calculate(number1, number2):
#     if number1 < 10:
#         number1 *= number1
#     return number1 + number2

# nowCalculate = calculate(2, 36)
# print(nowCalculate)

#=====================================
# ===== Default Arguments:
# def greetWithArgs(name="Guest"):
#     print(f"Hello, {name}!")

# greetWithArgs()

# def greetWithArgs(name, age = 30):
#     print(f"Hello, {name} {age}!")

# greetWithArgs("PrinceWill")
# greetWithArgs(name = "Tizih", age = 120)

# ==== Lamda Functions - arguments: expression
# E.g
# add = lambda x, y: x + y
# print(add(3, 5))         # Output: 8


# === Variable-lenth Arguments: ==== 
# You can pass an arbitrary number of arguments using *args and **kwargs.
# *args: collects extra positional arguments into a tuple.
# def sum_numbers(*args):
#     print(args)    # Prints the values in sum_numbers
#     return sum(args)

# print(sum_numbers(1, 2, 3))        # Output 6
# print(sum_numbers(4, 5, 6, 7))     # Output 22

# *args is very good because some times you may not know the length of the values

# # **kwargs: Collects extra keyword arguments into a dictionary
def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"*{key}: {value}")

greet(name="Tizih", age=30)
# Output:
# *name: Alice
# *age: 30


