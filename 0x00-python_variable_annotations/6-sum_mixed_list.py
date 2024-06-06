#!/usr/bin/env python3
""" This module contains a function that takes a list of floats and integers
    and returns their sum as a float. """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ This function takes a list of floats and integers and returns their sum
        as a float. """
    return sum(mxd_lst)
