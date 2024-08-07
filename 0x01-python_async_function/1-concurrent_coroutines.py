#!/usr/bin/env python3
"""
Import wait_random from the previous python file
async routine called wait_n that takes in 2 int
arguments (in this order): n and max_delay
You will spawn wait_random n times with the specified max_delay.
list of delays in ascending order"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """documentation"""
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)
