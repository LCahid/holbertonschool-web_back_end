#!/usr/bin/env python3
'''async'''
import time
import random
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''measure time'''
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    totar_time = end - start
    return totar_time/n
