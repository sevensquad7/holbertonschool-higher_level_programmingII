#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    num = 0
    if not bool(roman_string):
        return 0
    check = isinstance(roman_string, str)
    if check is False:
        return 0
    for i in range(len(roman_string)):
        num += roman[roman_string[i]]
        if i > 0:
            if roman[roman_string[i - 1]] < roman[roman_string[i]]:
                num -= roman[roman_string[i - 1]] * 2

    return num
