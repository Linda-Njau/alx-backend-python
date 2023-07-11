#!/usr/bin/env python3
"""async_comprehension coroutine"""

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """collect 10 random numbers using async comprehensing"""
    result = [i async for i in async_generator()]
    return result
