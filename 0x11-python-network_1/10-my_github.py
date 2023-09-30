#!/usr/bin/python3
"""Python script that fetches github"""
import requests
import sys


if __name__ == "__main__":
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"Bearer {sys.argv[2]}",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    url = f'https://api.github.com/user'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        user_data = response.json()
        print(user_data["id"])
    else:
        print("None")
