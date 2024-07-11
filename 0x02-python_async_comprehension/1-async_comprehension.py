#!/usr/bin/env python3
"""import modules, coroutine definition
async comprehension"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """collect 10 random numbers using an async comprehending
    over async_generator"""
    return [i async for i in async_generator()]
