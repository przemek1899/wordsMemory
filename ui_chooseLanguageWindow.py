# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Przemek\Documents\WordsMemoryUI\mainwindow.ui'
#
# Created: Sat May 30 12:37:50 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ChooseLanguageWindow(object):
    def setupUi(self, ChooseLanguageWindow):
        ChooseLanguageWindow.setObjectName(_fromUtf8("ChooseLanguageWindow"))
        ChooseLanguageWindow.resize(134, 181)
        self.centralWidget = QtGui.QWidget(ChooseLanguageWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.spanishButton = QtGui.QPushButton(self.centralWidget)
        self.spanishButton.setGeometry(QtCore.QRect(30, 40, 75, 23))
        self.spanishButton.setObjectName(_fromUtf8("spanishButton"))
        self.englishButton = QtGui.QPushButton(self.centralWidget)
        self.englishButton.setGeometry(QtCore.QRect(30, 90, 75, 23))
        self.englishButton.setObjectName(_fromUtf8("englishButton"))
        ChooseLanguageWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(ChooseLanguageWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 134, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        ChooseLanguageWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(ChooseLanguageWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        ChooseLanguageWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(ChooseLanguageWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        ChooseLanguageWindow.setStatusBar(self.statusBar)

        self.retranslateUi(ChooseLanguageWindow)
        QtCore.QMetaObject.connectSlotsByName(ChooseLanguageWindow)

    def retranslateUi(self, ChooseLanguageWindow):
        ChooseLanguageWindow.setWindowTitle(_translate("ChooseLanguageWindow", "MainWindow", None))
        self.spanishButton.setText(_translate("ChooseLanguageWindow", "Español", None))
        self.englishButton.setText(_translate("ChooseLanguageWindow", "English", None))

