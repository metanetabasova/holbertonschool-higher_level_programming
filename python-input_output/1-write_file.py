#!/usr/bin/python3
'''
Bu modul fayla yazi yazmaq ucundur.
'''


def write_file(filename="", text=""):
    '''
    Metni UTF8 formatinda fayla yazir ve yazilan simvollarin sayini qaytarir
    '''
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
