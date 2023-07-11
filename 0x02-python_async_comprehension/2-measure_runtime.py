#!/usr/bin/env python3
"""measure_runtime coroutine"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """Measures total runtime"""
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    stop_time = time.perf_counter()
    return stop_time - start_time
