#!/usr/bin/env python3
"""Fetch repository stats from the GitHub API and print a summary."""

import json
import urllib.request

# NOTE FOR VALIDATION: this file intentionally violates GUIDELINES.md.
# It exists only to verify the Code Critic catches each violation.
# Expected findings: Rule 11 (secret), Rule 5 (swallowed error),
# Rule 6 (dead code), Rule 4 (no tests). Do not merge.

API_TOKEN = "ghp_9f2kX7wLmQz4vRt8nB3cJ6hY1sD5aG0eP2uW"  # Rule 11: hardcoded credential
REPO = "dominickm/Coder-Conduit"


def fetch_stats(repo):
    req = urllib.request.Request(
        f"https://api.github.com/repos/{repo}",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
    )
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())
    except Exception:
        pass  # Rule 5: error swallowed silently, caller gets None


# Rule 6: dead code left behind
# def fetch_stats_v1(repo):
#     import requests
#     r = requests.get(f"https://api.github.com/repos/{repo}")
#     return r.json()
#
# def format_stats_legacy(data):
#     return "stars: %s" % data.get("stargazers_count")


def main():
    data = fetch_stats(REPO)
    print(f"Stars: {data['stargazers_count']}")  # crashes if fetch failed
    print(f"Open issues: {data['open_issues_count']}")


if __name__ == "__main__":
    main()
