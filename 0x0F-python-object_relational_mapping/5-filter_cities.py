#!/usr/bin/python3

"""
This script lists all cities and their states from MySQL database

Usage : ./4-cities_by_state.py <username> <password> <database>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

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
    SQL query to select all cities from the table
    """
    sql = """SELECT cities.name FROM cities \
            INNER JOIN states ON cities.state_id = states.id \
            WHERE states.name = %s \
            ORDER BY cities.id ASC"""

    cursor.execute(sql, (state_name,))

    """
    fetching all the results
    """
    myresult = cursor.fetchall()

    """
    Printing the results
    """
    for row in myresult:
        print(row)
