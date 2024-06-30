#!/usr/bin/env python3
""" Contains unit tests for utils.access_nested_map function"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Implement unit tests for test_access_nested_map funtion"""

    @parameterized.expand([
        ("case1", {"a": 1}, ("a",), 1),
        ("case2", {"a": {"b": 2}}, ("a",), {"b": 2}),
        ("case3", {"a": {"b": 2}}, ("a", "b"), 2)
    ])

    def test_access_nested_map(self, name, a, b, expected):
        self.assertEqual(access_nested_map(a, b), expected)

