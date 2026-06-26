#!/usr/bin/env python3
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    0 ile max_delay arasinda tesadufi bir saniye gozleyir
    ve sonda hemmin muddeti qaytarir.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
