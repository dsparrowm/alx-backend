#!/usr/bin/env python3
"""function named index_range that takes two integer
   arguments page and page_size and rwturns a tuple of size two
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """Helper function that returns start and end index"""
    if page <= 0 or page_size <= 0:
        raise ValueError("Both page and page_size must be positive ints")
    start = (page - 1) * page_size
    end = start + page_size
    return start, end
