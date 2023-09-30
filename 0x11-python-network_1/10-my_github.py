#!/usr/bin/python3
"""Python script that fetches github"""
import requests
import sys


headers = {
    'Authorization': sys.argv[2],
    'Accept': 'application/vnd.github.v3+json',
}
url = f'https://api.github.com/users/{sys.argv[1]}'


response = requests.get(url, headers=headers)
print(response.json()["id"])
