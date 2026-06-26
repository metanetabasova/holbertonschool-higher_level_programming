#!/usr/bin/env python3
"""
Bu modul wait_n funksiyasının ümumi icra müddətini ölçmək
üçün funksionallıq təmin edir.
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    wait_n(n, max_delay) funksiyasının ümumi icra müddətini ölçür
    və orta hesabla hər tapşırığa düşən vaxtı (total_time / n) qaytarır.
    """
    # İcra başlamazdan əvvəlki zamanı qeyd edirik
    start_time = time.time()

    # Asinxron wait_n funksiyasını işə salırıq
    asyncio.run(wait_n(n, max_delay))

    # İcra bitdikdən sonrakı zamanı qeyd edirik
    end_time = time.time()

    # Ümumi keçən vaxtı hesablayırıq
    total_time = end_time - start_time

    return total_time / n
