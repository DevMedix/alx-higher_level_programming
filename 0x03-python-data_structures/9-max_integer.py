#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_num = my_list[0]
    for num_count in my_list:
        if num_count > max_num:
            max_num = num_count
    return max_num
