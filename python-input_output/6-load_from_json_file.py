#!/usr/bin/python3
'''
Bu modul JSON faylindan obyekti yukleyen funksiya ucundur.
'''
import json


def load_from_json_file(filename):
    '''
    JSON faylindan melumati oxuyur ve Python obyekti kimi qaytarir.
    '''
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
