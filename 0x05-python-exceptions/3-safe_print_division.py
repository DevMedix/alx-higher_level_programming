#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        first_result = a / b
        return a / b
    except Exception:
        return None
    finally:
        try:
            results = a / b
            if b != 0:
                print("Inside result:", format(results))
        except Exception:
            print("Inside result: None")
