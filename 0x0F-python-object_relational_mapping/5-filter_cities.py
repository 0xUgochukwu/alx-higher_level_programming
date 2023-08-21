#!/usr/bin/python3
"""
This module runs a script to fetch all cities table
in the database provided along with the state name
equal to the state provided
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT c.name from cities c JOIN states s on \
                 c.state_id = s.id WHERE s.name = %s", (argv[4],))
    cities = cur.fetchall()
    print(", ".join(city[0] for city in cities))
    cur.close()
    db.close()
