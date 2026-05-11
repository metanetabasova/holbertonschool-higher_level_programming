#!/usr/bin/python3
"""
Bu modul fayl oxumaq funksiyasını ehtiva edir.
"""


def read_file(filename=""):
    """Faylı UTF8 formatında oxuyur və çap edir."""
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
