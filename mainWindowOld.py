#!usr/bin/python
### coding: utf-8
#__author__ = 'Przemyslaw Teodorski'

import sys
from functools import partial
from PyQt4 import QtGui
from databaseObjects import Word, Answer
from model import Interface


class MainWindowOld(QtGui.QMainWindow):

    #languages = {1: }

    spanishButtonLabel = str('Español')
    spanishSpecialCharacters = ['ñ', 'ó', 'á', 'ú', 'é', 'í']
    mode = {'es', 'en'}

    englishButtonLabel = str('English')

    def __init__(self):
        super(MainWindowOld, self).__init__()

    def initUI(self, onAddWordModel, closeConnection, onStartTestModel, onCheckAnswerModel,
               onNextTestWordModel, onContinueWithTest):

        self.onAddWordModel = onAddWordModel
        self.closeConnection = closeConnection
        self.onStartTestModel = onStartTestModel
        self.onCheckAnswerModel = onCheckAnswerModel
        self.onNextTestWordModel = onNextTestWordModel
        self.continueWithTest = onContinueWithTest

        self.spanishButton = QtGui.QPushButton(self.spanishButtonLabel)
        self.spanishButton.clicked.connect(self.onSpanishDict)

        self.englishButton = QtGui.QPushButton(self.englishButtonLabel)
        self.englishButton.clicked.connect(self.onEnglishDict)

        self.mainWidget = QtGui.QWidget()
        mainLayout = QtGui.QGridLayout()
        mainLayout.addWidget(self.spanishButton, 0,0,2,1)
        mainLayout.addWidget(self.englishButton, 1,0,2,1)
        self.mainWidget.setLayout(mainLayout)

        self.setCentralWidget(self.mainWidget)
        self.setGeometry(200, 200, 600, 500)
        self.setWindowTitle('Words Memory')
        self.show()

    def onSpanishDict(self):
        self.languageMode = 1
        self.addWordButton = QtGui.QPushButton('Añadir una palabra')
        self.addWordButton.clicked.connect(self.onAddWordWindow)

        self.startTestButton = QtGui.QPushButton('Empezar test')
        self.startTestButton.clicked.connect(self.onStartTest)

        subWidget = QtGui.QWidget()
        newLayout = QtGui.QGridLayout()
        newLayout.addWidget(self.addWordButton, 0,0,2,1)
        newLayout.addWidget(self.startTestButton, 1,0,2,1)
        subWidget.setLayout(newLayout)

        self.setCentralWidget(subWidget)

    def onEnglishDict(self):
        self.languageMode = 2
        self.addWordButton = QtGui.QPushButton('Add new word')
        self.addWordButton.clicked.connect(self.onAddWordWindow)

        self.startTestButton = QtGui.QPushButton('Start test')
        self.startTestButton.clicked.connect(self.onStartTest)

        subWidget = QtGui.QWidget()
        newLayout = QtGui.QGridLayout()
        newLayout.addWidget(self.addWordButton, 0,0,2,1)
        newLayout.addWidget(self.startTestButton, 1,0,2,1)
        subWidget.setLayout(newLayout)

        self.setCentralWidget(subWidget)

    def swapToSpanishCharacters(self, text):
        if len(text):
            root = str(text)[0:-1]
            l = str(text)[-1]
            if l == 'ń':
                self.newWordLine.setText(root + 'ñ')
            elif l == 'ó':
                self.newWordLine.setText(root + 'ó')
            elif l == 'ą':
                self.newWordLine.setText(root + 'á')
            elif l == 'ę':
                self.newWordLine.setText(root + 'é')


    def onAddWordWindow(self):
        self.newWordLine = QtGui.QLineEdit()
        #connect newWordLine with spanish characters
        self.newWordLine.textEdited.connect(self.swapToSpanishCharacters)

        self.translation = QtGui.QLineEdit()
        self.enTranslation = QtGui.QLineEdit()
        self.comment = QtGui.QPlainTextEdit()

        wordLabel = QtGui.QLabel('Palabra')
        translationLabel = QtGui.QLabel('Traslación polaco')
        enTranslationLabel = QtGui.QLabel('Traslación ingles')
        commentLabel = QtGui.QLabel('Comentario')

        self.acceptButton = QtGui.QPushButton('Ok')
        self.acceptButton.clicked.connect(self.onAcceptNewWord)

        self.cancelButton = QtGui.QPushButton('Cancel')
        self.cancelButton.clicked.connect(self.onCancelAddWord)

        layout = QtGui.QGridLayout()
        layout.addWidget(self.getWidgetSpecialLetters(), 0, 0, 1, 2)
        layout.addWidget(wordLabel, 1, 0, 1, 1)
        layout.addWidget(self.newWordLine, 1, 1, 1, 2)
        layout.addWidget(translationLabel, 2, 0, 1, 1)
        layout.addWidget(self.translation, 2, 1, 1, 2)

        layout.addWidget(enTranslationLabel, 3, 0, 1, 1)
        layout.addWidget(self.enTranslation, 3, 1, 1, 2)

        layout.addWidget(commentLabel, 4, 0, 1, 1)
        layout.addWidget(self.comment, 4, 1, 1, 2)

        layout.addWidget(self.acceptButton, 5, 0, 1, 1)
        layout.addWidget(self.cancelButton, 6, 0, 1, 1)

        subWidget = QtGui.QWidget()
        subWidget.setLayout(layout)
        self.setCentralWidget(subWidget)

    def getWidgetSpecialLetters(self):
        if self.languageMode == 1:
            #spanish dictionary
            buttonWidget = QtGui.QWidget()
            layout = QtGui.QHBoxLayout()
            for i in self.spanishSpecialCharacters:
                b = QtGui.QPushButton(str(i))
                t = b.text()
                b.clicked.connect(partial(self.onSpecialCharacterClicked, t))
                layout.addWidget(b)
            buttonWidget.setLayout(layout)
            return buttonWidget

        else :
            pass

    def onSpecialCharacterClicked(self, other):
        text = self.newWordLine.text()
        text += other
        self.newWordLine.setText(text)

    def checkAnswer(self):
        a = str(self.translation.text())
        self.onCheckAnswerModel(a)

    def onStartTest(self):
        self.onStartTestModel(self.languageMode)

    def showTestView(self):
        self.newWordLine = QtGui.QLabel()

        self.translation = QtGui.QLineEdit()
        self.enTranslation = QtGui.QLineEdit()

        self.correctPLTranslation = QtGui.QLineEdit()
        self.correctPLTranslation.setReadOnly(True)
        self.correctPLTranslation.hide()

        self.comment = QtGui.QPlainTextEdit()
        self.comment.hide()

        wordLabel = QtGui.QLabel('Palabra')
        translationLabel = QtGui.QLabel('Traslación polaco')
        enTranslationLabel = QtGui.QLabel('Traslación ingles')
        commentLabel = QtGui.QLabel('Comentario')

        self.nextButton = QtGui.QPushButton('Siguiente')
        self.nextButton.clicked.connect(self.onNextTestWordModel)

        self.acceptButton = QtGui.QPushButton('Ok')
        self.acceptButton.clicked.connect(self.checkAnswer)

        self.cancelButton = QtGui.QPushButton('Cancelar')
        self.cancelButton.clicked.connect(self.onCancelAddWord)

        layout = QtGui.QGridLayout()
        layout.addWidget(self.getWidgetSpecialLetters(), 0, 0, 1, 2)
        layout.addWidget(wordLabel, 2, 0, 1, 1)
        layout.addWidget(self.newWordLine, 2, 1, 1, 1)

        layout.addWidget(translationLabel, 3, 0, 1, 1)
        layout.addWidget(self.translation, 3, 1, 1, 1)
        layout.addWidget(self.correctPLTranslation, 4, 1, 1, 1)

        layout.addWidget(enTranslationLabel, 5, 0, 1, 1)
        layout.addWidget(self.enTranslation, 5, 1, 1, 1)

        layout.addWidget(commentLabel, 6, 0, 1, 1)
        layout.addWidget(self.comment, 6, 1, 1, 2)

        layout.addWidget(self.nextButton, 7, 0, 1, 1)
        layout.addWidget(self.acceptButton, 7, 1, 1, 1)
        layout.addWidget(self.cancelButton, 8, 0, 1, 1)

        subWidget = QtGui.QWidget()
        subWidget.setLayout(layout)
        self.setCentralWidget(subWidget)

    def windowContinue(self):
        label = ('Continuar con las palabras que no supiste?')
        ret = QtGui.QMessageBox.question(self, 'Atención', label, QtGui.QMessageBox.Cancel | QtGui.QMessageBox.Ok,
                                         QtGui.QMessageBox.Ok)
        if ret == QtGui.QMessageBox.Ok:
            self.continueWithTest()

    def congratulations(self):
        pass

    def onCancelAddWord(self):
        if self.languageMode == 1:
            self.onSpanishDict()
        else:
            pass

    def clearFields(self):
        self.translation.setText('')
        self.enTranslation.setText('')
        self.newWordLine.setText('')
        self.comment.setText('')

    def onAcceptNewWord(self):
        print('accept ui')
        newWord = str(self.newWordLine.text())
        polishTranslation = str(self.translation.text())
        englishTranslation = str(self.enTranslation.text())
        comment = str(self.comment)
        w = Word(self.languageMode, newWord, polishTranslation, englishTranslation, comment=comment)
        self.onAddWordModel(w)
        self.clearFields()

    def validateNewWord(self):
        if str(self.newWordLine.text()) == None:
            return False
        elif str(self.translation.text()) == None:
            return False

    def closeEvent(self, event):
        self.closeConnection()
        event.accept()
        print('after close event')


def main():
    app = QtGui.QApplication(sys.argv)
    ui = MainWindowOld()
    interface = Interface(ui);
    #ui.initUI()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()