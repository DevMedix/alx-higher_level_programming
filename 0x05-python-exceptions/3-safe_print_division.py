#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        if b != 0:
            print("Inside result:", format(result))
        else:
            print("Inside result: None")
        return result
