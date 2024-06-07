#!/usr/bin/env python3
""" This module contains a function that takes a string and an int or float and
    returns a tuple containing the string and the square of the int or float.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ This function takes a string and an int or float and returns a tuple
        containing the string and the square of the int or float. """
    return (k, v * v)
