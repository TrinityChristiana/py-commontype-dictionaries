"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

"""
Add several more words and their definitions
"""


word_definitions = {
    "Awesome": "The feeling of students when they are learning Python",
    "obvert": "to turn; to alter",
    "smalt": "deep blue",
    "baton": "heraldic sign of bastardy",
    "acropathy": "disease or illness of the extremities",
    "caricology": "study of sedges",
    "kneelet": "knee armour",
}

for (key, value) in word_definitions.items():
    print(f"{key}: {value}")

"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""


"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""
