#!/usr/bin/python3
"""
Bu modul MyList sinfini təyin edir.
"""


class MyList(list):
    """Siyahıdan (list) miras alan sinif."""

    def print_sorted(self):
        """Siyahının elementlərini artan sıra ilə çap edir."""
        print(sorted(self))
