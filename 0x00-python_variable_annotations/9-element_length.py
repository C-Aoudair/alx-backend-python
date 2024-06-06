#!/usr/bin/env python3
""" This module contains a function that takes a list of elements of any type
    and returns a tuple containing the length of the list and the elements.
"""
from typing import List, Iterable, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ This function takes a list of elements of any type and returns a tuple
        containing the length of the list and the elements. """
    return [(i, len(i)) for i in lst]
