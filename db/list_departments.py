import sqlite3

try:
    con = sqlite3.connect(r"e:\classroom\python\aug2\hr.db")
    cur = con.cursor()
    cur.execute("select * from departments")
    for dept in cur.fetchall():
        print("%3d %-20s %s" % (dept[0], dept[1],dept[2]))

except Exception as ex:
    print("Database error ->", ex)
finally:
    con.close()


