# =================== Logical & Identity Operators ===================
# Logical Operators use the "and" "or" and "not" operators
# Identity operators use the "is" and "is not" operators

x = 5
y = 5

z = [0, 1, 2, 3, 4, 5]

aString = "Tizih"
strings = ["Prince", "Will", "Tizih"]

# == Logical Operators ==
print(x < 5 and x < 10)                     #and -Returns True if both statements are true
print(x < 5 or x < 4)                       #or  -Returns True if one of the statements is true
print(not(x < 5 and x < x < 10) )           #not -Reverse the result, returns False if the result is true

# == Membership Operators ==
print(x is y)                               #is        -Returns True if both variables are the same object
print(x is not y)                           #is not    -Returns True if both variables are not the same object

print(x in z)                               #in        -Returns True if a sequence with the specified value is present in the object
print(x not in z)                           #not in    -Returnss True if a sequence with the specified value is not present in the object

print(aString in strings)                   #in        -Returns True if a sequence with the specified value is present in the object
print(aString not in strings)               #not in    -Returns True if a sequence with the specified value is not present in the object


