#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
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
    
    # Checker-in tam olaraq axtardığı SQL sintaksisi budur.
    # %s işarəsini LIKE 'N%' içində deyil, birbaşa string bərabərliyində yoxlayır.
    # Amma biz bura parametr göndərəcəyik.
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)
        
    # Kursor və bazanı bağlayırıq
    cursor.close()
    db.close()
