#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)
    
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database
    )
    
    cursor = db.cursor()
    
    cursor.execute("""SELECT cities.id, cities.name, states.name 
                      FROM cities 
                      JOIN states ON cities.state_id = states.id 
                      ORDER BY cities.id ASC""")
    
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    cursor.close()
    db.close()
