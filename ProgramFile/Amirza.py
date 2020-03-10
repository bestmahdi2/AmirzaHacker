from itertools import permutations
import sqlite3


class AmirzaClass:
    def amirzafunc(self, text, number):             # number is the value of checkboxes which user check
        textlist = text.replace("-", " ").replace("  ", " ").split(" ")             # change string to list
        x = 3           # we want words with more than 3 characters
        i = 0           # counter

        # answer keeper:
        lister = ["default", "default", "default", "default", "default", "default", "default", "default""default"]

        # 4, 3, 5 are checked
        if number == 12:
            # it make all possible words with letters that entered ,
            # from 3 letters in a word till the length of the string that entered in a word
            while x <= len(textlist):
                lister[i] = (list(permutations(textlist, x)))
                i += 1
                x += 1

        if number == 3:
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

        # 3 and 4 checked
        if number == 7:
            while 3 <= x <= 4:
                lister[i] = (list(permutations(textlist, x)))
                x += 1
                i += 1

        # 3 and 5 checked but 4 not checked
        if number == 8:
            while 3 <= x < 4:
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
            while 4 <= x < 5:
                lister[i] = (list(permutations(textlist, x)))
                x += 1
                i += 1
            while 5 <= x <= len(textlist):
                lister[i] = (list(permutations(textlist, x)))
                x += 1
                i += 1

        lister_new = []

        # make a new list for answers
        for i in lister:
            if i != "default" and i != "defaultdefault":
                lister_new.append(i)

        self.ultimList = []
        # join the letters to make words
        for i in lister_new:
            for k in i:
                self.ultimList.append("".join(k))

        # remove all duplicated words
        self.ultimList_undup = list(dict.fromkeys(self.ultimList))

    # creat connection with the sqlite database
    def create_connection(self, db_file):
        conn = None
        conn = sqlite3.connect(db_file)
        return conn

    # select all tasks in a column
    def select_all_tasks(self, conn):
        cur = conn.cursor()
        cur.execute("SELECT entry from mdx")
        rows = cur.fetchall()

        # save all data in a column to use in future
        self.diclist = []
        for row in rows:
            self.diclist.append(row[0])

#####################################
# this is for test , just uncomment  below :

# cla = AmirzaClass()
# cla.amirzafunc("گ ب  د آ ب ا د",4)
# # Moin.db is the name of the database
# conn = cla.create_connection(r"Moin.db")
# cla.select_all_tasks(conn)
#
# print(cla.ultimList)
# print(cla.ultimList_undup)
#
# answers = []
# for i in cla.ultimList_undup :
#     if i in cla.diclist :
#         answers.append(i)
#
# print(answers)


#####################################