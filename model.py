import interfaceDB

__author__ = 'Przemek'

from os import getcwd
from random import shuffle
from sqlite3 import Error
from databaseObjects import Answer
from datetime import datetime

class Interface(object):

    dbPath = 'D:\sqlite3\wordsMemory.db'

    def __init__(self, ui):
        super(Interface, self)
        self.ui = ui
        self.db = interfaceDB.ConnectionDB()
        abPath = getcwd()
        try:
            self.db.connectToDB(self.dbPath)
            self.connected = True
            self.ui.initUI(onAddWordModel=self.addWord, closeConnection=self.closeDBConnection,
                           onStartTestModel=self.onStartTestButton, onCheckAnswerModel=self.onCheckAnswer,
                           onNextTestWordModel=self.onNextWord, onContinueWithTest=self.onContinueWithTest)
            #languages = self.getDicts()
        except Error:
            self.connected = False

    def onStartTestButton(self, dictID):
        self.wordsTest = self.getWordsFromDict(dictID)
        shuffle(self.wordsTest)
        self.currentWord = self.wordsTest.pop()
        self.ui.showTestView()
        self.ui.newWordLine.setText(self.currentWord[2])
        self.inCorrectWords = []

    def onCheckAnswer(self, answer):
        self.ui.enTranslation.setText(self.currentWord[5])
        if answer == self.currentWord[4]:
            self.ui.translation.setStyleSheet("color: rgb(0, 153, 0);")
            a = Answer(None, 1, datetime.now())
            #self.addAnswer()
        else:
            self.inCorrectWords.append(self.currentWord)
            a = Answer(None, 0, datetime.now())
            self.ui.translation.setStyleSheet("color: rgb(255, 0, 0);")
            self.ui.correctPLTranslation.show()
            self.ui.correctPLTranslation.setText(self.currentWord[4])
            #self.addAnswer()
        if not self.wordsTest:
            self.ui.nextButton.hide()
            if self.inCorrectWords:
                self.ui.windowContinue()
            else:
                self.ui.congratulations()

    def onNextWord(self):
        self.ui.correctPLTranslation.hide()
        self.ui.translation.setStyleSheet("color: rgb(0, 0, 0);")
        self.ui.translation.clear()
        self.ui.enTranslation.clear()
        self.currentWord = self.wordsTest.pop()
        self.ui.newWordLine.setText(self.currentWord[2])

    def onContinueWithTest(self):
        self.wordsTest = self.inCorrectWords
        shuffle(self.wordsTest)
        self.currentWord = self.wordsTest.pop()
        self.ui.showTestView()
        self.ui.newWordLine.setText(self.currentWord[2])
        self.inCorrectWords = []

    def addWord(self, word):
        print('add word model')
        try:
            self.db.insertNewWord(word)
        except Error as e:
            print('Error exception')
            print(e)
        except Exception as e1:
            print('Exception exception')
            print(e1)

    def addAnswer(self, a):
        try:
            self.db.insertAnswer(a)
        except Error as e:
            pass
        except Exception as e1:
            pass

    def getDicts(self):
        try:
            d = self.db.selectDicts()
            return d
        except Error as a:
            pass
        except Exception as e:
            pass

    def getPartOfSpeech(self, dictID):
        pass

    def closeDBConnection(self):
        self.db.closeConnection()

    def getWordsFromDict(self, dictID):
        print(dictID)
        words = self.db.selectWordsFromDict(dictID)
        return words



