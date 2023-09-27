#!/usr/bin/python3

"""
This script lists all states from a MySQL database
with a name starting with N (upper N) from the database

Usage : ./1-filter_states.py <username> <password> <database>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    """
    making a connection to the MySQL server
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         password=password, db=database)

    """
    Creating a cursor object to interact with the database
    """
    cursor = db.cursor()

    """
    SQL query to select all states from the table
    """
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                   ORDER BY states.id ASC")

    """
    fetching all the results
    """
    myresult = cursor.fetchall()

    """
    Printing the results
    """

    for row in myresult:
        print(row)
