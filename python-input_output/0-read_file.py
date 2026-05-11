#!/usr/bin/python3
def read_file(filename = ""):
    '''UTF8 formatinda olan  metni oxuyur ve stdout-a cap edir.'''
    with open(filename, mode = "r", encoding = "utf-8") as f:
        print(f.read(), end = "")
