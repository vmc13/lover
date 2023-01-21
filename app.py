from PySide6 import QtWidgets
from PySide6.QtCore import QEvent
from ui_main import Ui_MainWindow

import random

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.coracao.setVisible(False)

        self.button_no.clicked.connect(self.moveButton)
        self.button_yes.clicked.connect(self.yes_choice)
        self.frame_no.installEventFilter(self)

    def moveButton(self):
        self.frame_no.move(random.randint(0,300), random.randint(0,300))

    def yes_choice(self):
        self.pergunta.setText("😈😈😈")
        self.coracao.setVisible(True)
        self.button_no.setVisible(False)
        self.button_yes.setVisible(False)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Enter and obj == self.frame_no:
            self.moveButton()
            return True
        else:
            return False


app = QtWidgets.QApplication([])

window = MainWindow()

window.show()

app.exec()