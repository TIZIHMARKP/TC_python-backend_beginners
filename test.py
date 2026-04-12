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
# Default Arguments:
def greetWithArgs(name="Guest"):
    print(f"Hello, {name}!")

greetWithArgs()

def greetWithArgs(name, age = 30):
    print(f"Hello, {name} {age}!")

greetWithArgs("PrinceWill")
greetWithArgs(name = "Tizih", age = 120)