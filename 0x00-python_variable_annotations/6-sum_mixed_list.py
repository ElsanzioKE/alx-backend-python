#!/usr/bin/env python3
"""annotated function"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns sum of mixedlist"""
    return sum(mxd_lst)
