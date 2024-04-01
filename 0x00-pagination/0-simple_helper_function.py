#!/usr/bin/env python3
"""Task  0
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """takes two integer arguments page and page_size. and returns a tuple
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
