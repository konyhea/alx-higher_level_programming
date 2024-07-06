#!/usr/bin/python3
'''import modules'''
from urllib import request, parse
from sys import argv


def main():
    '''sends POST request to a URL with email as parameter'''
    url = argv[1]
    email = argv[2]
    data = parse.urlencode({'email': email}).encode('utf-8')
    req = request.Request(url, data=data, method='POST')
    with request.urlopen(req) as response:
        response_body = response.read().decode('utf-8')
    print(response_body)


if __name__ == "__main__":
    main()
