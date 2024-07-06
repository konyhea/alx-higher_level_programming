#!/usr/bin/python3
'''import modules'''
import urllib.request


def main():
    '''script that fetches'''
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        html = resp.read()
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode('utf-8')))


if __name__ == "__main__":
    main()
