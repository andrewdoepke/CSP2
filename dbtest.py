import sqlite3 as sql

try:
    with sql.connect("static/database/database.db") as conn:
        curr = conn.cursor()
        conn.row_factory = sql.Row

        curr.execute("SELECT * FROM blogs;")
        hi = curr.fetchall()
        print(list(hi).__getitem__(0))
except:
    print("OH No")
finally:
    conn.close()



