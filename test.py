# =================== Logging and Error Handling  ===================
# == Error Handling
"""
Error handling allows you to manage runtime errors (exceptions) in a clean and controlled way.
Instead of allowing your program to crash, you can catch the error, display a helpful message,
or take corrective action.
Using try, except, else, and finally
"""

# try: Code that might raise an error is placed inside the try block.
# except: If an error occurs in the try block, it is caught by the except block.
# else: Code inside, the else block is executed if no error occurs in the try block.
# Finally: Code inside the finally block is always executed, regardless of whether an error occurred or not.

# Basic Example:
# try:
#     x = 10 / 0  # Division by zero
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# else:
#     print("Division successful.")
# finally:
#     print("Execution completed.")



# ==== Custom exceptions

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    check_age(-5)
except ValueError as e:
    print(f"Error: {e}")

# Handling Multiple Exceptions