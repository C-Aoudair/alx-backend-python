#!/usr/bin/env python3
""" Unit tests for client module units."""

from client import GithubOrgClient
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class

import fixtures
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """Unit test for client.GithubOrgClient class"""

    @parameterized.expand([("google"), ("abc")])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
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

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        mock_payload = [
            {'id': 1, 'name': 'project1'},
            {'id': 2, 'name': 'project2'},
            {'id': 3, 'name': 'project3'}
        ]
        mock_get_json.return_value = mock_payload

        with patch.object(
            GithubOrgClient, '_public_repos_url', new_callable=PropertyMock
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = 'github/repos'

            result = GithubOrgClient('org_name').public_repos()
            expected_result = ['project1', 'project2', 'project3']

            self.assertEqual(result, expected_result)
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, license, license_key, expected_result):
        result = GithubOrgClient.has_license(license, license_key)
        self.assertEqual(result, expected_result)


@parameterized_class([
    {"org_payload": fixtures.org_payload, "repos_payload": fixtures.repos_payload,
     "expected_repos": fixtures.expected_repos, "apache2_repos": fixtures.apache2_repos}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for GithubOrgClient.public_repos"""

    @classmethod
    def setUpClass(cls):
        """Set up class method to patch requests.get"""
        cls.get_patcher = patch('requests.get', side_effect=cls.mocked_requests_get)
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Tear down class method to stop the patcher"""
        cls.get_patcher.stop()

    @staticmethod
    def mocked_requests_get(url, *args, **kwargs):
        """Mock requests.get to return the appropriate fixture based on URL"""
        if "orgs" in url:
            return Mock(json=lambda: fixtures.org_payload)
        if "repos" in url:
            return Mock(json=lambda: fixtures.repos_payload)
        return Mock(json=lambda: None)

    def test_public_repos(self):
        """Test public_repos method"""
        client = GithubOrgClient("test_org")
        self.assertEqual(client.public_repos(), self.expected_repos)
        self.assertEqual(client.public_repos("apache-2.0"), self.apache2_repos)


class TestGithubOrgClient(unittest.TestCase):
    """ integration test """
    @patch.object(GithubOrgClient, 'org', return_value=org_payload)
    @patch.object(GithubOrgClient, 'repos_payload', return_value=repos_payload)
    def test_public_repos(self, mock_repos_payload, mock_org):
        client = GithubOrgClient("google")
        result = client.public_repos()
        self.assertEqual(result, expected_repos)

    @patch.object(GithubOrgClient, 'org', return_value=org_payload)
    @patch.object(GithubOrgClient, 'repos_payload', return_value=repos_payload)
    def test_public_repos_with_license(self, mock_repos_payload, mock_org):
        client = GithubOrgClient("google")
        result = client.public_repos(license="apache-2.0")
        self.assertEqual(result, apache2_repos)
