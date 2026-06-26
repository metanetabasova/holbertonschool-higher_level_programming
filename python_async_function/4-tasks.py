#!/usr/bin/env python3
"""
Bu modul task_wait_random funksiyasından istifadə edərək
çoxlu sayda asinxron tapşırıqları eyni vaxtda icra etməyi nümayiş etdirir.
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    task_wait_random funksiyasını n dəfə çağırır və yaradılan
    tapşırıqların bitmə müddətlərini (delays) artan sıra ilə qaytarır.
    """
    # task_wait_random funksiyası artıq bizə hazır asyncio.Task obyekti qaytarır
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    delays = []

    # Gözləmə müddətlərini tamamlanma ardıcıllığına görə siyahıya yığırıq
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
