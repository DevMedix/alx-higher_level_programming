#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        first_result = a / b
        return a / b
    except ZeroDivisionError:
        return None
    finally:
        try:
            results = a / b
            if b != 0:
                print("Inside result:", format(results))
        except ZeroDivisionError:
            print("Inside result: None")
