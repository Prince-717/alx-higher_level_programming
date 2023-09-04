#!/usr/bin/python3
""" Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
The email must be sent in the variable email
packages requests and sys """
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    values = {"email": argv[2]}

    _req = requests.post(url, values)
    print(_req.text)
