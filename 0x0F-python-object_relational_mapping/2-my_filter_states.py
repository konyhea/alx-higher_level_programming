#!/usr/bin/python3

'''Selecting from a SQL db'''

import MySQLdb
import sys


def main():
    '''Get command-line arguments'''
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    '''Connect to the database'''
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    '''Create a cursor'''
    cur = db.cursor()

    '''Execute a query with a parameter'''
    query = "SELECT * FROM states WHERE BINARY name = '{}'\
        ORDER BY id ASC".format(state_name)
    cur.execute(query)

    '''Fetch and print the results'''
    for state in cur.fetchall():
        print(state)

    '''Close the database connection'''
    db.close()


if __name__ == "__main__":
    main()
