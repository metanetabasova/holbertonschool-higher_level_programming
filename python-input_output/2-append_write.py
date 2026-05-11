#!/usr/bin/python3
'''
Bu modul faylin sonuna metn elave etmek ucundur.
'''


def append_write(filename="", text=""):
    '''
    Metni UTF8 formatinda faylin sonuna elave edir
    '''
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
