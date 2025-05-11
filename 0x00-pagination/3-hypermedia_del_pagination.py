#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination.
"""

import csv
from typing import List, Dict, Optional
Server = __import__('1-simple_pagination').Server


class DeletionResilientServer(Server):
    """Server class that paginates data and handles deletion resilience."""

    def __init__(self):
        super().__init__()
        self.__indexed_dataset = None

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Returns dataset indexed by original position
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: Optional[int] = None,
                        page_size: int = 10) -> Dict:
        """
        Returns a page of data and next index, skipping deleted entries.

        Args:
            index (int): start index
            page_size (int): number of items to return

        Returns:
            Dict: contains index, next_index, page_size, data
        """
        assert isinstance(index, int)
        assert isinstance(page_size, int)
        assert 0 <= index < len(self.indexed_dataset())

        data = []
        current_index = index
        count = 0
        indexed_data = self.indexed_dataset()
        max_index = max(indexed_data.keys())

        while count < page_size and current_index <= max_index:
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
                count += 1
            current_index += 1

        return {
            "index": index,
            "next_index": current_index,
            "page_size": len(data),
            "data": data
        }
