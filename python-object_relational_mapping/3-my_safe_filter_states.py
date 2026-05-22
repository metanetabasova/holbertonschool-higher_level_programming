#!/usr/bin/python3
"""
This module connects to a MySQL database and displays all values
in the states table of hbtn_0e_0_usa where the name matches the argument.
This script is strictly safe from MySQL injections.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Verilənlər bazasına qoşulma
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()

    # SQL Injection-ın qarşısını almaq üçün %s yer tutucusundan istifadə edirik.
    # Dəyəri dırnaq daxilində deyil, execute metoduna tuple olaraq ötürürük.
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    cursor.execute(query, (sys.argv[4],))

    # Nəticələrin əldə edilməsi və çapı
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Kursor və bazanın bağlanması
    cursor.close()
    db.close()
