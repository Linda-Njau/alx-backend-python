#!/usr/bin/env python3
"""function for element length"""

from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns iterable length"""
    return [(i, len(i)) for i in lst]
