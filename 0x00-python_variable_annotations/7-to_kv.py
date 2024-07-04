#!/usr/bin/env python3
"""annotated function"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """takes str and integer or float and returns a tuple"""
    sqr = float(v * v)
    return (k, sqr)
