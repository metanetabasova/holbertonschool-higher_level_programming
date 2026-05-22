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
    
    # Bütün ştatları id sırası ilə seçirik
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    
    rows = cursor.fetchall()
    
    # Python ilə ciddi şəkildə böyük 'N' hərfi ilə başlayanları yoxlayırıq
    for row in rows:
        if row[1][0] == 'N':
            print(row)
            
    # Bağlanışlar
    cursor.close()
    db.close()
