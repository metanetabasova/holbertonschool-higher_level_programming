#!/usr/bin/env python3
"""Module that returns a tuple with a squared value."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with k and v squared."""
    return (k, float(v ** 2))
