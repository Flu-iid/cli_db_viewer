import sqlite3
import slp
import showable

con = sqlite3.connect("test.db")
cur = con.cursor()

p = slp.Slp(0.1, 1)
prp = p.single_line_printer
prp("hello there :)")
db_list = [str(i).strip("',()")
           for i in cur.execute("SELECT name FROM sqlite_master")]
db_name = input("enter Data Base name >")
prp(f"welcome to {db_name} db") if db_name in db_list else cur.execute(
    f"CREATE TABLE {db_name}(id, note, importancy)")


def show_table(table):
    cur.execute(f"SELECT * FROM {table}")
    col = [i[0] for i in cur.description]
    cur.execute(f"SELECT * FROM {table}")
    sh = showable.Showable(col, [list(i) for i in cur])
    sh.show()


def insert_data(data: list, table):
    cur.execute(
        f"INSERT INTO {table} VALUES (?, ?, ?)", tuple(map(str, data)))
    con.commit()
    print("Done! added: ", data)


def remove_data(d: str, table):
    cur.execute(f"DELETE FROM {table} WHERE id={d}")
    con.commit()
    print(show_table(table))


def main():
    show_table(db_name)
    s = input("> ")
    while s:
        match s:
            case "help":
                print("""

                """)
            case "insert":
                d = input("add data according to col > ").split()
                insert_data(d, db_name)
            case "remove":
                d = input("enter id to remove > ")
                remove_data(d, db_name)
            case "show":
                show_table(db_name)
            case other:
                print("bad input try again")
        s = input("> ")
    con.close()
    return 0


if __name__ == "__main__":
    main()
