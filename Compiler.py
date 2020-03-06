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
    def pushB_clicked(self):
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

        self.cancel = "false"
        self.textBrowser.setText("")

        m = AmirzaClass()
        self.label_Error.setStyleSheet("color:white")
        self.label_Error.setText("Processing...")

        text = self.lineEdit.text()

        m.amirza(text,self.num)

        conn = m.create_connection(r"Moin.db")
        m.select_all_tasks(conn)

        answers = []
        # print()
        self.progressBar.setMaximum(len(m.ultimListO))
        # print(m.ultimList)
        def cancels():
            ui.cancel = "True"
            ui.progressBar.setProperty("value",0)
        self.pushButton_2.clicked.connect(cancels)

        for i in m.ultimListO:
            self.progressBar.setProperty("value", m.ultimListO.index(i)+1)
            if i in m.diclist:
                answers.append(i)
            QtWidgets.QApplication.processEvents()
            if ui.cancel == "True":
                break


            # self.progressBar.setValue(progress)
            # QtWidgets.QApplication.processEvents()
        nondup = list(dict.fromkeys(answers))
        self.to_show = " ".join(nondup)
        self.textBrowser.setText(self.to_show)
        self.label_Error.setStyleSheet("color:yellow")
        self.label_Error.setText("Finished")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = mains()
    ui.setupUi(MainWindow)


    ui.pushButton.clicked.connect(ui.pushB_clicked)


    MainWindow.show()
    sys.exit(app.exec_())