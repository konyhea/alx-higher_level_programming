#!/usr/bin/python3
'''import modules'''
import requests
from sys import argv


def main():
    '''fetches GitHub user id using GitHub API'''
    username = argv[1]
    password = argv[2]
    url = f'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))
    if response.status_code == 200:
        user_info = response.json()
        user_id = user_info['id']
        print(user_id)
    else:
        return None


if __name__ == "__main__":
    main()
