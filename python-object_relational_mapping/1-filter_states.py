#!/usr/bin/python3
'''
ne herbi ile baslayan butun statlari id-ye gore
artan sirada siyahilayan skript
'''
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
    