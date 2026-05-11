#!/usr/bin/python3
'''
Bu modul obyektin JSON formatinda fayla yadda saxlayan funksiya ucundur.
'''
import json


def save_to_json_file(my_obj, filename):
    '''
    Obyektin JSON temsili ile metn faylina yazir.
    '''
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
