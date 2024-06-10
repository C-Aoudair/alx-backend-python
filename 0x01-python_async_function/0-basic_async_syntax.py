#!/usr/bin/env python3
"""The basics of async"""
import random
import time


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay between 0 and max_delay seconds"""
    delay = random.uniform(0, max_delay)
    time.sleep(delay)
    return delay
