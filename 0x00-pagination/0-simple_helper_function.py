#!/usr/bin/env python3
"""
Simple helper function for pagination.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of start and end index for pagination.

    Args:
        page (int): Page number (1-indexed).
        page_size (int): Number of items per page.

    Returns:
        tuple: (start_index, end_index)
    """
    start = (page - 1) * page_size
    end = page * page_size
    return start, end
