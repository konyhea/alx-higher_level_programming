#!/usr/bin/python3
'''import modules'''
import requests
from sys import argv


def main():
    '''fetches with requests'''
    url = argv[1]
    r = requests.get(url)
    r = r.headers
    print(r.get('X-Request-Id'))


if __name__ == "__main__":
    main()
