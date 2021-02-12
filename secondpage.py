from PyQt5.QtWidgets import QMainWindow
from  include.window2 import Ui_MainWindow


class DetailPage(QMainWindow):
    def __init__(self ):
        super().__init__()

        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)