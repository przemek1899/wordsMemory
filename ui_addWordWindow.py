# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Przemek\Documents\addWordMode.ui'
#
# Created: Sat May 30 12:37:34 2015
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

class Ui_AddWordDialog(object):
    def setupUi(self, AddWordDialog):
        AddWordDialog.setObjectName(_fromUtf8("AddWordDialog"))
        AddWordDialog.resize(376, 402)
        self.horizontalLayoutWidget = QtGui.QWidget(AddWordDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 30, 341, 31))
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
        self.horizontalLayoutWidget_7 = QtGui.QWidget(AddWordDialog)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(70, 350, 241, 31))
        self.horizontalLayoutWidget_7.setObjectName(_fromUtf8("horizontalLayoutWidget_7"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_9.setMargin(0)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.cancelButton = QtGui.QPushButton(self.horizontalLayoutWidget_7)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout_9.addWidget(self.cancelButton)
        self.okButton = QtGui.QPushButton(self.horizontalLayoutWidget_7)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.horizontalLayout_9.addWidget(self.okButton)
        self.formLayoutWidget = QtGui.QWidget(AddWordDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(19, 89, 341, 251))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.formLayout.setLayout(0, QtGui.QFormLayout.LabelRole, self.horizontalLayout_2)
        self.newWordLabel = QtGui.QLabel(self.formLayoutWidget)
        self.newWordLabel.setObjectName(_fromUtf8("newWordLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.newWordLabel)
        self.newWordLine = QtGui.QLineEdit(self.formLayoutWidget)
        self.newWordLine.setObjectName(_fromUtf8("newWordLine"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.newWordLine)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.formLayout.setLayout(2, QtGui.QFormLayout.LabelRole, self.horizontalLayout_3)
        self.polishLabel = QtGui.QLabel(self.formLayoutWidget)
        self.polishLabel.setObjectName(_fromUtf8("polishLabel"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.polishLabel)
        self.polishWordLine = QtGui.QLineEdit(self.formLayoutWidget)
        self.polishWordLine.setObjectName(_fromUtf8("polishWordLine"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.polishWordLine)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.formLayout.setLayout(4, QtGui.QFormLayout.LabelRole, self.horizontalLayout_4)
        self.englishLabel = QtGui.QLabel(self.formLayoutWidget)
        self.englishLabel.setObjectName(_fromUtf8("englishLabel"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.englishLabel)
        self.englishWordLine = QtGui.QLineEdit(self.formLayoutWidget)
        self.englishWordLine.setObjectName(_fromUtf8("englishWordLine"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.englishWordLine)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.formLayout.setLayout(6, QtGui.QFormLayout.LabelRole, self.horizontalLayout_5)
        self.gruopLabel = QtGui.QLabel(self.formLayoutWidget)
        self.gruopLabel.setObjectName(_fromUtf8("gruopLabel"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.gruopLabel)
        self.groupSelect = QtGui.QComboBox(self.formLayoutWidget)
        self.groupSelect.setObjectName(_fromUtf8("groupSelect"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.groupSelect)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.formLayout.setLayout(8, QtGui.QFormLayout.LabelRole, self.horizontalLayout_6)
        self.partOfSpeechLabel = QtGui.QLabel(self.formLayoutWidget)
        self.partOfSpeechLabel.setObjectName(_fromUtf8("partOfSpeechLabel"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.partOfSpeechLabel)
        self.partOfSpeechSelect = QtGui.QComboBox(self.formLayoutWidget)
        self.partOfSpeechSelect.setObjectName(_fromUtf8("partOfSpeechSelect"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.partOfSpeechSelect)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.formLayout.setLayout(10, QtGui.QFormLayout.LabelRole, self.horizontalLayout_7)
        self.commentLabel = QtGui.QLabel(self.formLayoutWidget)
        self.commentLabel.setObjectName(_fromUtf8("commentLabel"))
        self.formLayout.setWidget(11, QtGui.QFormLayout.LabelRole, self.commentLabel)
        self.commentText = QtGui.QPlainTextEdit(self.formLayoutWidget)
        self.commentText.setObjectName(_fromUtf8("commentText"))
        self.formLayout.setWidget(11, QtGui.QFormLayout.FieldRole, self.commentText)

        self.retranslateUi(AddWordDialog)
        QtCore.QMetaObject.connectSlotsByName(AddWordDialog)

    def retranslateUi(self, AddWordDialog):
        AddWordDialog.setWindowTitle(_translate("AddWordDialog", "Form", None))
        self.specialLetter1.setText(_translate("AddWordDialog", "ñ", None))
        self.specialLetter2.setText(_translate("AddWordDialog", "ó", None))
        self.specialLetter3.setText(_translate("AddWordDialog", "á", None))
        self.specialLetter4.setText(_translate("AddWordDialog", "ú", None))
        self.specialLetter5.setText(_translate("AddWordDialog", "é", None))
        self.specialLetter6.setText(_translate("AddWordDialog", "í", None))
        self.cancelButton.setText(_translate("AddWordDialog", "Cancel", None))
        self.okButton.setText(_translate("AddWordDialog", "OK", None))
        self.newWordLabel.setText(_translate("AddWordDialog", "New word", None))
        self.polishLabel.setText(_translate("AddWordDialog", "Polish", None))
        self.englishLabel.setText(_translate("AddWordDialog", "English", None))
        self.gruopLabel.setText(_translate("AddWordDialog", "Group", None))
        self.partOfSpeechLabel.setText(_translate("AddWordDialog", "Part of speech", None))
        self.commentLabel.setText(_translate("AddWordDialog", "Comment", None))

