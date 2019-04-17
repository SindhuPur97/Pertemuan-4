from PyQt5.QtWidgets import (QWidget, QPushButton, QToolTip)

from PyQt5.QtGui import QFont

class Latihan4(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(400, 300)
        self.move(300, 300)
        self.setWindowTitle('Latihan Menampilkan Tooltip')

        self.button = QPushButton('Other Form')
        self.button.move(160, 120)
        self.button.setParent(self)
        self.button.setToolTip('''<font color=red>Tombol untuk membuka</font>
                                    <b>Form Lain</b>''')
        self.button.clicked.connect(self.buttonClick)

        self.button2 = QPushButton('Keluar')
        self.button2.move(160, 150)
        self.button2.setParent(self)
        self.button2.setToolTip('''<font color=blue>Tombol untuk</font>
                                    <b>Keluar</b>''')
        self.button2.clicked.connect(self.buttonClick)

    def buttonClick(self):
        self.close()
