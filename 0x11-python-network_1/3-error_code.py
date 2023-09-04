#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8) """
from urllib.error import HTTPError
from urllib.request import urlopen
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urlopen(url) as response:
            print(response.read().decode())
    except HTTPError as r:
        print("Error code: {}".format(r.code))
