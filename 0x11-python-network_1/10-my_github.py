#!/usr/bin/python3
"""Python script that fetches github"""
import requests
import sys


if __name__ == "__main__":
    headers = {
        'Authorization': f'Bearer {sys.argv[2]}',
        'X-GitHub-Api-Version': '2022-11-28',
        'Accept': 'application/vnd.github+json'
    }
    url = f'https://api.github.com/users/{sys.argv[1]}'

    response = requests.get(url, headers=headers)
    print(response)
    print(response.json().get('id'))
