__author__ = 'Przemek'

import sys

from ui_chooseLanguageWindow import Ui_ChooseLanguageWindow
from ui_addWordWindow import Ui_AddWordDialog
from ui_languageMenuWindow import Ui_LanguageMenuDialog
from ui_testWindow import Ui_TestDialog

from functools import partial
from PyQt4.QtGui import QMainWindow
from databaseObjects import Word, Answer
from model import Interface

class MainWindow(QMainWindow):

    spanishButtonLabel = str('Español')
    spanishSpecialCharacters = ['ñ', 'ó', 'á', 'ú', 'é', 'í']
    mode = {'es', 'en'}

    englishButtonLabel = str('English')

    def __init__(self):
        super(MainWindow, self).__init__()

    def initUI(self, onAddWordModel, closeConnection, onStartTestModel, onCheckAnswerModel,
               onNextTestWordModel, onContinueWithTest):

        self.onAddWordModel = onAddWordModel
        self.closeConnection = closeConnection
        self.onStartTestModel = onStartTestModel
        self.onCheckAnswerModel = onCheckAnswerModel
        self.onNextTestWordModel = onNextTestWordModel
        self.continueWithTest = onContinueWithTest

        self.ui = Ui_ChooseLanguageWindow()
        self.ui.setupUi(self)

        self.ui.spanishButton.clicked.connect(self.onSpanishDict)
        self.ui.englishButton.clicked.connect(self.onEnglishDict)

        self.setWindowTitle('Words Memory')
        self.show()



