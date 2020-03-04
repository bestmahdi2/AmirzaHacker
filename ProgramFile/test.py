import sqlite3


def create_connection(db_file):
    conn = None
    conn = sqlite3.connect(db_file)
    return conn


def select_all_tasks(conn):
    cur = conn.cursor()
    cur.execute("SELECT entry from mdx")
    rows = cur.fetchall()
    # rows =rows.replace(",), (" , ",")
    # print(rows)
    lister = []
    for row in rows:
        lister.append(row[0])
    # if "ادب" in lister:
    #     print(lister.index("ادب"))

conn = create_connection(r"Moin.db")
select_all_tasks(conn)