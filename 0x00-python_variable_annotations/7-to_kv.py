#!/usr/bin/env python3
"""returns tuple"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns tuple representation"""
    return k, (v**2)
