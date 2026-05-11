#!/usr/bin/python3
'''
Bu modul obyekti Json formatina cerviren funksiya ucundur.
'''
import json


def to_json_string(my_obj):
    '''
    Obyektin JSON temsilini qaytarir
    '''
    return json.dumps(my_obj)
