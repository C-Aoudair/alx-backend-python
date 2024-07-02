org_payload = {
    "repos_url": "https://api.github.com/orgs/google/repos",
    "name": "Google",
    "description": "A multinational technology company specializing in Internet-related services and products.",
    "public_repos": 1500,
}

repos_payload = [
    {
        "id": 7697149,
        "node_id": "MDEwOlJlcG9zaXRvcnk3Njk3MTQ5",
        "name": "episodes.dart",
        "full_name": "google/episodes.dart",
        "private": False,
        "html_url": "https://github.com/google/episodes.dart",
        "description": "A framework for timing performance of web apps.",
        "fork": False,
    },
]

expected_repos = ["episodes.dart"]
apache2_repos = []
