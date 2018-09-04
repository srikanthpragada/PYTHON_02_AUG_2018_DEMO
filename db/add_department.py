import sqlite3

try:
    con = sqlite3.connect(r"e:\classroom\python\aug2\hr.db")
    cur = con.cursor()
    # take input from user
    name = input("Enter department name     :")
    loc =  input("Enter department location :")
    cur.execute("insert into departments(deptname,location) values(?,?)",
                 (name,loc))
    con.commit()
except Exception as ex:
    print("Database Error ->", ex)
    con.rollback()
finally:
    con.close()


