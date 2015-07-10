# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Przemek\Documents\WordsMemoryUI\testmode.ui'
#
# Created: Sat May 30 12:37:39 2015
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

class Ui_TestDialog(object):
    def setupUi(self, TestDialog):
        TestDialog.setObjectName(_fromUtf8("TestDialog"))
        TestDialog.resize(337, 367)
        self.horizontalLayoutWidget = QtGui.QWidget(TestDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 311, 31))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.specialLetter1 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.specialLetter1.setObjectName(_fromUtf8("specialLetter1"))
        self.horizontalLayout.addWidget(self.specialLetter1)
        self.specialLetter2 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.specialLetter2.setObjectName(_fromUtf8("specialLetter2"))
        self.horizontalLayout.addWidget(self.specialLetter2)
        self.specialLetter3 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.specialLetter3.setObjectName(_fromUtf8("specialLetter3"))
        self.horizontalLayout.addWidget(self.specialLetter3)
        self.specialLetter4 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.specialLetter4.setObjectName(_fromUtf8("specialLetter4"))
        self.horizontalLayout.addWidget(self.specialLetter4)
        self.specialLetter5 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.specialLetter5.setObjectName(_fromUtf8("specialLetter5"))
        self.horizontalLayout.addWidget(self.specialLetter5)
        self.specialLetter6 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.specialLetter6.setObjectName(_fromUtf8("specialLetter6"))
        self.horizontalLayout.addWidget(self.specialLetter6)
        self.horizontalLayoutWidget_7 = QtGui.QWidget(TestDialog)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(10, 320, 311, 31))
        self.horizontalLayoutWidget_7.setObjectName(_fromUtf8("horizontalLayoutWidget_7"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_9.setMargin(0)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.nextButton = QtGui.QPushButton(self.horizontalLayoutWidget_7)
        self.nextButton.setObjectName(_fromUtf8("nextButton"))
        self.horizontalLayout_9.addWidget(self.nextButton)
        self.checkButton = QtGui.QPushButton(self.horizontalLayoutWidget_7)
        self.checkButton.setObjectName(_fromUtf8("checkButton"))
        self.horizontalLayout_9.addWidget(self.checkButton)
        self.backToMenuButton = QtGui.QPushButton(self.horizontalLayoutWidget_7)
        self.backToMenuButton.setObjectName(_fromUtf8("backToMenuButton"))
        self.horizontalLayout_9.addWidget(self.backToMenuButton)
        self.formLayoutWidget = QtGui.QWidget(TestDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 80, 311, 221))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.formLayout.setLayout(0, QtGui.QFormLayout.LabelRole, self.horizontalLayout_2)
        self.wordLabel = QtGui.QLabel(self.formLayoutWidget)
        self.wordLabel.setObjectName(_fromUtf8("wordLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.wordLabel)
        self.wordLine = QtGui.QLineEdit(self.formLayoutWidget)
        self.wordLine.setEnabled(False)
        self.wordLine.setObjectName(_fromUtf8("wordLine"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.wordLine)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.formLayout.setLayout(2, QtGui.QFormLayout.LabelRole, self.horizontalLayout_4)
        self.polishLabel = QtGui.QLabel(self.formLayoutWidget)
        self.polishLabel.setObjectName(_fromUtf8("polishLabel"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.polishLabel)
        self.polishLine = QtGui.QLineEdit(self.formLayoutWidget)
        self.polishLine.setObjectName(_fromUtf8("polishLine"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.polishLine)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.formLayout.setLayout(4, QtGui.QFormLayout.LabelRole, self.horizontalLayout_5)
        self.englishLabel = QtGui.QLabel(self.formLayoutWidget)
        self.englishLabel.setObjectName(_fromUtf8("englishLabel"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.englishLabel)
        self.englishLine = QtGui.QLineEdit(self.formLayoutWidget)
        self.englishLine.setObjectName(_fromUtf8("englishLine"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.englishLine)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.formLayout.setLayout(6, QtGui.QFormLayout.LabelRole, self.horizontalLayout_6)
        self.commentLabel = QtGui.QLabel(self.formLayoutWidget)
        self.commentLabel.setObjectName(_fromUtf8("commentLabel"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.commentLabel)
        self.showCommentButton = QtGui.QPushButton(self.formLayoutWidget)
        self.showCommentButton.setObjectName(_fromUtf8("showCommentButton"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.showCommentButton)

        self.retranslateUi(TestDialog)
        QtCore.QMetaObject.connectSlotsByName(TestDialog)

    def retranslateUi(self, TestDialog):
        TestDialog.setWindowTitle(_translate("TestDialog", "Form", None))
        self.specialLetter1.setText(_translate("TestDialog", "ñ", None))
        self.specialLetter2.setText(_translate("TestDialog", "ó", None))
        self.specialLetter3.setText(_translate("TestDialog", "á", None))
        self.specialLetter4.setText(_translate("TestDialog", "ú", None))
        self.specialLetter5.setText(_translate("TestDialog", "é", None))
        self.specialLetter6.setText(_translate("TestDialog", "í", None))
        self.nextButton.setText(_translate("TestDialog", "Next", None))
        self.checkButton.setText(_translate("TestDialog", "Check", None))
        self.backToMenuButton.setText(_translate("TestDialog", "Back to menu", None))
        self.wordLabel.setText(_translate("TestDialog", "Word", None))
        self.polishLabel.setText(_translate("TestDialog", "Polish", None))
        self.englishLabel.setText(_translate("TestDialog", "English", None))
        self.commentLabel.setText(_translate("TestDialog", "Comment", None))
        self.showCommentButton.setText(_translate("TestDialog", "Show comment", None))

