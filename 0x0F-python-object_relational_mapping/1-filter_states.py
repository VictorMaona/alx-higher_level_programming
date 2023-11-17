#!/usr/bin/python3
"""  Establish connection to database and verify the number """

import MySQLdb
import sys

if __name__ == "__main__":
    # Verify that right amount of command line parameters is supplied.
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Convert command line parameters
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        # Link up with the database.
        db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database, port=3306)

        # Make object with cursor to communicate with the database.
        cursor = db.cursor()

        # Run database query to choose the states whose names begin 'N'
        query = 
        cursor.execute(query)

        # Retrieve every row.
        rows = cursor.fetchall()

        # Print each row state individually.
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        # Address database issues
        print("MySQL Error: {}".format(e))

    except Exception as e:
        # Address further exclusions
        print("Error: {}".format(e))

    finally:
        # Free resources end the database connection and cursor.
        if cursor:
            cursor.close()
        if db:
            db.close()
