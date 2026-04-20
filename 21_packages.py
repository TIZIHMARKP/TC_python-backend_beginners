# ================    PACKAGES    =====================
'''
Understanding PIP: Python Package Installer

What is PIP?
- PIP stands for "Pip Installs Packages".
- It is the default package manager for python and is used to install, namage, 
  and unistall python packages (libraries) from the Python Package Index (PyPI).
- PyPi is an online repository of software packages for Python, offering thoudands of prebuilt libraries.
'''

'''
Why Us PIP?
1. Ease of Use: PIP simplifies the process of installing and managing Python packages.
2. Large Ecosystem: Access thousands of 3rd party libraries from PyPI.
3. Dependency Management: Automatically handles dependencies required by a package
'''
 

'''
Installing PIP
- PIP comes pre-installed with Python versions 3.4 and above.
- To verify if PIP is installed, open a terminal or command prompt and type:

  pip --version

- If PIP is not installed:
  - For Windows:
    1. Download `get-pip.py` from the official website: [get-pip.py](https://bootstrap.pypa.io/get-pip.py).
    2. Run the script in the terminal:
       python get-pip.py

  - For Linux/maxOS:
    
  sudo apt install python3-pip  # For Linux
  brew install pip              # For maxOS with Homebrew
'''


'''
# Basic PIP Commands

# 1. Installing a Package

   pip install <package_name>

   Example:
   pip install requests
   - This installs the `requests` library, used for making HTTP requests.

# 2. Upgrading a Package
   
   pip install --upgrade <package_name>

   Example:

   pip install --upgrade flask

# 3. Uninstalling a Package

   pip uninstall <package_name>

   Example:

   pip uninstall numpy

# 4. Listing Installed Packages

    pip list

    Example output:

    Package     Version
    -----        ----
    Flask       2.3.0
    requests    2.28.1

# 5. Checking Package Information

    pip show <package_name>

    Example:

    pip show django

    Output:

    Name: Django
    version 4.2
    Summary: A high-level python web framework.
    Locations: /usr/local/lib/python3.9/site-packages

# 6. Installing Specific Package Versions

    pip install <package_name>==<version>

    Example:

    pip install pandas==1.4.3

# 7. Saving Installed Packages to a File

    pip freeze > requirements.txt

    - This generates a `requirements.txt` file, listing all installed packages and their versions.

# 8. Installing Packages from a Requirements File

    pip install -r requirements.txt

    - useful for replicating environments across projects.

'''
