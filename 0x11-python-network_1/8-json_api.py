#!/usr/bin/python3
"""Search API"""
import requests
import sys

if __name__ == "__main__":
    def posting(arg=""):
        url = "http://0.0.0.0:5000/search_user"
        values = {"q": arg}
        response = requests.post(url, values)

        try:
            json_o = response.json()
            if not json_o:
                print("No result")
            else:
                print("[{}] {}".format(json_o.get('id'), json_o.get('name')))
        except:
            print("Not a valid JSON")
    posting(sys.argv[1])
