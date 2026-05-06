#!/usr/bin/python3
"""
Bu modul list sinfindən miras alan MyList sinfini saxlayır.
"""


class MyList(list):
    """Siyahı üzərində xüsusi əməliyyatlar aparan sinif."""

    def print_sorted(self):
        """Siyahını artan sıra ilə çap edir, lakin orijinalı dəyişmir."""
        print(sorted(self))