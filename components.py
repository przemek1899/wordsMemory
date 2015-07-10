__author__ = 'Przemek'

from PyQt4 import QtGui

class AddWordDialog(QtGui.QDialog):

    def __init__(self, parent=None):
        super(AddWordDialog, self).__init__(parent)
        #self.parent = parent
        self.setWindowTitle('Skrypty')

        self.newWordLine = QtGui.QLineEdit()
        self.translation = QtGui.QLineEdit()

        self.acceptButton = QtGui.QPushButton('Ok')
        self.acceptButton.clicked.connect(self.onAccept)

        self.cancelButton = QtGui.QPushButton('Cancel')
        self.cancelButton.clicked.connect(self.onCancel)

        layout = QtGui.GridLayout()
        self.setLayout(layout)
