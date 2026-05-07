#!/usr/bin/python3
'''bu modul obyektin sinifini yoxlayan funksiyadan ibaretdir.'''


def is_same_class(obj, a_class):
    '''obyektin tam olaraq gosterilen sinifin numunesi olub olmadigini yoxlayir'''
    return type(obj) is a_class
