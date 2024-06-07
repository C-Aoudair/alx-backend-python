#!/usr/bin/env python3
""" This module contain a function that takes a dictionary and a key
    as arguments and return the value of the key safely."""
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(
        dct: Mapping, key: Any, default: Union[T, None] = None
        ) -> Union[Any, T]:
    """ Return the value of the key safely."""
    if key in dct:
        return dct[key]
    else:
        return default
