#!/usr/bin/python3
"""
Lists all values where name matches the argument, safe from MySQL injection.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    uname, pwd, db, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=uname,
        passwd=pwd,
        db=db
    )
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
