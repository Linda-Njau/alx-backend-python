#!/usr/bin/env python3
"""wait_random async function"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """wait_random func that takes max_delay default of 10"""
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
