#!/usr/bin/env python3
""" Unit tests for client module units."""

from client import GithubOrgClient
from unittest.mock import patch, PropertyMock
from parameterized import parameterized

import unittest


class TestGithubOrgClient(unittest.TestCase):
    """Unit test for client.GithubOrgClient class"""

    @parameterized.expand([("case1", "google"), ("case2", "abc")])
    @patch("client.get_json")
    def test_org(self, name, org_name, mock_get_json):
        mock_response = {"name": org_name}
        mock_get_json.return_value = mock_response
        result = GithubOrgClient(org_name).org

        self.assertEqual(result, mock_response)
        url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(url)

    def test_puplic_repos_url(self):
        with patch.object(
            GithubOrgClient, "org", new_callable=PropertyMock
        ) as mock_org:
            mock_payload = {"repos_url": "github/org/repos"}
            mock_org.return_value = mock_payload
            result = GithubOrgClient("org_name")._public_repos_url

            self.assertEqual(result, mock_payload["repos_url"])
            mock_org.assert_called_once()
