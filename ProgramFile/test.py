# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Amirza_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
# Hidpi scaling
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
# use Hidpi icons
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(560, 310)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Pirate Icon 21.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(0.978)
        MainWindow.setStyleSheet("color:#FCE400;background-color:#3C3F41;")
        MainWindow.setDocumentMode(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 541, 31))
        self.lineEdit.setStyleSheet("background-color:#F5F5F5 ; color:black")
        self.lineEdit.setText("")
        self.lineEdit.setFrame(False)
        self.lineEdit.setDragEnabled(True)
        self.lineEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 5, 531, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("overflow : auto;")
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(245, 80, 71, 31))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setWhatsThis("")
        self.pushButton.setStyleSheet("background-color :#B8860B; color: black")
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 140, 540, 131))
        self.textBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textBrowser.setStyleSheet("color:white ; align:\"center\";font-size:14px;")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.textBrowser.setObjectName("textBrowser")
        self.label_Error = QtWidgets.QLabel(self.centralwidget)
        self.label_Error.setGeometry(QtCore.QRect(12, 63, 351, 16))
        self.label_Error.setStyleSheet("color:red;")
        self.label_Error.setText("")
        self.label_Error.setObjectName("label_Error")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(17, 114, 531, 23))

        self.progressBar.setProperty("value", 0)

        maxs = [1,2,3,4,5]
        self.progressBar.setMaximum(len(maxs))

        for i in maxs:
            self.progressBar.setProperty("value", maxs.index(i)+1)

        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 560, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Amirza Hacker"))
        self.lineEdit.setStatusTip(_translate("MainWindow", "You can type here"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter your characters here..."))
        self.label.setText(_translate("MainWindow", "Amirza Hacker:"))
        self.pushButton.setToolTip(_translate("MainWindow", "Shortcut : Enter"))
        self.pushButton.setStatusTip(_translate("MainWindow", "Click to change number you entered"))
        self.pushButton.setText(_translate("MainWindow", "Go"))
        self.textBrowser.setStatusTip(_translate("MainWindow", "Reasults"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
