#!/usr/bin/env python3
"""code from wait_n alter it into task_wait_n
"""
import asyncio
from typing import List
tawr = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """documentation"""
    delays = await asyncio.gather(*(tawr(max_delay) for _ in range(n)))
    return sorted(delays)
