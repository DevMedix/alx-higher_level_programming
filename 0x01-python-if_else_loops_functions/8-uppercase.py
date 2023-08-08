#!/usr/bin/python3
def uppercase(str):
    uppercase_str = ""
    for ch in str:
        if 'a' <= ch <= 'z':
            uppercase_str += chr(ord(ch) - 32)
        else:
            uppercase_str += ch
    print(uppercase_str)
