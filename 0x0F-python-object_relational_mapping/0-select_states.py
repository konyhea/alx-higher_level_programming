#!/usr/bin/python3

'''
list all states from the db hbtn_0e_0_usa:
'''
import MySQLdb
import sys


def main():
    '''Selecting from a SQL db'''
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    '''Connecting to the database'''
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    '''Creating a cursor'''
    cur = db.cursor()

    '''The query for collecting from the SQL db'''
    query = "SELECT * FROM states ORDER BY states.id ASC"
    cur.execute(query)

    '''Fetching and printing the results'''
    for state in cur.fetchall():
        print(state)

    '''Closing the database connection'''
    db.close()


if __name__ == "__main__":
    main()
