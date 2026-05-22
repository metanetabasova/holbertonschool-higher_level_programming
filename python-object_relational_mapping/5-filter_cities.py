#!/usr/bin/python3
"""
Lists all cities of a state given as argument (safe from SQL injection).
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username, password, db_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )
    cur = db.cursor()

    # Yalnız bir sorğu, JOIN ilə
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cur.execute(query, (state_name,))

    rows = cur.fetchall()
    # Çıxış: şəhər adlarını vergüllə ayırıb bir sətrdə çap et
    print(", ".join([row[0] for row in rows]))

    cur.close()
    db.close()
