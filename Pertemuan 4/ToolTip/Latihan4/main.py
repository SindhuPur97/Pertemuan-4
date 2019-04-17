import sys
from PyQt5.QtWidgets import QApplication

from Latihan4 import *

if __name__ == '__main__':
    a = QApplication(sys.argv)

    minform = Latihan4()
    minform.show()
    a.exec_()
