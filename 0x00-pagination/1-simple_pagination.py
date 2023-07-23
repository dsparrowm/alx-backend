#!/usr/bin/env python3
"""Write a function named index_range that takes two integer
   arguments page and page_size.
   The function should return a tuple of size two containing
   a start index and an end index corresponding to the range
   of indexes to return in a list for those particular
   pagination parameters.
   Page numbers are 1-indexed, i.e. the first page is page 1.
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """Helper function that returns start and end index"""
    if page <= 0 or page_size <= 0:
        raise ValueError("Both page and page_size must be positive ints")
    start = (page - 1) * page_size
    end = start + page_size
    return start, end


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """return the proper page of the data"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        data = self.dataset()
        try:
            start, end = index_range(page, page_size)
            return data[start:end]
        except IndexError:
            return []
