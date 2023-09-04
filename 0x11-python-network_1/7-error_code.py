#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL and displays
the body of the response.
If the HTTP status code is greater than or equal to 400,
print: Error code: followed by the value of the HTTP status code
packages requests and sys """
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    _req = requests.get(argv[1])
    if _req.status_code <= 400:
        print(_req.text)
    else:
        print("Error code: {}".format(_req.status_code))
