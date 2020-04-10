# **************************** Challenge: Dictionary of Words ****************************
"""
Author: Trinity Terry
pyrun: python dictionaryOfWords.py 
"""


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

"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""
print(word_definitions["obvert"])
print(word_definitions["kneelet"])


"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""
for (key, value) in word_definitions.items():
    print(f"The definition of {key} is {value}")
