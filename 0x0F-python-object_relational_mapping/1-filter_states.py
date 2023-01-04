#!/usr/bin/python3
'''
# Lists all states with a name starting with N from the database hbtn_0e_0_usa.
# Usage: ./1-filter_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
'''
from sys import argv
import MySQLdb

if __name__ == "__main__":
    user = argv[1]
    password = argv[2]
    db = argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=user,
                           passwd=password, db=db, charset="utf8")
    session = conn.cursor()

    session.execute("""SELECT * FROM states WHERE name LIKE BINARY "N%" ORDER
            BY states.id""")
    states = session.fetchall()

    for state in states:
        print(state)

    session.close()
    conn.close()
