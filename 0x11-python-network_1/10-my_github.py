#!/usr/bin/python3
"""Python script that fetches github"""
import requests
import sys


if __name__ == "__main__":
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {sys.argv[2]}",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    url = f'https://api.github.com/user'

    response = requests.get(url, headers=headers)
    print(response.text)
