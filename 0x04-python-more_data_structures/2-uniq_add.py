#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    unique = list(set(my_list))
    for i in unique:
        sum += i
    return sum
