#!/usr/bin/python3
"""
MySQL verilənlər bazasından (hbtn_0e_0_usa) adı 'N' hərfi ilə
başlayan bütün ştatları id-yə görə artan sırada siyahılayan skript.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Konsoldan ötürülən arqumentləri dəyişənlərə mənimsədirik
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Verilənlər bazasına qoşuluruq (localhost, port 3306)
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=db_name
    )

    # Sorğuları icra etmək üçün cursor (göstərici) yaradırıq
    cursor = db.cursor()

    # SQL sorğusunu icra edirik (Yalnız adı 'N' ilə başlayanlar və id-yə görə ASC sıralama)
    # MySQL-də LIKE operatoru böyük/kiçik hərfə həssas (case-insensitive) ola bilər,
    # lakin tapşırıq binary və ya birbaşa 'N%' tələb etdiyi üçün bu format tam doğrudur.
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    # Bütün uyğun nəticələri əldə edirik
    query_rows = cursor.fetchall()

    # Nəticələri ekrana çıxarırıq
    for row in query_rows:
        print(row)

    # Bağlantıları və cursor-u bağlayırıq
    cursor.close()
    db.close()
