# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Przemek\Documents\WordsMemoryUI\languagemode.ui'
#
# Created: Sat May 30 12:37:45 2015
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

class Ui_LanguageMenuDialog(object):
    def setupUi(self, LanguageMenuDialog):
        LanguageMenuDialog.setObjectName(_fromUtf8("LanguageMenuDialog"))
        LanguageMenuDialog.resize(191, 286)
        self.centralwidget = QtGui.QWidget(LanguageMenuDialog)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.startGenTestButton = QtGui.QPushButton(self.centralwidget)
        self.startGenTestButton.setGeometry(QtCore.QRect(20, 50, 121, 23))
        self.startGenTestButton.setObjectName(_fromUtf8("startGenTestButton"))
        self.addNewWordButton = QtGui.QPushButton(self.centralwidget)
        self.addNewWordButton.setGeometry(QtCore.QRect(20, 130, 121, 23))
        self.addNewWordButton.setObjectName(_fromUtf8("addNewWordButton"))
        self.addNewGroupButton = QtGui.QPushButton(self.centralwidget)
        self.addNewGroupButton.setGeometry(QtCore.QRect(20, 170, 121, 23))
        self.addNewGroupButton.setObjectName(_fromUtf8("addNewGroupButton"))
        self.backToMenuButton = QtGui.QPushButton(self.centralwidget)
        self.backToMenuButton.setGeometry(QtCore.QRect(20, 210, 121, 23))
        self.backToMenuButton.setObjectName(_fromUtf8("backToMenuButton"))
        self.startGroupTestButton = QtGui.QPushButton(self.centralwidget)
        self.startGroupTestButton.setGeometry(QtCore.QRect(20, 90, 121, 23))
        self.startGroupTestButton.setObjectName(_fromUtf8("startGroupTestButton"))
        LanguageMenuDialog.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(LanguageMenuDialog)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 191, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuLanguage = QtGui.QMenu(self.menubar)
        self.menuLanguage.setObjectName(_fromUtf8("menuLanguage"))
        self.menu2 = QtGui.QMenu(self.menubar)
        self.menu2.setObjectName(_fromUtf8("menu2"))
        LanguageMenuDialog.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(LanguageMenuDialog)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        LanguageMenuDialog.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuLanguage.menuAction())
        self.menubar.addAction(self.menu2.menuAction())

        self.retranslateUi(LanguageMenuDialog)
        QtCore.QMetaObject.connectSlotsByName(LanguageMenuDialog)

    def retranslateUi(self, LanguageMenuDialog):
        LanguageMenuDialog.setWindowTitle(_translate("LanguageMenuDialog", "MainWindow", None))
        self.startGenTestButton.setText(_translate("LanguageMenuDialog", "Start general test", None))
        self.addNewWordButton.setText(_translate("LanguageMenuDialog", "Add new word", None))
        self.addNewGroupButton.setText(_translate("LanguageMenuDialog", "Add new group", None))
        self.backToMenuButton.setText(_translate("LanguageMenuDialog", "Back to menu", None))
        self.startGroupTestButton.setText(_translate("LanguageMenuDialog", "Start test with a group", None))
        self.menuLanguage.setTitle(_translate("LanguageMenuDialog", "Language", None))
        self.menu2.setTitle(_translate("LanguageMenuDialog", "2", None))

