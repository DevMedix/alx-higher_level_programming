#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = [tuple_a[i] if i < len(tuple_a) else 0 for i in range(2)]
    b = [tuple_b[i] if i < len(tuple_b) else 0 for i in range(2)]
    new_add_tuple = (a[0] + b[0], a[1] + b[1])
    return new_add_tuple
