#!/usr/bin/env python3
""" Contains unit tests for utils.access_nested_map function"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Implement unit tests for test_access_nested_map funtion"""

    @parameterized.expand(
        [
            ("case1", {"a": 1}, ("a",), 1),
            ("case2", {"a": {"b": 2}}, ("a",), {"b": 2}),
            ("case3", {"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, name, a, b, expected):
        """ test access_nested_map function"""
        self.assertEqual(access_nested_map(a, b), expected)

    @parameterized.expand(
        [
            ("case1", {}, ("a",)),
            ("case2", {"a": 1}, ("a", "b")),
        ]
    )
    def test_access_nested_map_exception(self, name, a, b):
        """ test case"""
        with self.assertRaises(KeyError):
            access_nested_map(a, b)


class TestGetJson(unittest.TestCase):
    """Test the utils.get_json function."""

    @parameterized.expand(
        [
            ("case1", "http://example.com", {"payload": True}),
            ("case2", "http://holberton.io", {"payload": False}),
        ]
    )
    @patch('requests.get')
    def test_get_json(self, name, url, payload, mock_get):
        """ test case"""
        mock_response = payload
        mock_get.return_value.json.return_value = mock_response

        result = get_json(url)
        self.assertEqual(result, mock_response)
        mock_get.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """ Test the utils.momoize function."""
    class TestClass:

        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    @patch.object(TestClass, 'a_method')
    def test_memoize(self, mock_method):
        """ test case"""
        mock_response = 42
        mock_method.return_value = mock_response

        result = self.TestClass().a_property
        self.assertEqual(result, mock_response)
        mock_method.assert_called_once()
