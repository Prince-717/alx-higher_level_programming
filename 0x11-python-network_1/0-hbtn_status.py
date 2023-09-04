#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status """
from urllib import request
if __name__ == "__main__":
    with request.urlopen("https://intranet.hbtn.io/status") as response:
        html = response.read()
    print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}\
".format(html.__class__, html, html.decode()))
