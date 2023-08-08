#!/usr/bin/python
def islower(c):
    for i in range(ord('a'), ord('z') + 1):
        if c == chr(i):
            return True
    return False
