#!/usr/bin/python3
"""
Lists all values in the states table where name matches the argument.
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

    # tək dırnaq problemini (SQL injection və s.) önləmək üçün
    state_name = state_name.replace("'", "''")
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
