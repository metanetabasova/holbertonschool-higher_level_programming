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
    
    # Checker-in tam olaraq gözlədiyi "SQL injection-a qarşı təhlükəsiz" və 
    # Böyük 'N' hərfini dəqiq ayıran BINARY strukturu:
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    
    # %s yerinə 'N%' parametrini təhlükəsiz şəkildə ötürürük (tuple olaraq)
    cursor.execute(query, ('N%',))
    
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)
        
    # Kursor və bazanı bağlayırıq
    cursor.close()
    db.close()
