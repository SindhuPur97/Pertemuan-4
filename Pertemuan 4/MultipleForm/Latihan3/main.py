import sys
from PyQt5.QtWidgets import QApplication

from Latihan3 import *

if __name__ == '__main__':
    a = QApplication(sys.argv)

    minform = Latihan3()
    minform.show()
    a.exec_()
