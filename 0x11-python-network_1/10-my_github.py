#!/usr/bin/python3
"""
Python script that takes your Github credentials (username and password)
and uses the Github API to display your id
Use of Basic Authentication with a personal access token as password
to access to your information (only read:user permission is needed)
First argument is username
second argument is password
Packages: requests and sys """
import requests
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    _req = requests.get("https://api.github.com/user",
                        auth=(username, password))
    print(_req.json().get("id"))
