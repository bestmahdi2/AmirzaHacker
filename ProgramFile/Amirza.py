from itertools import permutations
import sqlite3

class AmirzaClass:
    def amirza(self , text, number):
        # text = input("enter: ")
        textlist = text.replace("-"," ").replace("  "," ").split(" ")
            # textlist1 = text.replace("-"," ").repalce("  "," ").split(" ")
        x = 3
        i = 0
        lister = ["default", "default", "default", "default", "default","default","default","default""default" ]

        if number == 12:
            while x <= len(textlist):
                lister[i] = (list(permutations(textlist, x)))
                i += 1
                x += 1
        #     # print(lister)

        if number == 3 :
            while x <= number:
                lister[i] = (list(permutations(textlist, x)))
                x += 1

        if number == 4:
            while x <= number:
                lister[i] = (list(permutations(textlist, x)))
                x += 1

        if number == 5:
            x = 5
            while x <= len(textlist):
                lister[i] = (list(permutations(textlist, x)))
                x += 1
                i += 1

        if number == 7:
            while 3 <= x <= 4 :
                lister[i] = (list(permutations(textlist, x)))
                x += 1
                i += 1

        if number == 8:
            while 3 <= x < 4 :
                lister[i] = (list(permutations(textlist, x)))
                x += 1
                i += 1
            x = 5
            while 4 < x <= len(textlist):
                lister[i] = (list(permutations(textlist, x)))
                x += 1
                i += 1


        if number == 9:
            x = 4
            while 4 <= x < 5 :
                lister[i] = (list(permutations(textlist, x)))
                x += 1
                i += 1
            # x = 5
            while 5 <= x <= len(textlist):
                lister[i] = (list(permutations(textlist, x)))
                x += 1
                i += 1

        lister_new = []
        for i in lister :
            if i != "default" and i != "defaultdefault":
                lister_new.append(i)
        # print(lister_new)

        self.ultimList = []
        for i in lister_new:
            for k in i :
                self.ultimList.append("".join(k))
        # print(self.ultimList)

        self.ultimListO = list(dict.fromkeys(self.ultimList))
        # print(self.ultimListO)

    def create_connection(self, db_file):
        conn = None
        conn = sqlite3.connect(db_file)
        return conn

    def select_all_tasks(self,conn):
        cur = conn.cursor()
        cur.execute("SELECT entry from mdx")
        rows = cur.fetchall()
        self.diclist = []
        for row in rows:
            self.diclist.append(row[0])
        # print(lister)
#
# cla = AmirzaClass()
# cla.amirza("گ ب  د آ ب ا د",5)
#
# conn = cla.create_connection(r"Moin.db")
# cla.select_all_tasks(conn)
#
# print(cla.ultimList)
# answers = []
# for i in cla.ultimList :
#     if i in cla.diclist :
#         answers.append(i)
#
# print(answers)

