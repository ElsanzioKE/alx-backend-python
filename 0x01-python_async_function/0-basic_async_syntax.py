#!/usr/bin/env python3
"""
asynchronous coroutine taking in an integer
argument(max_delay default value 10)
named wait_random that awaits for a random
delay betwn 0 and max_delay seconds and returns it
random module used"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """asynchronous function so use of async and await a must
    random.uniform"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
