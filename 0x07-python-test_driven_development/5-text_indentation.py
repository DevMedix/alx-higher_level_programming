#!/usr/bin/python3
"""
This module contains text_indentation functions
it takes one str parameter
raises a TypeError when another type is passed
"""
def text_indentation(text):
    """
    Format and print text with double line breaks after '.', '?', and ':'.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    formatted_text = text.replace(".", ".\n\n").replace("?", "?\n\n").replace(":", ":\n\n")

    lines = formatted_text.strip().split('\n')

    for line in lines[:-1]:
        print(line.strip())

    if lines:
        print(lines[-1].strip(), end='')
