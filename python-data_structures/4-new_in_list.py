#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Orijinal siyahının surətini yaradırıq
    copy_list = my_list[:]
    
    # İndeksi yoxlayırıq
    if idx < 0 or idx >= len(my_list):
        return copy_list
    
    # Dəyişikliyi surət üzərində edirik
    copy_list[idx] = element
    return copy_list
