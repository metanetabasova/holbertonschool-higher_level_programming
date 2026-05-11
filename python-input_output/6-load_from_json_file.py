#!/usr/bin/python3
"""
Bu modul JSON faylından obyekti yükləyən funksiyanı ehtiva edir.
"""
import json


def load_from_json_file(filename):
    """
    JSON faylından məlumatı oxuyur və Python obyekti kimi qaytarır.
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
