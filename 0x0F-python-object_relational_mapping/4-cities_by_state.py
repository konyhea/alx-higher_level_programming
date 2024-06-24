#!/usr/bin/python3

'''
List all cities from the database hbtn_0e_4_usa
'''

import MySQLdb
import sys


def main():
    '''Get arguments from command line'''
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    '''Connect to database'''
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    '''Create cursor'''
    cur = db.cursor()

    '''Query to select all cities'''
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        INNER JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """

    '''Execute query'''
    cur.execute(query)

    '''Fetch and print results'''
    for city in cur.fetchall():
        print(city)

    '''Close database connection'''
    db.close()


if __name__ == "__main__":
    main()
