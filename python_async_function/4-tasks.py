#!/usr/bin/env python3
"""
Bu modul task_wait_random funksiyasından istifadə edərək
çoxlu sayda asinxron tapşırıqları icra edir.
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    task_wait_random funksiyasını n dəfə çağırır və
    tamamlanma müddətlərini artan sıra ilə qaytarır.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
