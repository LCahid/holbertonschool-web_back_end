#!/usr/bin/env python3
'''Python - Variable Annotations'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''func func doc'''
    return [(i, len(i)) for i in lst]
