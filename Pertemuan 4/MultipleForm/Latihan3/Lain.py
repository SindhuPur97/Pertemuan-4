from PyQt5.QtWidgets import QWidget, QPushButton

class Lain(QWidget):
        def __init__(self):
                super().__init__()
                self.setupUi()

        def setupUi(self):
                self.resize(400, 300)
                self.move(300, 300)
                self.setWindowTitle('Form Lain')

                self.button = QPushButton('About')
                self.button1 = QPushButton('Tutup')
                self.button.move(150, 130)
                self.button1.move(310, 260)
                self.button.setParent(self)
                self.button1.setParent(self)

                self.button.clicked.connect(self.buttonClick)
                self.button1.clicked.connect(self.buttonClick1)

        def buttonClick(self):
                self.close()
        def buttonClick1(self):
                self.close()
