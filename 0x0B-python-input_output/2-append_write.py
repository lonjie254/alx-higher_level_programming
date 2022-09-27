#!/usr/bin/python3

"""a function that appends a string at the end of a text file
(UTF8) and returns the number of characters added"""


def append_write(filename="", text=""):
    """appends the specified text to file"""
    with open(filename, 'a', encoding="utf-8") as myFile:
        data_written = myFile.write(text)
    return data_written
