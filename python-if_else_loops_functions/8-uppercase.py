#!/usr/bin/python3
def uppercase(str):
    for char in str:
        ascii_code = ord(char)
        if ascii_code >= 97 and ascii_code <= 122:
            char = chr(ascii_code - 32)
        print("{}".format(char), end="")
    print("")
