#!/usr/bin/python3
'''
Bu modul sade JSON seriyalasdirma ve deserilizasiya funksiyalarini ehtiva edir.
'''
import json


def serialize_and_save_to_file(data, filename):
    '''
    Python lugetini JSON farmatina yazir
    '''
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    '''
    JSON faylindan melumat oxuyur ve onu Python lugetine cevirir.
    '''
    with open(filename, mode="r", encoding='utf-8') as f:
        return json.load(f)
