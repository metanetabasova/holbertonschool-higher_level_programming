#!/usr/bin/env python3
"""
Bu modul adi funksiya daxilində asyncio.Task obyektinin
yaradılmasını nümayiş etdirir.
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    wait_random(max_delay) funksiyasını götürür və onu
    baxıla bilən bir asyncio.Task obyekti kimi qaytarır.
    """
    # Coroutine-i Task obyektinə çeviririk və icra üçün növbəyə salırıq
    task = asyncio.create_task(wait_random(max_delay))
    return task
