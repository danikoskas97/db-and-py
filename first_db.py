# coding:utf-8
import sqlite3

try:
    connect = sqlite3.connect("first-db.db")
    cursor = connect.cursor()
    # new_user = [(1, "jason", 15), (2,'marc', 12)] can be done with tuple in list
    # -----------------------------
    # adding a new user
    # new_user = (cursor.lastrowid, "julie", 23)
    # cursor.execute("INSERT INTO tt_users VALUES(?,?,?)", new_user)
    # commit changes
    # todo only if we do changes in the db
    # connect.commit()
    # -----------------------------
    select_all = cursor.execute('SELECT * FROM tt_users')
    for row in select_all.fetchall():
        print(row[1])

except Exception as e:
    print("[Error]", e)
    connect.rollback()

finally:
    connect.close()










