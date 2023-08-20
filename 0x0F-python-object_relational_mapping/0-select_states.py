#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    dataBase = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], dataBase=sys.argv[3])
    cur = dataBase.cursor()
    cur.execute("SELECT * FROM `states`")
    [print(state) for state in cur.fetchall()]
