#!/usr/bin/python3
'''import modules'''
import requests
from sys import argv


def main():
    '''sends POST request to a URL with email as parameter'''
    url = argv[1]
    email = argv[2]
    r = requests.post(url, data={'email': email})
    print(r.text)


if __name__ == "__main__":
    main()
