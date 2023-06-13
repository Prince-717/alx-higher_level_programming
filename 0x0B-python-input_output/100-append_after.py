#!/usr/bin/python3
"""Python module that defines a w_text file insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts w_text after each file_line containing a given string in a file
    """
    w_text = ""
    with open(filename) as file_to_read:
        for file_line in file_to_read:
            w_text += file_line
            if search_string in file_line:
                w_text += new_string
    with open(filename, "n") as n:
        n.write(w_text)
