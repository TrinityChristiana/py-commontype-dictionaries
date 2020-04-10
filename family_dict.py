# **************************** Challenge: The Family Dictionary ****************************
"""
Author: Trinity Terry
pyrun: python family_dict.py
"""

# Define a dictionary that contains information about several members of your family. Use the following example as a template.
my_family = {
    "brother": {
        "name": "Remle",
        "age": 18
    },
    "sister": {
        "name": "Olivia",
        "age": 11
    },
    "sister": {
        "name": "Gabrielle",
        "age": 15
    },
    "mother": {
        "name": "Teresa",
        "age": 42
    },
    "father": {
        "name": "Eugene",
        "age": 47
    },
    "self": {
        "name": "Trinity",
        "age": 20
    },
    "brother": {
        "name": "Diego",
        "age": 6
    },
    "sister": {
        "name": "Luna",
        "age": 3
    },
    "mother": {
        "name": "Skeeter",
        "age": 3
    }
}

# Using a dictionary comprehension, produce output that looks like: "Krista is my sister and is 42 years old"

for (relationship, value) in my_family.items():
    print(
        f"{value['name']} is my {relationship} and is {value['age']} years old")
