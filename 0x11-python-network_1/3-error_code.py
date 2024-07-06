#!/usr/bin/python3
'''import modules'''
from urllib import request, error
from sys import argv


def main():
    '''sends requests to a url'''
    req = request.Request(argv[1])
    try:
        with request.urlopen(req) as response:
            response_body = response.read().decode('utf-8')
            print(response_body)
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
    except error.URLError as e:
        print(f"Error: {e.reason}")


if __name__ == "__main__":
    main()
