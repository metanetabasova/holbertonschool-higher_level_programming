#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa.

Usage: ./5-filter_cities.py <mysql_username> <mysql_password> <database_name> <state_name>
"""
import sys
import MySQLdb


def main():
    if len(sys.argv) != 5:
        return

    username, password, dbname, state_name = sys.argv[1:5]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname
    )
    cur = db.cursor()

    # One execute() call, parameterized (SQL injection safe)
    cur.execute(
        """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """,
        (state_name,)
    )

    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
