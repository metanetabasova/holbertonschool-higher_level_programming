#!/usr/bin/python3
"""
Bu skript hbtn_0e_0_usa verilənlər bazasından adı 'N' hərfi ilə
başlayan bütün ştatları ştatın ID-sinə görə artan sırada sıralayaraq siyahılayır.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Əmr sətrindən arqumentlərin götürülməsi
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # MySQL serverinə qoşulma
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Sorğuları icra etmək üçün kursorun (cursor) yaradılması
    cursor = db.cursor()

    # SQL sorğusunun hazırlanması və icra edilməsi
    # BINARY istifadə etməklə 'N' hərfinin böyük hərf olmasına tam əmin oluruq
    query = """
        SELECT id, name 
        FROM states 
        WHERE name LIKE BINARY 'N%' 
        ORDER BY id ASC
    """
    cursor.execute(query)

    # Bütün nəticələrin əldə edilməsi
    rows = cursor.fetchall()

    # Nəticələrin tələb olunan formatda ekrana çıxarılması
    for row in rows:
        print(row)

    # Kursorun və verilənlər bazası əlaqəsinin bağlanması
    cursor.close()
    db.close()
