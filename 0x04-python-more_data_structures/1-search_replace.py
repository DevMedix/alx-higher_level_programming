#!/usr/bi/python3
def search_replace(my_list, search, replace):
    new_item_list = []
    for item in my_list:
        if item == search:
            item = replace
        new_item_list.append(item)
    return new_item_list
