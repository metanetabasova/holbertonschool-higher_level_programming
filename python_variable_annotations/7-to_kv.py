#!/usr/bin/env python3
"""This module provides a function that returns a tuple with a squared value."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple where the first element is k and the second is v squared."""
    return (k, float(v ** 2))
