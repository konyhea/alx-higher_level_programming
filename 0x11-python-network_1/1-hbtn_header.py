#!/usr/bin/python3
'''import modules'''
from urllib import request
from sys import argv


def main():
    '''sends requests to a url'''
    req = request.Request(argv[1])
    with request.urlopen(req) as response:
        x_request_id = response.getheader('X-Request-Id')
    print(x_request_id)


if __name__ == "__main__":
    main()
