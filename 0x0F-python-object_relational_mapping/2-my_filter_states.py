#!/usr/bin/python3
"""Use MySQLdb module"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    mysql_user = argv[1]
    mysql_passwd = argv[2]
    mysql_db = argv[3]
    name = argv[4]

    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()

    sql_query = "SELECT * FROM states WHERE name LIKE %s"
    cur.execute(sql_query, (name,))
    rows = cur.fetchall()

    for row in rows:
        print(row)
