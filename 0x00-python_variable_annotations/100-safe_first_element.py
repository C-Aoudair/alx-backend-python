#!/usr/bin/env python3
""" This module contains a function that takes an argument as a sequence
    and return its slice or null
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Takes an argument as sequence and return any type or None"""
    if lst:
        return lst[0]
    else:
        return None
    