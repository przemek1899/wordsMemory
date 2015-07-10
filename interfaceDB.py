__author__ = 'Przemek'

import sqlite3


class ConnectionDB(object):

    def __init__(self):
        super(ConnectionDB, self)

    def connectToDB(self, dbFilename):
        try:
            self.conn = sqlite3.connect(dbFilename)
            self.cur = self.conn.cursor()
        except sqlite3.Error as e:
            print('Error while connecting to db')
            raise e
        except Exception as e1:
            print(e1)


    def closeConnection(self):
        if self.conn:
            self.conn.close()

    def insertNewWord(self, newWord):
        wordValues = (None, newWord.dictID, newWord.word, newWord.partOfSpeechID, newWord.pl, newWord.other, 0, 0,
                      newWord.imagePath, newWord.comment, newWord.hint)
        self.cur.execute('INSERT INTO words VALUES (?,?,?,?,?,?,?,?,?,?,?)', wordValues)
        self.conn.commit()

    def insertAnswer(self, an):
        answerValues = (None, an.wordID, an.date.__str__(), an.isCorrect)
        self.cur.execute('INSERT INTO answers VALUES (?,?,?,?)', answerValues)
        self.conn.commit()

    def selectDicts(self):
        self.cur.execute('SELECT ID, language FROM dictionaries;')
        return self.cur.fetchall()

    def selectPartOfSpeech(self, dictID):
        self.cur.execute('SELECT name FROM part_of_speech WHERE ID_DICT = ?', dictID)
        return self.cur.fetchall()

    def selectWordsFromDict(self, dictID):
        self.cur.execute('SELECT * FROM words WHERE ID_DICT = ?', (dictID,))
        return self.cur.fetchall()