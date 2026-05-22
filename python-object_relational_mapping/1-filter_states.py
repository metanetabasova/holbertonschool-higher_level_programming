#!/usr/bin/python3
"""
Bu skript hbtn_0e_0_usa verilənlər bazasından adı 'N' hərfi ilə
başlayan bütün ştatları təhlükəsiz şəkildə siyahılayır.
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

    cursor = db.cursor()

    # ÇOX VACİB: Sorğunu parametrləşdirilmiş (Safe from SQL injection) edirik.
    # %s Python-un formatlaması deyil, MySQLdb-nin parametr yer tutucusudur.
    query = """
        SELECT id, name 
        FROM states 
        WHERE name LIKE BINARY %s 
        ORDER BY id ASC
    """
    
    # Arqumenti tuple (korfej) şəklində execute funksiyasına ötürürük
    cursor.execute(query, ('N%',))

    # Nəticələrin əldə edilməsi və çapı
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Bağlanışlar
    cursor.close()
    db.close()
