#!/usr/bin/env python3
"""
    import modules, define the coroutine,
    loop and yield
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """loops 10 times, each asynchronously wait 1 second and yield"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
