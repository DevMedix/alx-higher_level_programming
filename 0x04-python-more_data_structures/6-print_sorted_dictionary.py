#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_dict = sorted(a_dictionary.keys())
    for item in sort_dict:
        print(f"{item}: {a_dictionary[item]}")
