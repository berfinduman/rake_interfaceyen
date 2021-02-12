from PyQt5.QtWidgets import QApplication, QWidget,QLabel, QPushButton,QVBoxLayout,QHBoxLayout,QSlider,QStyle,QSizePolicy, QFileDialog
from PyQt5.QtGui import QIcon,QPixmap, QPalette
from PyQt5.QtMultimediaWidgets import QVideoWidget,QVideoWidgetControl,QCameraViewfinder
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import Qt, QUrl
import sys

class Window(QWidget,object,):
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("Camera4")
        
        icon = QIcon()
        icon.addPixmap(QPixmap(":/icons/icons/rake.jpg"), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.setGeometry(0,0,720,480)
        self.init_ui()
    def init_ui(self):
        self.mediaPlayer=QMediaPlayer(None, QMediaPlayer.VideoSurface)

        videowidget=QVideoWidget()

        #create button for open and slot
        openBtn=QPushButton("Open Video")
        openBtn.clicked.connect(self.open_file)


        #create button for playing
        self.playBtn=QPushButton()
        self.playBtn.setEnabled(False)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playBtn.clicked.connect(self.play_video)

        #create slider
        self.slider=QSlider(Qt.Horizontal)
        self.slider.setRange(0,0)
        self.slider.sliderMoved.connect(self.set_position)


        #create a label 
        self.label=QLabel()
        self.label.setSizePolicy(QSizePolicy.Preferred,QSizePolicy.Maximum)

        #create hbox layout
        hboxLayout=QHBoxLayout()
        hboxLayout.setContentsMargins(0,0,0,0)

        #setwidget to the hbox layout
        hboxLayout.addWidget(openBtn)
        hboxLayout.addWidget(self.playBtn)
        hboxLayout.addWidget(self.slider)

        #create and set vbox layout
        vboxlayout=QVBoxLayout()
        vboxlayout.addWidget(videowidget)
        vboxlayout.addLayout(hboxLayout)
        vboxlayout.addWidget(self.label)

        self.setLayout(vboxlayout)
        
        self.mediaPlayer.setVideoOutput(videowidget)
        #mediaplayer signal slots
        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)
        

    def open_file(self):
        filename,_ = QFileDialog.getOpenFileName(self, "Open Video")

        if filename != "":
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.playBtn.setEnabled(True)
    def play_video(self):
        if self.mediaPlayer.state()==QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()

        else: 
            self.mediaPlayer.play()

    def mediastate_changed(self, state):
        if self.mediaPlayer.state()==QMediaPlayer.PlayingState:
            self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    #position changed, duration changed

    def position_changed(self, position):
        self.slider.setValue(position)
    
    def duration_changed(self, duration):
        self.slider.setRange(0,duration)
    
    def set_position(self, position):
        self.mediaPlayer.setPosition(position)
    
    def handle_errors(self):
        self.playBtn.setEnabled(True)
        self.label.setText("Error:"+ self.mediaPlayer.errorString())


        

import photos_rc
import icons_rc

app=QApplication(sys.argv)
window=Window()
window.show()
sys.exit(app.exec_())
"""



"""
    
    