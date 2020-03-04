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

    def pushB_clicked(self):
        m = AmirzaClass()
        text = self.lineEdit.text()
        self. listers = m.amirza(text)

        conn = m.create_connection(r"Moin.db")
        m.select_all_tasks(conn)

        answers = []
        for i in m.ultimList :
            if i in m.diclist :
                answers.append(i)
        nondup = list(dict.fromkeys(answers))
        self.to_show = " ".join(nondup)
        self.textBrowser.setText(self.to_show)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = mains()
    ui.setupUi(MainWindow)


    ui.pushButton.clicked.connect(ui.pushB_clicked)


    MainWindow.show()
    sys.exit(app.exec_())