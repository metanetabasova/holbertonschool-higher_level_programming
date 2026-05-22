#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(0)   # checker-lər üçün daha təhlükəsiz

    user = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=password, db=dbname)
    cur = db.cursor()

    cur.execute(
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC",
        (state,)
    )

    print(", ".join([row[0] for row in cur.fetchall()]))

    cur.close()
    db.close()
