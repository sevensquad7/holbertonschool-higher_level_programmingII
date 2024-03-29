#!/usr/bin/python3
"""
This is "text_indentation" module
this module contains text_indentation function,
prints a text with 2 new lines after each of these
characters: '.', '?' and ':'
"""


def text_indentation(text):
    """Return string divided by spaces
    Arguments:
        text (string): string to be formmated
    raises:
        TypeError: if the text called with the program is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    list_lines = []
    for char in ".:?":
        text = text.replace(char, char + "\n\n")
#    list_lines = [lines.strip(' ') for lines in text.split('\n')]
    for lines in text.split('\n'):
        list_lines.append(lines.strip(" "))
    revised = "\n".join(list_lines)
    print(revised, end="")
