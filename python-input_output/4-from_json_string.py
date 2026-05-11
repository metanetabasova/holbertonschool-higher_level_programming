#!/usr/bin/python3
'''
Bu modul JSON formatli metni Python obyektine ceviren funksiya ucundur
'''
import json


def from_json_string(my_str):
    '''JSON metni ile temsil olunan Python obyektini qaytarir.
    '''
    return json.loads(my_str)
