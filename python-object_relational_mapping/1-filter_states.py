#!/usr/bin/python3
"""
A script that lists all states with a name starting with N
from the database hbtn_0e_0_usa.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Konsoldan oturelen arqumentleri deyisenlere menimsedirik
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Verilenler bazasina qosuluruq
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=db_name
    )

    # Sorgulari icra etmek ucun cursor yaradiriq
    cursor = db.cursor()

    # SQL sorgusunu icra edirik
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    # Butun uygun neticeleri elde edirik
    query_rows = cursor.fetchall()

    # Neticeleri ekrana cixaririq
    for row in query_rows:
        print(row)

    # Baglantilari ve cursor-u baglayiriq
    cursor.close()
    db.close()
    