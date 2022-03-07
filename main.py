from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from maingui import *
import sys

class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        super().setupUi(self)
    
        

        



if __name__ == '__main__':
    qt = QApplication(sys.argv)
    new = App()
    new.show()
    qt.exec_()      