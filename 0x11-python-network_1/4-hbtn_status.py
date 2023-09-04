#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status
only with requests package """
import requests

html = requests.get("https://intranet.hbtn.io/status")
print("Body response:\n\t- type: {}\n\t- content: {}\
".format(html.text.__class__, html.text))
