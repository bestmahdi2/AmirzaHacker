from os import sep
from PyQt5 import QtWidgets, QtCore,QtGui
from ProgramFile.Amirza import AmirzaClass
from ProgramFile.Amirza_ui import Ui_MainWindow

# Hidpi scaling
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
# use Hidpi icons
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class MainClass(Ui_MainWindow):         # inheritate from Ui_MainWindow
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)         # run the original codes in setupUi

# region icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("spy.ico"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
# endregion

        self.cancel = "false"           # for clicking on the cancel button
        self.num = 0


    def retranslateUi(self, MainWindow):
        super().retranslateUi(MainWindow)
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setShortcut(_translate("MainWindow", "Return"))             # make shortcut for pushbutton

    # add checkbox numbers to self.num
    def number_adder_func(self,num):
        self.num += num

    def checkbox_checker_func(self):
        self.num = 0
        check3 = self.checkBox3.isChecked()                 # if checkbox3 is checked ,check3 is True  , else is False
        check4 = self.checkBox4.isChecked()
        check5 = self.checkBoxMore.isChecked()

        if check3 ==True:
            self.number_adder_func(3)
        if check4 ==True:
            self.number_adder_func(4)
        if check5 ==True:
            self.number_adder_func(5)

        if check3 == False and check4 == False and check5 == False:             # show error if none of checkboxes checked
            self.label_Error.setStyleSheet("color:red")
            self.label_Error.setText("Check at least one checkbox")

        if check3 == True or check4 == True or check5 == True:              # go to next function if at least one of checkboxes is  checked
            self.empty_entrance_func()

##
    def empty_entrance_func(self):
        text = self.lineEdit.text()
        text = text.replace("  "," ").replace("   "," ").replace("    "," ")
        if text == "" or text ==" ":
            self.label_Error.setText("Empty entrance")
        else:
            self.pushB_clicked()

    def language_checker_func(self):
        persian = ["ا", "آ", "ب", "پ", "ت", "ث", "ج", "چ", "ح", "خ", "د", "ذ", "ر", "ز", "ژ", "س", "ش", "ص", "ض", "ط",
                   "ظ", "ع", "غ", "ف", "ق", "ک", "گ", "ل", "ن", "و", "ه", "ی", "م", " "]
        text = self.lineEdit.text()         # get the text in the lineEdit
        textlist = text.split()         # split them and make a list
        Counter = 0
        while 0 <= Counter < len(textlist):
            if textlist[Counter] not in persian:
                self.label_Error.setStyleSheet("color:red")
                self.label_Error.setText("Incorrect entrance")
                self.pushButton.setEnabled(False)   # disable the pushbutton
                QtWidgets.QApplication.processEvents()
                break
            else:
                ui.label_Error.setText("")
                ui.pushButton.setEnabled(True)
                QtWidgets.QApplication.processEvents()
                Counter += 1


    def pushB_clicked(self):
        self.cancel = "false"
        self.wrong = False
        self.textBrowser.setText("")

        m = AmirzaClass()           # make object from AmirzaClass
        text = self.lineEdit.text()
        m.amirzafunc(text,self.num)             # send the self.num (number of checkboxes) to amirzafunc

        self.label_Error.setStyleSheet("color:white")
        self.label_Error.setText("Processing...")

        conn = m.create_connection(r"Moin.db")
        m.select_all_tasks(conn)

        answers = []
        self.progressBar.setMaximum(len(m.ultimList_undup))             # set maximum for progressbar by length of the ultimList_undup

        def cancel_func():          # when the cancel button clicked
                ui.cancel = "True"
                ui.progressBar.setProperty("value", 0)

        self.pushButton_2.clicked.connect(cancel_func)          # connect cancel button to cancel_func

        for i in m.ultimList_undup:
                self.progressBar.setProperty("value", m.ultimList_undup.index(i) + 1)              # set value of the progressbar by index of (i) in m.ultimList_undup
                if i in m.diclist:
                    answers.append(i)           # append answers if the word is in the database
                QtWidgets.QApplication.processEvents()
                if ui.cancel == "True":
                    break           # break if cancel button clicked
        try:
            nondup = list(dict.fromkeys(answers))       # remove duplicated words in answers
            self.to_show = " ".join(nondup)         # join the nondup objects with space character
            self.textBrowser.setText(self.to_show)          # set textBrowser to show the to_show

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
    ui = MainClass()
    ui.setupUi(MainWindow)

    ui.lineEdit.textEdited.connect(ui.language_checker_func)            # check language input while typing
    ui.pushButton.clicked.connect(ui.checkbox_checker_func)             # connect pushbutton


    MainWindow.show()
    sys.exit(app.exec_())