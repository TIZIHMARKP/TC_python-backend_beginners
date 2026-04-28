# =================== Logging and Error Handling  ===================
# == The Logging Module
# Provides a flexible way to log messages


import logging

# logging.basicConfig(
#     filename = "app.log",
#     level = logging.DEBUG,
#     format = "%(asctime)s - %(levelname)s - %(message)s"
# )

# logging.info("This is an info message.")
# logging.error("This is an erro message.")

# Logging Levels
# Level  -  Purpose
# DEBUG  -  Detailed information for debugging.
# INFO  -  General infomation about execution
# WARNING  -  An indication of potential problem
# ERROR  -  Serious issue occurred.
# CRITICAL - A severe error causing program crash


# Writting logs to a file
# logging.basicConfig(filename = "./app.log", level=logging.INFO)
# logging.info("Program started")
# logging.warning("This is a warning")
# logging.error("An error occurred")


def greet():
    logging.critical("Program started")

    for i in range(10):
        print(i)
    logging.critical("Program finished")


greet()