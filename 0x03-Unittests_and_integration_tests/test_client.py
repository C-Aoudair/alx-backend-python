#!/usr/bin/env python3
""" Unit tests for client module units."""

from client import GithubOrgClient
from unittest.mock import patch
from parameterized import parameterized

import unittest


class TestGithubOrgClient(unittest.TestCase):
    """ Unit test for client.GithubOrgClient class"""

    @parameterized.expand([('case1', 'google'), ('case2', 'abc')])
    @patch('client.get_json')
    def test_org(self, name, org_name, mock_get_json):
        mock_response = {"name": org_name}
        mock_get_json.return_value = mock_response
        result = GithubOrgClient(org_name).org

        self.assertEqual(result, mock_response)
        url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(url)
