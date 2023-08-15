#!/usr/bin/python3
def no_c(my_string):
    new_word = ''
    for letter in my_string:
        if ('c' not in letter) and ('C' not in letter):
            new_word += letter
    return new_word
