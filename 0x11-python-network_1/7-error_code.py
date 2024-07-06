#!/usr/bin/python3
'''import modules'''
import requests
from sys import argv


def main():
    '''send request to a URL with a status code if found'''
    url = argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print(f'Error code: {r.status_code}')
    else:
        print(r.text)


if __name__ == "__main__":
    main()
