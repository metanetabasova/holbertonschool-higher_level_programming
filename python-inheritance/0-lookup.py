#!/usr/bin/python3
'''bu modul obyejtlerin atributlarini yoxlamaq ucun funksiyadan ibaretdir'''


def lookup(obj):
    '''Obyektin butun atribut ve metodlarinin siyahisini qaytarir'''
    return dir(obj)
