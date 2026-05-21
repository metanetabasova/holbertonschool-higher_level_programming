#!/usr/bin/python3
'''
id-ye gore artan siralayib siyahilayan skript
'''
import sys
import MySQLdb

if __name__ == "__main__":
    # konsoldan oturulen arqumentleri deyisenkere menimsedirik
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

    # sorgularin icra etmek ucun cursor yaradiriq
    cursor = db.cursor()

    # SQL sorgusunu icra edirik
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Butun neticeleri elde edirik
    query_rows = cursor.fetchall()

    # Neticeleri teleb olunan formatda ekrana cixaririq
    for row in query_rows:
        print(row)

    # Baglantilari ve cursor-u baglayiriq
    cursor.close()
    db.close()
