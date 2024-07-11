#!/usr/bin/env python3
"""import modules, coroutine definition
measure and gather"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure the total runtime of executingasync_comprehension"""
    start = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end = time.perf_counter()
    return end - start
