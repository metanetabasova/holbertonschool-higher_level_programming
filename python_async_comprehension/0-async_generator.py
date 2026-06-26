#!/usr/bin/env python3
"""
Bu modul 10 dəfə dövr edərək hər saniyədən bir təsadüfi
ədədlər generasiya edən asinxron generatoru ehtiva edir.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    10 dəfə dövr edir, hər dəfə asinxron olaraq 1 saniyə gözləyir
    və 0-10 aralığında təsadüfi bir float ədəd yield edir.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
