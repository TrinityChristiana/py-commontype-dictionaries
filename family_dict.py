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

for (relationship, value) in my_family.items():
    # for (key, value) in value.items():
    print(
        f"{value['name']} is my {relationship} and is {value['age']} years old")
