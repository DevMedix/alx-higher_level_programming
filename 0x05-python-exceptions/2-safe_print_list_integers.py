#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        length = 0
        for item in my_list:
            length += 1

        for item in my_list[:x]:
            if isinstance(item, int):
                if x <= length:
                    print("{:d}".format(item), end='')
                    count += 1
                elif x > length:
                    raise IndexError("list index out of range")
        print()
        return count
    except TypeError:
        return 0
