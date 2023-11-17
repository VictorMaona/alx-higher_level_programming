#!/usr/bin/python3
"""Lists states with a name starting with 'N' (case-sensitive) from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Extract command-line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        # Connect to the MySQL database
        db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database, port=3306)

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Execute the SQL query to select states with names starting with 'N' (case-sensitive)
        query = """
                SELECT * FROM states
                WHERE name LIKE BINARY 'N%'
                ORDER BY states.id
                """
        cursor.execute(query)

        # Fetch all the rows
        rows = cursor.fetchall()

        # Print the rows (states) one by one
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        # Handle MySQL errors
        print("MySQL Error: {}".format(e))

    except Exception as e:
        # Handle other exceptions
        print("Error: {}".format(e))

    finally:
        # Close the cursor and database connection to release resources
        if cursor:
            cursor.close()
        if db:
            db.close()
