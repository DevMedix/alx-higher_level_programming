#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set3 = set()
    for item in set_1:
        if item not in set_2:
            set3.add(item)
    for item in set_2:
        if item not in set_1:
            set3.add(item)
    return set3
