#!/usr/bin/env python3
"""Import module for helper function."""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Function takes two int args (page & page_size) and
    returns a tuple of size 2 containing start index
    and end index.
    """
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    return (start_idx, end_idx)
