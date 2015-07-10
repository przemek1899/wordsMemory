__author__ = 'Przemek'

class Word(object):

    def __init__(self, dictID, word, pl, other, partOfSpeechID=None, imagePath=None, comment=None, hint=None):
        super(Word, self)
        self.dictID = dictID
        self.word = word
        self.pl = pl
        self.other = other
        self.partOfSpeechID = partOfSpeechID
        self.imagePath = imagePath
        self.comment = comment
        self.hint = hint

    def modify(self,  dictID, word, pl, other, partOfSpeechID, imagePath, comment, hint):
        self.dictID = dictID
        self.word = word
        self.pl = pl
        self.other = other
        self.partOfSpeechID = partOfSpeechID
        self.imagePath = imagePath
        self.comment = comment
        self.hint = hint


class Answer(object):

    def __init__(self, wordID, isCorrect, date):
        super(Answer, self)
        self.wordID = wordID
        self.isCorrect = isCorrect
        self.date = date
