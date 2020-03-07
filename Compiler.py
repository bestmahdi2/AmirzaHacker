from PyQt5 import QtWidgets, QtCore
from ProgramFile.Amirza import AmirzaClass
from ProgramFile.Amirza_ui import Ui_MainWindow

# Hidpi scaling
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
# use Hidpi icons
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class mains(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.cancel = "false"
        self.num = 0

    def retranslateUi(self, MainWindow):
        super().retranslateUi(MainWindow)
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setShortcut(_translate("MainWindow", "Return"))

    def checker(self,num):
        self.num += num
    def firstpush(self):
        self.num = 0
        check3 = self.checkBox3.isChecked()
        check4 = self.checkBox4.isChecked()
        check5 = self.checkBoxMore.isChecked()

        if check3 ==True:
            self.checker(3)
        if check4 ==True:
            self.checker(4)
        if check5 ==True:
            self.checker(5)
        if check3 == False and check4 == False and check5 == False :
            self.label_Error.setStyleSheet("color:red")
            self.label_Error.setText("Check at least one checkbox")
        if check3 == True or check4 == True or check5 == True:
            self.entrance()

    def spell(self):
        persian = ["ا", "آ", "ب", "پ", "ت", "ث", "ج", "چ", "ح", "خ", "د", "ذ", "ر", "ز", "ژ", "س", "ش", "ص", "ض", "ط",
                   "ظ", "ع", "غ", "ف", "ق", "ک", "گ", "ل", "ن", "و", "ه", "ی", "م", " "]
        text = self.lineEdit.text()
        textlist = text.split()
        for i in textlist:
            if i not in persian:
                self.label_Error.setStyleSheet("color:red")
                self.label_Error.setText("Incorrect entrance")
                self.pushButton.setEnabled(False)
            else:
                ui.label_Error.setText("")
                ui.pushButton.setEnabled(True)
        # for i in te

    def entrance(self):
        text = self.lineEdit.text()
        text = text.replace("  "," ").replace("   "," ").replace("    "," ")
        if text == "" or text ==" ":
            self.label_Error.setText("Empty entrance")
        else:
            self.pushB_clicked()
    def pushB_clicked(self):
        self.cancel = "false"
        self.wrong = False
        self.textBrowser.setText("")

        m = AmirzaClass()
        text = self.lineEdit.text()
        m.amirza(text,self.num)

        self.label_Error.setStyleSheet("color:white")
        self.label_Error.setText("Processing...")

        conn = m.create_connection(r"Moin.db")
        m.select_all_tasks(conn)

        answers = []
                # print()
        self.progressBar.setMaximum(len(m.ultimListO))

            # print(m.ultimList)
        def cancels():
                ui.cancel = "True"
                ui.progressBar.setProperty("value", 0)

        self.pushButton_2.clicked.connect(cancels)

        for i in m.ultimListO:
                self.progressBar.setProperty("value", m.ultimListO.index(i) + 1)
                if i in m.diclist:
                    answers.append(i)
                QtWidgets.QApplication.processEvents()
                if ui.cancel == "True":
                    break
                # self.progressBar.setValue(progress)
                # QtWidgets.QApplication.processEvents()
        try:
            nondup = list(dict.fromkeys(answers))
            # print(answers)
            self.to_show = " ".join(nondup)
            self.textBrowser.setText(self.to_show)

        except :
            self.label_Error.setText("Incorrect entrance")
            self.wrong = True

        if self.wrong == False:
            self.label_Error.setStyleSheet("color:yellow")
            self.label_Error.setText("Finished")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = mains()
    ui.setupUi(MainWindow)

    ui.lineEdit.textEdited.connect(ui.spell)
    ui.pushButton.clicked.connect(ui.firstpush)


    MainWindow.show()
    sys.exit(app.exec_())