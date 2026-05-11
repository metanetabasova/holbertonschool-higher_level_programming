#!/usr/bin/python3
'''
Bu skript butun komanda setri arqumentlerini PYTHON siyahisina elave edir.
'''
import sys
import os

# evvelki tapsiriqdaki funksiyalari idxal edirik
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Eger fayl movcuddursa movcud siyahini yukleyirik
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Komanda setri arqumentlerini siyahiya elave edirik
items.extend(sys.argv[1:])

# Yenilenmis siyahini fayla yaziriq
save_to_json_file(items, filename)
