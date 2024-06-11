#!/usr/bin/env python3
""" Contains the task_wait_random async function."""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Returns a list of delays in ascending order."""
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays
