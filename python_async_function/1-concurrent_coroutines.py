#!/usr/bin/env python3
"""
Bu modul verilmis sayda tesadufi gozleme tapsiriqlarini
asinxron sekilde icra edir ve neticeleri siralo sekilde qaytarir.
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    wait_random funksiyasini n defe eyni vaxtda (concurrently) cagirir.
    Gozleme muddetlerini (delays) artan sira ile siyahi seklinde qaytarir
    """
    # n defe wait_random tapsirigi yaradiriq
    tasks = [wait_random(max_delay) for _ in range(n)]

    delays =[]
