from itertools import permutations
import sqlite3


class AmirzaClass:
    def amirzafunc(self, text):
        textlist = text.replace("-", " ").replace("  ", " ").split(" ")
        x = 3
        i = 0

        lister = ["default", "default", "default", "default", "default", "default", "default"]

        while  x <= len(textlist):
            lister[i] = (list(permutations(textlist, x)))
            x += 1
            i += 1

        lister_new = []

        for i in lister:
            if i != "default" :
                lister_new.append(i)

        self.ultimList = []

        for i in lister_new:
            for k in i:
                self.ultimList.append("".join(k))

        self.ultimList_undup = list(dict.fromkeys(self.ultimList))

    def create_connection(self, db_file):
        conn = None
        conn = sqlite3.connect(db_file)
        return conn

    def select_all_tasks(self, conn):
        cur = conn.cursor()
        cur.execute("SELECT entry from mdx")
        rows = cur.fetchall()

        self.diclist = []
        for row in rows:
            self.diclist.append(row[0])

#####################################

# textget = input("Type your letters")
cla = AmirzaClass()
# cla.amirzafunc(textget)
cla.amirzafunc("گ ب  د آ ب ا د")


conn = cla.create_connection(r"Moin.db")
cla.select_all_tasks(conn)

answers = []
for i in cla.ultimList_undup :
    if i in cla.diclist :
        answers.append(i)

print(answers)


#####################################