#!/usr/bin/python3
'''
Bu modul CSV melumatlarini oxuyub JSON formatina ceviren funksiyani ehtiva edir.
'''
import csv
import json


def convert_csv_to_json(csv_filename):
    '''
    CSV faylini oxuyur ve terkibini data.json faylina yazir.
    '''
    try:
        # CSV faylini oxumaq ucun aciriq
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            # DictReader her setri avtomatik lugete cevirir
            csv_reader = csv.DictReader(csv_file)

            # Butun lugetleri bir siyahiya toplayiriq
            data_list = [row for row in csv_reader]

        # Siyahini JSON formatinda data.json faylina yaziriq
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, indent=4)

        return True

    except (FileNotFoundError, IOError, PermissionError):
        # Fay; tapilmadiqda ve ya diger giris-cixis xetalarinda False qaytarir
        return False
