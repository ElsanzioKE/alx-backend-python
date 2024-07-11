#!/usr/bin/env python3
"""function not async
task_wait_random takes max_delay
returns asyncio.Task"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """documentation"""
    return asyncio.create_task(wait_random(max_delay))
