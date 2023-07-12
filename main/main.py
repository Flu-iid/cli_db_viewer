import sqlite3
import slp

con = sqlite3.connect("test.db")
cur = con.cursor()

p = slp.Slp(0.1, 1)
prp = p.single_line_printer
prp("hello there :)")
db_list = [str(i).strip("',()")
           for i in cur.execute("SELECT name FROM sqlite_master")]
db_name = input("enter Data Base name >")
prp(f"welcome to {db_name} db") if db_name in db_list else cur.execute(
    "CREATE TABLE todo(id, note, importancy)")


def insert_data(data: list, table):
    cur.execute(f"INSERT INTO {table} VALUES (?, ?, ?)", data)
    con.commit()
    print("Done! added: ", data)


def show_table(table):
    cur.execute(f"SELECT * FROM {table}")
    col = [i[0] for i in cur.description]
    print(col)
    for i in cur:
        print(i)


d = (1, "learn mongoDB", 2)
# insert_data(d, name)
show_table(db_name)
