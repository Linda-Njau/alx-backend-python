#!/usr/bin/env python3
"""returns callback function"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns callback function"""
    return (lambda x: multiplier*x)
