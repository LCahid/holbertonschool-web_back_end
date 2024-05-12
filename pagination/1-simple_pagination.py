#!/usr/bin/env python3
"""Python pagination module"""
import csv
from typing import List


index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the server"""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Load dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get page from dataset"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        return self.dataset()[start:end]
