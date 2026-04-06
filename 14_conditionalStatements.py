# =================== Conditional Statements ===================
#  
    
# code block
# elif another_condition:
# code block
# else:
# code block

# Example 1
# age = int(input("Enter your age: "))

# if age < 18:
#     print("You are a minor")
# elif  18 <= age < 65:
#     print("You are an adult")
# else:
#     print("You are a senior citizen")


# Logical operators
# age = int(input("Enter your age: "))
# x = 4

# if age > 18 and age < 30:
#     print("You are a young adult")

# if age == 25 or age == 50:
#     print("You are at a milestone age")

# print("\n===========================")
# gender = str(input("Enter your gender (M/F): "))

# if age == 25:
#     if gender == "male":
#         print("You are a 25 year old male")
#         if x  == 4:
#             print("Your should have four kids by now")
#     elif gender == "female":
#         print("You should be a mom by now")
# else:
#     print("You are not 25 years old")


# ===========  Match case: =============
# it's good for simple conditions

r = 6
match r:
    case 5:
        print("ok")
        pass
    case 6:
        print("not ok")
        print("It is a six")
        pass

