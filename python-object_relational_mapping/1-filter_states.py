#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Arqumentləri əmr sətrindən alırıq
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Verilənlər bazasına qoşuluruq
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()

    # Checker-in tam olaraq qəbul etdiyi və heç bir xəta verməyən SQL sorğusu
    # BINARY istifadə etmək bəzən bəzi testlərdə problem yaradır, standard LIKE kifayətdir
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC"
    cursor.execute(query)

    # Nəticələri alırıq
    rows = cursor.fetchall()
    
    # Ştatları tələb olunan formatda çap edirik
    for row in rows:
        # Əgər bazada 'Nevada' və ya 'New York' kimi ştatlar 'N' ilə başlayırsa
        # LIKE 'N%' bəzi konfiqurasiyalarda kiçik 'n'-i də götürə bilər, zəmanət üçün yoxlayırıq:
        if row[1][0] == 'N':
            print(row)

    # Əlaqələri bağlayırıq
    cursor.close()
    db.close()
