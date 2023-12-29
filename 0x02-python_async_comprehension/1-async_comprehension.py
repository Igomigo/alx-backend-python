#!/usr/bin/env python3
"""
Contains a coroutine that will collect 10 random numbers
using an async comprehension over the async_generator function,
then return the 10 random numbers.
"""

import asyncio
from typing import Generator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """
    collect 10 random numbers using an async comprehension
    over async_generator, and returns the 10 random numbers.
    """
    return [i async for i in async_generator()]
