#!/usr/bin/python3
'''
This module connects to a MySQL database and displays all values
in the states table of hbtn_0e_0_usa where the name matches the argument.
It takes 4 arguments: username, password, database name, and state name.
'''
import sys
import MySQLdb

if __name__ == "__main__":
    # Verilenler bazasina qosulma
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()

    # Tapsirigin telebine esasen istifadeci inputunu fotmat ile sorguya daxil edirik
    # Statin adini deqiq yoxlamaq ucun Binary istifade olunur
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC"
    cursor.execute(query.format(sys.argv[4]))

    # Neticelerin elde edilmesi ve capi
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Kursor ve bazanin baglanmasi
    cursor.close()
    db.close()
