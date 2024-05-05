#!/usr/bin/env python3
'''async'''
from typing import List
import random
import asyncio
task_wait_random = __import__('3-task').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''wait random'''
    dictwait = []
    for i in range(n):
        dictwait.append(await task_wait_random(max_delay))
    return sorted(dictwait)
