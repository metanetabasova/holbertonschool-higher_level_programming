#!/usr/bin/python3
'''obyektin mirasliq elaqesini yoxlayan modul'''


def inherits_from(obj, a_class):
    '''
    obyektin gosterilen sinifden
    miras alib-almadigini yoxlayir
    '''
    return issubclass(type(obj), a_class) and type(obj) is not a_class
