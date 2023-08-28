#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None

    try:
        print("Inside result: {}".format(result))
    finally:
        return result
