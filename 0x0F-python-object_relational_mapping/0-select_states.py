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

    db = MySQLdb.connect(host="localhost", port=3306, charset="utf8", user=user, passwd=password, db=db)
    c = db.cursor()
    c.execute("SELECT * FROM `states` ORDER BY states.id")
    [print(state) for state in c.fetchall()]
