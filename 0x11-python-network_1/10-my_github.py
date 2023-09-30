#!/usr/bin/python3
"""Python script that fetches github"""
import requests
import sys


if __name__ == "__main__":
    headers = {
        'Authorization': sys.argv[2],
        'Accept': 'application/vnd.github.v3+json',
    }
    url = f'https://api.github.com/user'


    response = requests.get(url, headers=headers)
    if response.status_code >= 400:
        print("None")
    else:
        print(response.json()["id"])
