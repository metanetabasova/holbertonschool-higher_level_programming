#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    conn = MySQLdb.connect(
        host="localhost", port=3306,
        user=username, passwd=password, db=db_name
    )
    cur = conn.cursor()
    # Sorğu: bütün şəhərləri id-yə görə düzülmüş şəkildə əldə et
    query = "SELECT id, name, state_id FROM cities ORDER BY id ASC"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
