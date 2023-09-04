#!/usr/bin/python3
""" Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the body
of the response (decoded in utf-8) """
from urllib import request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    values = {"email": argv[2]}

    data = urllib.parse.urlencode(values)
    data = data.encode()
    _request = urllib.request.Request(url, data)
    with urllib.request.urlopen(_request) as response:
        _page = response.read()
        print(_page.decode())
