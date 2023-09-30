#!/usr/bin/python3
"""Python script that fetches github"""
import requests
import sys


headers = {
    'Authorization': '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',
    'Accept': 'application/vnd.github.v3+json',
}
username = 'Abodawoud'
url = f'https://api.github.com/users/{username}'


response = requests.get(url, headers=headers)
print(response.json()["id"])
