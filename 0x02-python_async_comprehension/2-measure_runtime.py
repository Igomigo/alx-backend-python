#!/usr/bin/env python3
"""
Contains a coroutine called measure_runtime coroutine
that will execute async_comprehension four times in parallel
using asyncio.gather.
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Executes the async_comprehension coroutine four times
    in parallel using asyncio.gather and returns the total runtime """
    start: float = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    elapsed: float = time.perf_counter() - start
    return elapsed
