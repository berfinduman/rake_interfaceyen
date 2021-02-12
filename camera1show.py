from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
from include.camera1 import Ui_MainWindow
from include.camera2 import Ui_MainWindow2
from include.camera3 import Ui_MainWindow3
from include.yenivideo import Window


#from new import Window


class CameraPage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


class Camera2Page(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self)


class Camera3Page(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow3()
        self.ui.setupUi(self)


class Camera4Page(QMainWindow):
    def __init__(self ):
        super().__init__()

        self.ui=Ui_MainWindow3()
        self.ui.setupUi(self)



