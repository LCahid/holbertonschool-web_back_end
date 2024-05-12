#!/usr/bin/env python3
"""Python pagination module"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Python pagination function"""
    return ((page - 1) * page_size, page * page_size)
