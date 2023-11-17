#!/usr/bin/python3
""" 
Connect to the MySQL database and retrieve states.
Display states with names starting with 'N' (case-sensitive).
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    
    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute the SQL query to select states with names starting
    # with 'N' in a case-sensitive manner, and order the results
    # by the 'id' field in ascending order
    cur.execute("""
        SELECT * FROM states
        WHERE name LIKE BINARY 'N%'
        ORDER BY states.id
    """)

    # Fetch all the rows
    rows = cur.fetchall()

    # Print the rows (states) one by one
    for row in rows:
        print(row)

    # Close the cursor and database connection to release resources
    cur.close()
    db.close()
