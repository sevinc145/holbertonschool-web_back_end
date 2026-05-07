#!/usr/bin/env python3
''' 0-simple_helper_function.py pagination '''


def index_range(page, page_size):
    """
    Calculate the start and end indexes for pagination.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
