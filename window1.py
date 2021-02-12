
from PyQt5 import QtCore, QtGui, QtWidgets
from camera1show import CameraPage, Camera2Page, Camera3Page, Camera4Page
from secondpage import DetailPage


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1469, 1279)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/rake.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/cam.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon1)
        self.commandLinkButton.setIconSize(QtCore.QSize(50, 50))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.commandLinkButton)
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_2.setIcon(icon1)
        self.commandLinkButton_2.setIconSize(QtCore.QSize(50, 50))
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.commandLinkButton_2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("others/walle_2.jpg"))
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("others/walle_2.jpg"))
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.label_4)
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_3.setIcon(icon1)
        self.commandLinkButton_3.setIconSize(QtCore.QSize(50, 50))
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.commandLinkButton_3)
        self.commandLinkButton_4 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_4.setIcon(icon1)
        self.commandLinkButton_4.setIconSize(QtCore.QSize(50, 50))
        self.commandLinkButton_4.setObjectName("commandLinkButton_4")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.commandLinkButton_4)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("others/walle_2.jpg"))
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setEnabled(True)
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("others/walle_2.jpg"))
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.label_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("others/logo.png"))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/kırmızıbuton.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.toolButton.setIcon(icon2)
        self.toolButton.setIconSize(QtCore.QSize(30, 30))
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_2.addWidget(self.toolButton)
        self.toolButton_5 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_5.setText("")
        self.toolButton_5.setIcon(icon2)
        self.toolButton_5.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_5.setObjectName("toolButton_5")
        self.horizontalLayout_2.addWidget(self.toolButton_5)
        self.toolButton_3 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_3.setText("")
        self.toolButton_3.setIcon(icon2)
        self.toolButton_3.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_3.setObjectName("toolButton_3")
        self.horizontalLayout_2.addWidget(self.toolButton_3)
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setText("")
        self.toolButton_2.setIcon(icon2)
        self.toolButton_2.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_2.setObjectName("toolButton_2")
        self.horizontalLayout_2.addWidget(self.toolButton_2)
        self.toolButton_4 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_4.setText("")
        self.toolButton_4.setIcon(icon2)
        self.toolButton_4.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_4.setObjectName("toolButton_4")
        self.horizontalLayout_2.addWidget(self.toolButton_4)
        self.toolButton_6 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_6.setText("")
        self.toolButton_6.setIcon(icon2)
        self.toolButton_6.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_6.setObjectName("toolButton_6")
        self.horizontalLayout_2.addWidget(self.toolButton_6)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setEnabled(True)
        self.comboBox.setMinimumSize(QtCore.QSize(200, 80))
        self.comboBox.setMaximumSize(QtCore.QSize(100, 100))
        self.comboBox.setStyleSheet("background-color: rgb(255, 47, 20);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"selection-background-color: rgb(255, 255, 255,0);\n"
"selection-background-color: rgb(255, 38, 10,0);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.push= QtWidgets.QToolButton(self.centralwidget)
        self.push.isCheckable()
        self.push.setText("Go")

        self.verticalLayout.addWidget(self.comboBox, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.push, 1, QtCore.Qt.AlignRight)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1469, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.toolButton_5.clicked.connect(self.tikla)
        self.toolButton_4.clicked.connect(self.tikla)
        self.toolButton_3.clicked.connect(self.tikla)
        self.toolButton_2.clicked.connect(self.tikla)
        self.toolButton.clicked.connect(self.tikla)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Interface-1"))
        self.commandLinkButton.setText(_translate("MainWindow", "Camera1"))
        self.commandLinkButton_2.setText(_translate("MainWindow", "Camera2"))
        self.commandLinkButton_3.setText(_translate("MainWindow", "Camera3"))
        self.commandLinkButton_4.setText(_translate("MainWindow", "Camera4"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Window1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Window2"))


        self.commandLinkButton.clicked.connect(self.opencam)
        self.camera=CameraPage()
        self.commandLinkButton_2.clicked.connect(self.opencam2)
        self.camera2=Camera2Page()
        self.commandLinkButton_3.clicked.connect(self.opencam3)
        self.camera3=Camera3Page()
        self.commandLinkButton_4.clicked.connect(self.opencam4)
        self.camera4=Camera4Page()
        self.details=DetailPage()
        self.push.clicked.connect(self.gowindow)


    def gowindow(self):

        if self.comboBox.currentText()== "Window2":

            self.details.show()
            MainWindow.close()
            self.details.ui.commandLinkButton_6.clicked.connect(self.reshow5)

    def  reshow5(self):

        self.details.close()

        MainWindow.show()
        self.comboBox.setCurrentIndex(0)

    def opencam(self ):

        self.camera.show()
        MainWindow.close()
        self.camera.ui.commandLinkButton.clicked.connect(self.reshow)
    def reshow(self):
        self.camera.close()
        MainWindow.show()

    def opencam2(self ):
        self.camera2.show()    
        MainWindow.close()
        self.camera2.ui.commandLinkButton.clicked.connect(self.reshow2)
    def reshow2(self):
        self.camera2.close()
        MainWindow.show()
    def opencam3(self ):
        self.camera3.show()    
        MainWindow.close()
        self.camera3.ui.commandLinkButton.clicked.connect(self.reshow3)

    def reshow3(self):
        self.camera3.close()
        MainWindow.show()
    def opencam4(self ):

        self.camera4.showMaximized()
        MainWindow.close()
        self.camera4.ui.commandLinkButton.clicked.connect(self.reshow4)
    def reshow4(self):
        self.camera4.close()
        MainWindow.show()
    def tikla(self):
        self.icon9 = QtGui.QIcon()
        self.icon9.addPixmap(QtGui.QPixmap(":/icons/icons/kırmızıbuton.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_5.setIcon(self.icons9)
        self.toolButton_4.setIcon(self.icon9)
        self.toolButton_3.setIcon(self.icon9)
        self.toolButton_2.setIcon(self.icon9)
        self.toolButton.setIcon(self.icon9)

import icons_rc
import photos_rc
    
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())