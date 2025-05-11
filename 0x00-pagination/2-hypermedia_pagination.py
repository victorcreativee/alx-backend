#!/usr/bin/env python3
"""
Hypermedia pagination.
"""

import math
from typing import Dict, List
Server = __import__('1-simple_pagination').Server


class ServerWithHyper(Server):
    """Extends Server to add hypermedia pagination metadata"""

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Returns hypermedia-style pagination data

        Args:
            page (int): current page number
            page_size (int): number of items per page

        Returns:
            Dict: contains page, page_size, data,
            next_page, prev_page, total_pages
        """
        data_page = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        return {
            'page_size': len(data_page),
            'page': page,
            'data': data_page,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
