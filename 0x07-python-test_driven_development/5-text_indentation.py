#!/usr/bin/python3
"""

Python function that prints 2 new lines after ".?:" characters

"""


def text_indentation(text):
    """ Function that prints 2 new lines after ".?:" characters

    Args:
        text: input string

    Returns:
        No return

    Raises:
        TypeError: If text is not a string


    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    string = text[:]

    for m in ".?:":
        text_list = string.split(m)
        string = ""
        for index in text_list:
            index = index.strip(" ")
            string = index + m if string is "" else string + "\n\n" + index + m

    print(string[:-3], end="")
