#!/usr/bin/env python3
'''Python - Variable Annotations'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Callable'''
    def func(n: float) -> float:
        '''func'''
        return n * multiplier
    return func
