#!/usr/bin/python3

"""a function that writes a text file (UTF8)
and returns the number of characters written"""


def write_file(filename="", text=""):
    """writes the specified text to file"""
    with open(filename, 'w', encoding="utf-8") as myFile:
        data_written = myFile.write(text)
    return data_written
