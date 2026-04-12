# =================== File Handling Basics ===================
# Opening Files
# Use the open() function to open a file.
# Always close files to free resources

# file = open("example.txt", "r") # Open in read mode
# content = file.read()
# print(content)
# file.close()

# == File Modes
# Mode  -  Description
# r  -  Read (default). File must exist.
# w  -  Write. Creates a new file or truncates an existing one.
# a  -  Append. Adds content to the end of the file.
# r+  -  Read and write. File must exist.
# x  -  Create a new file


# == Reading Files
# Methods: read(), readline(), readlines().
# with open("example.txt", "r") as file:
#     # print(file.read())            # Read entire file
#     # print(file.readline())        # Read one line
#     print(file.readlines())        # Read all lines as a list

# == Writing Files
# Use write() or writelines() for writing.
with open("example.txt", "w") as file:
    file.write("Hello Tizih!\n")
    file.writelines(["Line 1\n", "Line 2\n"])
