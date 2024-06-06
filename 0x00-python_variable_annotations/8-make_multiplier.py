#!/usr/bin/env python3
""" This module contains a function that takes a float and returns a function
    that multiplies a float by the original float. """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ This function takes a float and returns a function that multiplies a
        float by the original float. """
    def multiply(n: float) -> float:
        """ This function multiplies a float by the original float. """
        return n * multiplier
    return multiply
