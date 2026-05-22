#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N)
from the database specified by args.
"""
import MySQLdb
import sys

if __name__ == '__main__':
    # Get arguments: username, password, db name
    uname, pwd, db = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL server
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=uname,
        passwd=pwd,
        db=db
    )
    cur = conn.cursor()
    # Execute query to filter states starting with 'N', sorted by id
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
