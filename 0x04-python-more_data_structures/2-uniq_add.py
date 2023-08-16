#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_item_list = []
    sum_item = 0
    for item in my_list:
        if item not in new_item_list:
            new_item_list.append(item)
    for new_item in new_item_list:
        sum_item += int(new_item)
    return sum_item
