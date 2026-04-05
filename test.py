# =================== Handling Strings in Python ===================
# 

# x = "Hello Tizih"

# print(x[0])

# print(x[:5])

# print(x[2:5])   # slicing a string

# print(x[:6])    # slicing a string from character 4 to the end

# print(x[7:])    # slicing a string from character 7 to the end

# print(x[-5:-2])   # gives you orl

# y = "Hello Marko"

# print(y.upper())           # Uppercase
# print(y.lower())           # lowercase
# print(y.capitalize())      # first character uppercase
# print(y.startswith("H"))   # True


# z = "He llo the re"
# print(z.strip())        # Removes leading and trailing whitespaces

# u = "Hello Fhere"
# print(u.replace("F", "I"))  # Replace a character

# v = "Jane, Royal"
# print(v.split(", "))   # returns ['Jane', 'Doe']


# ===================== Concatenation ======================
# Concatenations means bringing strings together or adding strings together


a = "Hello"
b = "There"
c = a + b
d = " "
e = a + d + b

print(c)
print(e)
print("Hello" + " " + "There")
f = a + " " + b
print(f)

#  ========     Formatting =========

name = "Prince Mark"
age = 40
info = f"My name is {name}. I am {age} years old"
print(info)


