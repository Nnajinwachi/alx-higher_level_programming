#!/usr/bin/python3
"""function to read a text file"""


def read_file(filename=""):
    """read the file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
