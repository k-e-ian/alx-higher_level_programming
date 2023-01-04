#!/usr/bin/python3
'''
Lists all states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql username> \
                             <mysql password> \
                             <database name>
'''
import sys
import MySQLdb

if __name__ == "__main__":
    '''not executed when imported'''
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=user,
                           passwd=password, db=db, charset="utf8")
    session = conn.cursor()

    session.execute('SELECT * FROM states ORDER BY states.id')

    states = session.fetchall()

    for state in states:
        print(state)

    session.close()
    conn.close()i
