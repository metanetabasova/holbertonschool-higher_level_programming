#!/usr/bin/python3
"""
Takes 4 arguments: mysql username, mysql password, database name and state name,
then lists all cities of that state from the database (SQL injection safe).

Usage:
    ./5-filter_cities.py <mysql_username> <mysql_password> <database_name> <state_name>
"""
import sys
import MySQLdb


def main():
    if len(sys.argv) != 5:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cur = db.cursor()

    # Only one execute() call, parameterized => SQL injection safe
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
