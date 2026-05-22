#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Check arguments
    if len(sys.argv) != 4:
        sys.exit(1)
    
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database,
            port=3306
        )
        
        # Create cursor
        cursor = db.cursor()
        
        # Execute single query with JOIN to get cities with state names
        query = """
        SELECT cities.id, cities.name, states.name 
        FROM cities 
        JOIN states ON cities.state_id = states.id 
        ORDER BY cities.id ASC
        """
        cursor.execute(query)
        
        # Fetch and display all results
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        
        # Close cursor and connection
        cursor.close()
        db.close()
        
    except MySQLdb.Error as e:
        print(f"Error: {e}")
        sys.exit(1)