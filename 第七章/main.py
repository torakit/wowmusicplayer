#修复了部分configparse的错误: activateicon
#更改了窗口为Qmainwindow,因为有些方法继承不到,也可能是我不懂,反正为了实现功能为前提就修改了
#修改了部分 playsong ,nextsong,presong 的错误,已知还有一些,没来得及弄,持续修复中
#curd 已修复
#tablewidget.setItem 为 (y,x,data) 
#新增的功能在这章有讲,请看博客


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTimer,QDateTime,QThread,QUrl,QByteArray,QSize,QPoint
import time

from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit,QDialog,QFileDialog
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QLabel,QAbstractItemView,QGraphicsDropShadowEffect ,QMainWindow
# from PyQt5.QtWidgets import QMessageBox, QMenu
import sqlite3


# from PyQt5 import QtCore, QtGui, QtWidgets,Qt
# from PyQt5.QtWidgets import QFileDialog,QListWidgetItem,QAbstractItemView,QGraphicsItem, QGraphicsPixmapItem,QGraphicsScene, QGraphicsView,QLabel,QTableWidgetItem,QApplication,QComboBox
# from PyQt5.QtCore import QTimer,QStringListModel,QSize,QObject,pyqtSignal,QThread,QUrl
from PyQt5.QtGui import QPixmap,QFont,QIcon
# from PyQt5.QtWebEngineWidgets import *
import os
import random,time
from pygame import mixer
from mutagen.mp3 import MP3
import style

from netmusicsearch import *
import requests
# from dler import *
from lyric import * ##########################################
import music_tag

from datetime import timedelta

import configparser

from pathlib import Path

from PyQt5.QtCore import QObject , pyqtSignal
class Settings(QDialog):
    datatrans=pyqtSignal(str )
    def setupUi(self, Form):
        self.dirname=str(__file__).replace(str(__file__).split('\\')[-1],'')
        
        Form.setObjectName("Form")
        # Form.setWindowIcon(QtGui.QIcon(icon1))
        Form.resize(389, 352)
        
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 20, 54, 12))
        self.label.setObjectName("label")
        
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(10, 220, 54, 12))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(10, 100, 54, 12))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(10, 160, 54, 12))
        self.label_7.setObjectName("label_7")
        self.picbox = QtWidgets.QCheckBox(self)
        self.picbox.setGeometry(QtCore.QRect(10, 40, 91, 16))
        self.picbox.setObjectName("picbox")
        self.websearch = QtWidgets.QCheckBox(self)
        self.websearch.setGeometry(QtCore.QRect(190, 40, 71, 16))
        self.websearch.setObjectName("websearch")
        self.visual = QtWidgets.QCheckBox(self)
        self.visual.setGeometry(QtCore.QRect(100, 40, 81, 16))
        self.visual.setObjectName("visual")
        self.normalmode = QtWidgets.QCheckBox(self)
        self.normalmode.setGeometry(QtCore.QRect(140, 70, 71, 16))
        self.normalmode.setObjectName("normalmode")
        self.minimode = QtWidgets.QCheckBox(self)
        self.minimode.setGeometry(QtCore.QRect(50, 70, 71, 16))
        self.minimode.setObjectName("minimode")
        self.picpath = QtWidgets.QLineEdit(self)
        self.picpath.setGeometry(QtCore.QRect(10, 120, 113, 20))
        self.picpath.setObjectName("picpath")
        self.picimp = QtWidgets.QPushButton(self)
        self.picimp.setGeometry(QtCore.QRect(130, 120, 75, 23))
        self.picimp.setObjectName("picimp")
        self.picfolder = QtWidgets.QLineEdit(self)
        self.picfolder.setGeometry(QtCore.QRect(10, 180, 113, 20))
        self.picfolder.setObjectName("picfolder")
        self.fldimp = QtWidgets.QPushButton(self)
        self.fldimp.setGeometry(QtCore.QRect(130, 180, 75, 23))
        self.fldimp.setObjectName("fldimp")
        self.skimp = QtWidgets.QPushButton(self)
        self.skimp.setGeometry(QtCore.QRect(130, 240, 75, 23))
        self.skimp.setObjectName("skimp")
        self.skinpath = QtWidgets.QLineEdit(self)
        self.skinpath.setGeometry(QtCore.QRect(10, 240, 113, 20))
        self.skinpath.setObjectName("skinpath")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(10, 280, 71, 16))
        self.label_2.setObjectName("label_2")
        self.downloadpath = QtWidgets.QLineEdit(self)
        self.downloadpath.setGeometry(QtCore.QRect(10, 300, 113, 20))
        self.downloadpath.setObjectName("downloadpath")
        self.downimp = QtWidgets.QPushButton(self)
        self.downimp.setGeometry(QtCore.QRect(130, 300, 75, 23))
        self.downimp.setObjectName("downimp")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
    
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "功能显示:"))
        self.label_3.setText(_translate("Form", "皮肤:"))
        self.label_5.setText(_translate("Form", "导入图片"))
        self.label_7.setText(_translate("Form", "幻灯片:"))
        self.picbox.setText(_translate("Form", "图片/幻灯片"))
        self.websearch.setText(_translate("Form", "网上搜索"))
        self.visual.setText(_translate("Form", "音乐可视化"))
        self.normalmode.setText(_translate("Form", "一般模式"))
        self.minimode.setText(_translate("Form", "迷你模式"))
        self.picimp.setText(_translate("Form", "导入"))
        self.fldimp.setText(_translate("Form", "导入文件夹"))
        self.skimp.setText(_translate("Form", "导入"))
        self.label_2.setText(_translate("Form", "下载文件夹"))
        self.downimp.setText(_translate("Form", "导入"))

            
        
        self.config=configparser.ConfigParser()

        self.picimp.clicked.connect(self.picchange)
        self.fldimp.clicked.connect(self.picchnage1)
        self.downimp.clicked.connect(self.downpath)
        self.skimp.clicked.connect(self.skinconfig)
    
    def skinconfig(self):
        try:
            pass
        except:
            pass
        
        pass

    def picchnage1(self):
        if self.picfolder.text()=='':
            directory=QFileDialog.getExistingDirectory(self.picfolder,
                    "选取文件夹",
                    "./")
            self.picfolder.setText('{}'.format(directory))
            self.config['DEFAULT']['saver']=directory   
        else:
            self.config['DEFAULT']['saver']=self.picfolder.text()
        
        self.writeconfig()
        
        
    def picchange(self):
        if self.picpath.text()=='':
            directory=QFileDialog.getOpenFileName(self.picpath,"Add picture","","Picture Filed(*.jpg *.gif *.png)")        
            
            self.picpath.setText('{}'.format(directory[0]))
            self.config['DEFAULT']['pic']=directory[0]
        else:
            self.config['DEFAULT']['pic']=self.picpath.text()
        self.writeconfig()
    
    def downpath(self):
        if self.picpath.text()=='':
            directory=QFileDialog.getOpenFileName(self.picpath,"Add picture","","Picture Filed(*.jpg *.gif *.png)")        
            self.picpath.setText(directory[0])
            self.config['DEFAULT']['downpath']=directory[0]
        else:
            self.config['DEFAULT']['downpath']=self.picpath.text()
        self.writeconfig()
    
    def writeconfig(self):
        with open(f'{self.dirname}settings.ini','w') as f:
            self.config.write(f)
    
    def status1(self,a):
        if a==5:
            self.status.setText('图片已导入')
        elif a==7:
            self.status.setText('文件夹已导入')
        elif a==8:
            self.status.setText('下载文件夹已导入')
        elif a==9:
            self.status.setText('皮肤文件夹已导入')
        elif a==10:
            self.status.setText('迷你模式')
        elif a==11:
            self.status.setText('一般模式')
        elif a==12:
            self.status.setText(self.skinname)
        elif a==13:
            self.status.setText(self.songname)
        elif a==14:
            self.status.setText('')
        elif a==15:
            self.status.setText('')
        elif a==16:
            self.status.setText('')
        elif a==17:
            self.status.setText('')
        elif a==18:
            self.status.setText('')
        elif a==19:
            self.status.setText('')
        elif a==20:
            self.status.setText('')
        elif a==21:
            self.status.setText('')
        elif a==22:
            self.status.setText('')
        self.timer1.stop()
        self.timer1.deleteLater()
        pass

###################################################
###################################################
###################################################
###################################################
###################################################
###################################################

###################################################
class Ui_Form(QMainWindow):
    
    
    
    def __init__(self):
        super().__init__()

        self.setObjectName("Form")
        
        self.dirname=str(__file__).replace(str(__file__).split('\\')[-1],'')
        
        icon1=f'{self.dirname}images\\1.ico'
        
        # Form.setWindowIcon(QtGui.QIcon(icon1))
        # Form.setWindowFlag(Qt.FramelessWindowHint)
        # self.border_width = 8
        # 设置 窗口无边框和背景透明 *必须
        # Form.setWindowOpacity(0.0)
        # Form.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.window_width,self.window_height=681,610
        self.setMinimumSize(self.window_width,self.window_height)
        
        self.bg = QtWidgets.QLabel(self)
        self.bg.setObjectName("bg")
        self.bg.resize(681, 610)
        self.bg.setMouseTracking(True)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(130, 375, 410, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mini = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.mini.setSizeIncrement(QtCore.QSize(0, 0))
        self.mini.setObjectName("mini")
        self.horizontalLayout.addWidget(self.mini)
        self.ranser = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.ranser.setObjectName("ranser")
        self.horizontalLayout.addWidget(self.ranser)
        self.play = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.play.setObjectName("play")
        self.play.setFixedSize(64,64)
        self.horizontalLayout.addWidget(self.play)
        
        self.stopbtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.stopbtn.setObjectName("stop")
        self.stopbtn.setFixedSize(64,64)
        self.horizontalLayout.addWidget(self.stopbtn)
        self.pre = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pre.setObjectName("pre")
        self.horizontalLayout.addWidget(self.pre)
        self.next = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.next.setObjectName("next")
        self.horizontalLayout.addWidget(self.next)
        # self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        # self.label.setObjectName("label")
        self.mutebtn=QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.mutebtn.setObjectName('mute')
        
        self.horizontalLayout.addWidget(self.mutebtn)
        self.volm = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.volm.setOrientation(QtCore.Qt.Horizontal)
        self.volm.setObjectName("horizontalSlider")
        self.horizontalLayout.addWidget(self.volm)
        # self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        # self.label_2.setObjectName("label_2")
        # self.horizontalLayout.addWidget(self.label_2)
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(545, 425, 128, 128))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.scan = QtWidgets.QLabel(self.gridLayoutWidget)
        
        self.scan.setObjectName("scan")
        self.gridLayout.addWidget(self.scan, 0, 0, 1, 1)
        self.playlist = QtWidgets.QTableWidget(self)
        self.a=221
        self.playlist.verticalHeader().setVisible(False)
        self.playlist.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.playlist.setColumnCount(4)
        self.playlist.setHorizontalHeaderLabels(['歌名', '歌手', '专辑','封面'])
        self.playlist.setGeometry(QtCore.QRect(20, 21, self.a, 241))
        self.playlist.setObjectName("playlist")
        
        
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(130, 354, 410, 21))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.slider= QtWidgets.QSlider(self.horizontalLayoutWidget_2)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slider")
        self.horizontalLayout_2.addWidget(self.slider)
        self.time1 = QtWidgets.QLabel(self)
        self.time1.setGeometry(QtCore.QRect(420, 380, 54, 12))
        self.time1.setObjectName("time1")
        
        self.total = QtWidgets.QLabel(self)
        self.total.setGeometry(QtCore.QRect(480, 380, 54, 12))
        self.total.setObjectName("total")
        self.importbtn = QtWidgets.QPushButton(self)
        self.importbtn.setGeometry(QtCore.QRect(20, 270, 75, 23))
        self.importbtn.setObjectName("importbtn")
        self.delbtn = QtWidgets.QPushButton(self)
        self.delbtn.setGeometry(QtCore.QRect(160, 270, 75, 23))
        self.delbtn.setObjectName("delbtn")
        self.plsinp = QtWidgets.QLineEdit(self)
        self.plsinp.setGeometry(QtCore.QRect(20, 300, 113, 21))
        self.plsinp.setObjectName("plsinp")
        shadow = QGraphicsDropShadowEffect()
  
        # setting blur radius
        shadow.setBlurRadius(15)
  
        # adding shadow to the label
        self.plsinp.setGraphicsEffect(shadow)
        self.plsbtn = QtWidgets.QPushButton(self)
        self.plsbtn.setGeometry(QtCore.QRect(124, 296, 75, 23))
        self.plsbtn.setObjectName("plsbtn")
        self.set = QtWidgets.QPushButton(self)
        self.set.setGeometry(QtCore.QRect(520, 5, 75, 23))
        self.set.setObjectName("set")
        
        self.minim =QtWidgets.QPushButton(self)
        self.minim.setGeometry(QtCore.QRect(560, 5, 75, 23))
        self.minim.setObjectName("minim")
        self.closebtn = QtWidgets.QPushButton(self)
        self.closebtn.setGeometry(QtCore.QRect(600, 5, 75, 23))
        self.closebtn.setObjectName("closebtn")
      
        
        
        
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(440, 30, 221, 131))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.serbtn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.serbtn.setObjectName("serbtn")
        self.gridLayout_2.addWidget(self.serbtn, 1, 1, 1, 1)
        self.serinput = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.serinput.setObjectName("serinput")
        self.gridLayout_2.addWidget(self.serinput, 1, 0, 1, 1)
        self.serl1 = QtWidgets.QTableWidget(self.gridLayoutWidget_2)
        self.serl1.setObjectName("serl1")
        self.serl1.setColumnCount(0)
        self.serl1.setRowCount(0)
        self.gridLayout_2.addWidget(self.serl1, 2, 0, 1, 2)
        self.tog2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.tog2.setObjectName("tog2")
        self.gridLayout_2.addWidget(self.tog2, 0, 0, 1, 1)
        self.tog0y = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.tog0y.setObjectName("tog0y")
        self.gridLayout_2.addWidget(self.tog0y, 0, 1, 1, 1)
        self.tog0 = QtWidgets.QPushButton(self)
        self.tog0.setGeometry(QtCore.QRect(170, 0, 71, 23))
        self.tog0.setObjectName("tog0")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(250, 0, 181, 161))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tog1 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.tog1.setObjectName("tog1")
        self.gridLayout_3.addWidget(self.tog1, 0, 0, 1, 1)
        self.disa1 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.disa1.setObjectName("disa1")
        self.gridLayout_3.addWidget(self.disa1, 0, 1, 1, 1)
        self.wallp = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.wallp.setObjectName("wallp")
        self.wallp.setScaledContents(True)#图片大小自适应
        self.gridLayout_3.addWidget(self.wallp, 1, 0, 1, 2)
        
        self.status = QtWidgets.QLabel(self)
        self.status.setGeometry(QtCore.QRect(0, 550, 693, 30))
        self.status.setObjectName("status")
        # self.refscan = QtWidgets.QPushButton(self)
        # self.refscan.setGeometry(QtCore.QRect(630, 431, 31, 20))
        # self.refscan.setObjectName("refscan")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(250, 170, 411, 131))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tog3 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.tog3.setObjectName("tog3")
        self.gridLayout_4.addWidget(self.tog3, 0, 1, 1, 1)
        self.dis3 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.dis3.setObjectName("dis3")
        self.gridLayout_4.addWidget(self.dis3, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 0, 0, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.gridLayoutWidget_4)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_4.addWidget(self.graphicsView, 1, 0, 1, 3)

        self.config=configparser.ConfigParser()
        self.config.read(f'{self.dirname}settings.ini')
        print(f'{self.dirname}settings.ini')
        
        self.lyriclist = QtWidgets.QListWidget(self)
        self.lyriclist.setGeometry(QtCore.QRect(20, 460, 520, 90))
        self.lyriclist.setObjectName("lyriclist")
        
        
        
        self.cover = QtWidgets.QLabel(self)
        self.cover.setGeometry(QtCore.QRect(1, 330, 128, 128))
        self.cover.setText("")
        self.cover.setObjectName("label_3")
        self.jump = QtWidgets.QPushButton(self)
        self.jump.setGeometry(QtCore.QRect(500, 435, 70, 50))
        self.jump.setObjectName("jump")


        

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        # self.mini.setText(_translate("Form", "min"))
        # self.ranser.setText(_translate("Form", "ran/ser"))
        # self.play.setText(_translate("Form", "p"))
        # self.pre.setText(_translate("Form", "pre"))
        # self.next.setText(_translate("Form", "next"))
        self.time1.setText(_translate("Form", "00:00:00"))
        self.total.setText(_translate("Form", "/ 00:00:00"))
        self.importbtn.setText(_translate("Form", "导入"))
        self.delbtn.setText(_translate("Form", "删除"))
        self.plsbtn.setText(_translate("Form", "搜索"))
        self.set.setText(_translate("Form", "设定"))
        self.serbtn.setText(_translate("Form", "搜索"))
        # self.tog2.setText(_translate("Form", "-"))
        # self.tog0y.setText(_translate("Form", "2o"))
        # self.tog0.setText(_translate("Form", "-"))
        # self.tog1.setText(_translate("Form", "-"))
        # self.disa1.setText(_translate("Form", "1o"))
        # self.status.setText(_translate("Form", ""))
        # self.tog3.setText(_translate("Form", "-"))
        # self.dis3.setText(_translate("Form", "3o"))
        self.tog2.clicked.connect(self.set2)#searchb
        self.tog3.clicked.connect(self.set3)#vg
        # self.tog1.clicked.connect(self.set1)#wp

        self.testup()
        # self.skip()
        self.ena=True
        self.a=221
        self.slider.valueChanged.connect(self.slidersettime)
        # self.slider.sliderMoved.connect(self.slidersettime)
        self.tog0.clicked.connect(self.toggle0)#playlist
        self.set.clicked.connect(self.opendialogwin)
        self.importbtn.clicked.connect(self.importfile)
        # playcontrol
        self.play.clicked.connect(self.playsong)
        self.pre.clicked.connect(self.previoussong)
        self.next.clicked.connect(self.nextsong)
        self.ranser.clicked.connect(self.shuffleplaylist)
        self.volm.valueChanged.connect(self.setvolume)
        self.mutebtn.clicked.connect(self.mutesong)
        mixer.init()
        self.checksettingfile()
        # self.dirname=os.path.dirname(sys.executable)#windows打包后程序的当前的exe的文件夹
        self.dirname=str(__file__).replace(str(__file__).split('\\')[-1],'')
        self.closeevent(0)#这里因为每次启动也是跑这个,那么我就没必要重复写个函数了
        self.mute=False#默认是有声的
        self.playsw=False#默认是暂停
        self.ransw=False#默认是顺序播放
        self.randomlist=[]#shuffleplaylist
        self.musiclist1=[]
        self.index=0
        self.closebtn.clicked.connect(lambda:self.close())
        self.minim.clicked.connect(lambda:self.showMinimized())
        """
        self.ser1 #
        self.mini #
        self.ranser #
        self.set #
        self.delbtn
        self.plsbtn #localsearch
        self.play #play
        self.pre #preview
        self.next #next
        self.ser1 #websearch
        self.plsinp #localsearchinp
        self.serinput #searchinp
        self.volm
        self.slider
        """
        
        
    
    # def showEvent(self, QShowEvent):
    #     print("窗口被展示了")
    # def mousePressEvent(self, QMouseEvent):
    #     print("鼠标按压")
    

    
#1############################################################################
    
        
            
    def styleconfig(self):

        self.slider.setStyleSheet(style.playsliderstyle())
        self.playlist.setStyleSheet(style.tablehheader())
        self.volm.setStyleSheet(style.volumestyle())
        self.play.setStyleSheet(style.buttonstyle())
        self.stopbtn.setStyleSheet(style.buttonstyle())
        self.ranser.setStyleSheet(style.buttonstyle())
        self.mutebtn.setStyleSheet(style.buttonstyle())
        self.next.setStyleSheet(style.buttonstyle())
        self.pre.setStyleSheet(style.buttonstyle())
        self.mini.setStyleSheet(style.buttonstyle())
        self.delbtn.setStyleSheet(style.buttonstyle())
        self.plsbtn.setStyleSheet(style.buttonstyle())
        self.serbtn.setStyleSheet(style.buttonstyle())
        self.set.setStyleSheet(style.buttonstyle())
        self.tog2.setStyleSheet(style.buttonstyle())
        self.tog0y.setStyleSheet(style.buttonstyle())
        self.tog0.setStyleSheet(style.buttonstyle())
        self.tog1.setStyleSheet(style.buttonstyle())
        self.disa1.setStyleSheet(style.buttonstyle())
        self.dis3.setStyleSheet(style.buttonstyle())
        self.tog3.setStyleSheet(style.buttonstyle())
        self.jump.setStyleSheet(style.buttonstyle())
        self.importbtn.setStyleSheet(style.buttonstyle())
        

        self.horizontalLayoutWidget.setStyleSheet(style.layoutstyle())
        self.time1.setStyleSheet(style.labelstyle())
        self.total.setStyleSheet(style.labelstyle())
        self.cover.setStyleSheet(style.labelstyle1())
        self.plsinp.setStyleSheet(style.lineeditstyle())
        
        self.serinput.setStyleSheet(style.lineeditstyle())
        
        # Form.setStyleSheet(style.windowsskin())
        self.bg.setStyleSheet(style.windowsskin())
        self.closebtn.setStyleSheet(style.buttonstyle())
        self.minim.setStyleSheet(style.buttonstyle())
    def activateicon(self):
        
        # try:
        #第二次会直接跑setting文件,设置文件有机会在没有设置的时候为空,所以会读取默认值

        if "ran1" in self.config['icon']:
            ran1=self.config['icon']['ran1']
        else:
            ran1=f"{self.dirname}images\\suf.png"
        
        if "ran2" in self.config['icon']:
            ran2=self.config['icon']['ran2']
        else:
            ran2=f"{self.dirname}images\\pro.png"

        
        if "play" in self.config['icon']:
            play=self.config['icon']['ran1']
        else:
            play=f"{self.dirname}images\\play.png"
            
        
        if "pause" in self.config['icon']:
            pause=self.config['icon']['pause']
        else:
            pause=f"{self.dirname}images\\pause.png"
            
        
        if "next" in self.config['icon']:
            next=self.config['icon']['next']
        else:
            next=f"{self.dirname}images\\nex.png"
            
        
        if "pre" in self.config['icon']:
            pre=self.config['icon']['pre']
        else:
            pre=f"{self.dirname}images\\pre.png"
            
        
        if "search" in self.config['icon']:
            search=self.config['icon']['search']
        else:
            search=f"{self.dirname}images\\search.png"
            
            
        if "del" in self.config['icon']:
            dele=self.config['icon']['del']
        else:
            dele=f"{self.dirname}images\\del.png"
            
        
        if "imp" in self.config['icon']:
            imp=self.config['icon']['imp']
        else:
            imp=f"{self.dirname}images\\imp.png"
            
        
        if "mini" in self.config['icon']:
            mini=self.config['icon']['mini']
        else:
            mini=f"{self.dirname}images\\mini.png"
            
            
        
        if "ext" in self.config['icon']:
            ext=self.config['icon']['ext']
        else:
            ext=f"{self.dirname}images\\extend.png"
            
        
        if "minimize" in self.config['icon']:
            minimize=self.config['icon']['minimize']
        else:
            minimize=f"{self.dirname}images\\minim.png"
            
        
        
        if "pop" in self.config['icon']:
            pop=self.config['icon']['pop']
        else:
            pop=f"{self.dirname}images\\pop.png"
            
            
        if "set" in self.config['icon']:
            sett=self.config['icon']['set']
        else:
            sett=f"{self.dirname}images\\set.png"
            
        if "mute" in self.config['icon']:
            mute=self.config['icon']['mute']
        else:
            mute=f"{self.dirname}images\\mute.png"
        
        if "sound" in self.config['icon']:
            sound=self.config['icon']['sound']
        else:
            sound=f"{self.dirname}images\\sound.png"
            
            
        if "stop" in self.config['icon']:
            stop=self.config['icon']['stop']
            
            print(stop)
        else:
            stop=f"{self.dirname}images\\stop.png"
            print(stop)
            
        if "close" in self.config['icon']:
            close=self.config['icon']['close']
        else:
            close=f"{self.dirname}images\\close.png"
            
        if "minim" in self.config['icon']:
            minim=self.config['icon']['minim']
        else:
            minim=f"{self.dirname}images\\minim.png"
        self.writeconfig()
        # except:
            # #首次
            # self.config.add_section('icon')#首次会新建icon这一项
            # ran1=f"{self.dirname}images\\suf.png"
            
            
            # self.config['icon']['ran1']=ran1

            # ran2=f"{self.dirname}images\\pro.png"
            # self.config['icon']['ran2']=ran2

            # play=f"{self.dirname}images\\play.png"
            # self.config['icon']['ran1']=play

            # pause=f"{self.dirname}images\\pause.png"
            # self.config['icon']['pause']=pause

            # next=f"{self.dirname}images\\next.png"
            # self.config['icon']['next']=next


            # pre=f"{self.dirname}images\\pre.png"
            # self.config['icon']['pre']=pre

            # search=f"{self.dirname}images\\search.png"
            # self.config['icon']['search']=search

            # dele=f"{self.dirname}images\\del.png"
            # self.config['icon']['del']=dele


            # imp=f"{self.dirname}images\\imp.png"
            # self.config['icon']['imp']=imp


            # mini=f"{self.dirname}images\\mini.png"
            
            # self.config['icon']['mini']=mini
            # ext=f"{self.dirname}images\\extend.png"
            # self.config['icon']['ext']=ext
            # minimize=f"{self.dirname}images\\minim.png"
            # self.config['icon']['minimize']=minimize
            # pop=f"{self.dirname}images\\pop.png"
            # self.config['icon']['pop']=pop
            
            # sett=f"{self.dirname}images\\set.png"
            # self.config['icon']['set']=sett
            
            # mute=f"{self.dirname}images\\mute.png"
            # self.config['icon']['set']=mute
            
            # sound=f"{self.dirname}images\\sound.png"
            # self.config['icon']['set']=sound
            
            # stop=f"{self.dirname}images\\stop.png"
            # self.config['icon']['stop']=stop
            # self.writeconfig()
        
        self.ran1=QtGui.QIcon()
        self.ran1.addPixmap(QtGui.QPixmap(ran1), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        
        self.ran2=QtGui.QIcon()
        self.ran2.addPixmap(QtGui.QPixmap(ran2), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ranser.setIcon(self.ran2)
        size = QSize(32, 32)
        self.ranser.setIconSize(size)
        
        self.closeic=QtGui.QIcon()
        self.closeic.addPixmap(QtGui.QPixmap(close), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closebtn.setIcon(self.closeic)
        size = QSize(32, 32)
        self.closebtn.setIconSize(size)
        
        
        self.minimic=QtGui.QIcon()
        self.minimic.addPixmap(QtGui.QPixmap(minim), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minim.setIcon(self.minimic)
        size = QSize(32, 32)
        self.minim.setIconSize(size)
            
        self.playic=QtGui.QIcon()
        self.playic.addPixmap(QtGui.QPixmap(play), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.pauseic=QtGui.QIcon()
        self.pauseic.addPixmap(QtGui.QPixmap(pause), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play.setIcon(self.pauseic)
        size = QSize(64, 64)
        self.play.setIconSize(size)
        #默认是否为自动播放,懒,之后configparse补上
        
        self.nexic=QtGui.QIcon()
        self.nexic.addPixmap(QtGui.QPixmap(next), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next.setIcon(self.nexic)
        size = QSize(32, 32)
        self.next.setIconSize(size)
        self.preic=QtGui.QIcon()
        self.preic.addPixmap(QtGui.QPixmap(pre), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pre.setIcon(self.preic)
        size = QSize(32, 32)
        self.pre.setIconSize(size)
        self.searchic=QtGui.QIcon()
        self.searchic.addPixmap(QtGui.QPixmap(search), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.serinput.setIcon(self.searchic)
        self.searchic1=QtGui.QIcon()
        self.searchic1.addPixmap(QtGui.QPixmap(search), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.serbtn.setIcon(self.searchic1)
        self.plsbtn.setIcon(self.searchic1)
        size = QSize(24, 24)
        self.serbtn.setIconSize(size)
        self.plsbtn.setIconSize(size)
        self.delic=QtGui.QIcon()
        self.delic.addPixmap(QtGui.QPixmap(dele), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delbtn.setIcon(self.delic)
        self.importic=QtGui.QIcon()
        self.importic.addPixmap(QtGui.QPixmap(imp), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.importbtn.setIcon(self.importic)
        self.miniic=QtGui.QIcon()
        self.miniic.addPixmap(QtGui.QPixmap(mini), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mini.setIcon(self.miniic)
        size = QSize(32, 32)
        self.mini.setIconSize(size)
        self.extendic=QtGui.QIcon()
        self.extendic.addPixmap(QtGui.QPixmap(ext), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.muteic=QtGui.QIcon()
        self.muteic.addPixmap(QtGui.QPixmap(mute), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.soundic=QtGui.QIcon()
        self.soundic.addPixmap(QtGui.QPixmap(sound), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.stopic=QtGui.QIcon()
        self.stopic.addPixmap(QtGui.QPixmap(stop), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopbtn.setIcon(self.stopic)
        size = QSize(64, 64)
  

        self.stopbtn.setIconSize(size)
        
        
        
        self.tog0y.setIcon(self.extendic)
        self.disa1.setIcon(self.extendic)
        self.dis3.setIcon(self.extendic)
        
    
        self.togic=QtGui.QIcon()
        self.togic.addPixmap(QtGui.QPixmap(minimize), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.tog2.setIcon(self.togic)
        self.tog0.setIcon(self.togic)
        self.tog3.setIcon(self.togic)
        self.tog1.setIcon(self.togic)
        

        
        
        self.popup=QtGui.QIcon()
        self.popup.addPixmap(QtGui.QPixmap(pop), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.jump.setIcon(self.popup)
        self.setic=QtGui.QIcon()
        self.setic.addPixmap(QtGui.QPixmap(sett), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.set.setIcon(self.setic)
        self.mutebtn.setIcon(self.soundic)  
        size = QSize(32, 32)
        self.mutebtn.setIconSize(size)
        
    def opendialogwin(self):
        try:
            self.timer2.stop()
            self.timer2.deleteLater()
        except:
            pass
        
        dialog=QDialog()
        # self.t1.stop()
        # self.t1.deleteLater()
        dialog.ui = Settings()
        
        dialog.ui.setupUi(dialog)
        dialog.closeEvent=self.closeevent
        dialog.show()
        dialog.exec_()
    
    def closeevent(self,event):
        self.config.read(f'{self.dirname}settings.ini')
        pic,saver,skin,down='0','0','0','0'
        if "pic" in self.config['DEFAULT']:
            pic=self.config['DEFAULT']['pic']
        if "saver" in self.config['DEFAULT']:
            saver=self.config['DEFAULT']['saver']
        if "skinconfig" in self.config['DEFAULT']:
            skin=self.config['DEFAULT']['skinconfig']
        if "downpath" in self.config['DEFAULT']:
            down=self.config['DEFAULT']['downpath']
        if pic!='0':
            self.picchange(self.config['DEFAULT']['pic'])
        if saver!='0':        
            self.scrsaver(self.config['DEFAULT']['saver'])
        if skin!='0':
            pass#皮肤之后会讲,大家不要着急
        
        if down!='0':
            pass#涉及有些音乐下载功能已经烂大街基本照抄了,
                # 所以爬虫那块我不会讲,但其实有地方直接抄,
                # 这提示已经很够了....
                # 会在之后简单带一下selenium
        
        self.activateicon()
        self.styleconfig()
        
    def checksettingfile(self):
        if os.path.exists(f'{self.dirname}settings.ini'):
            pass
        else:
            self.config['DEFAULT']['pic']='0'
            self.config['DEFAULT']['saver']='0'
            self.config['DEFAULT']['downpath']='0'
            self.config['DEFAULT']['skinconfig']='0'
            
            self.writeconfig()
    
    def writeconfig(self):
        with open(f'{self.dirname}settings.ini','w') as f:
            self.config.write(f)
        
        
    def folderloop(self,folder):
        for root,d,f in os.walk(folder):
            for i in f:
                if i.endswith('.jpg'):
                    fullname=os.path.join(root,i)
                elif i.endswith('.gif'):
                    fullname=os.path.join(root,i)
                elif i.endswith('.png'):
                    fullname=os.path.join(root,i)
                self.t1=QTimer()
                self.t1.start(2500)
                self.t1.timeout.connect(lambda:self.picchange1(fullname))
    def scrsaver(self,folder):
        
        for root,dirs,files in os.walk(folder,topdown=False):
            
            root=str(root)
            
            filenames=[os.path.join(root,i) for i in files]
            rang=len(filenames)
            
            self.rang=rang-1
            self.rang2=rang-1
            
            self.timer2=QTimer()    
            
            self.timer2.start(2000)
            self.timer2.timeout.connect(lambda:self.picchange1(filenames[self.rang]))

    def picchange1(self,filename):
                print(filename)
                self.rang-=1
                
                self.wallp.setPixmap(QPixmap(filename))
     
                if self.rang==0:
                    self.rang=self.rang2
                
    def picchange(self,filename):
        self.wallp.setPixmap(QPixmap(filename))
        
        self.timer1=QTimer()
        self.timer1.start(1)
        self.timer1.timeout.connect(lambda:self.status1(5))
        
    

    
    def importfile(self):
        filex , check = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()",
                                               "", "All Files (*);;音乐文件 (*.mp3,*.wmv)")
        if check:
            print(filex)
        
        path = Path(filex)
        filename=path.name
        # filenamewithout=path.stem
        
        from mutagen.id3 import ID3
        from mutagen.mp3 import MP3
        tags = ID3(filex)
        # length=MP3(filex).info.length
        # duration=self.audio_duration(length)
        
        # self.length=f'{str(duration[1]).zfill(2)}:{str(duration[3]).zfill(2)}:{str(duration[5]).zfill(2)}'
        # print(self.length)
        try:
            pict = tags.get("APIC:").data
        except:
            pict=b''
        import music_tag
        f = music_tag.load_file(filex)
        
        try:
            songname=str(f['tracktitle'])
        except:
            
            f['tracktitle']=filex.split('.')[0]
            songname=str(f['tracktitle'])
    
        data=(songname,)
        # length=f['length']
        
        artisttag=True
        albumtag=True
        lytag=True
        try:
            artist=str(f['artist'])
        except:
            artisttag=False
        try:
            album=str(f['album'])
        except:
            albumtag=False            
        try:
            lyric=f['lyric']
        
        except:
            lytag=False
            
        if artisttag==False or albumtag==False or lytag==False:#
            self.searchlyric(songname)
            
            self.data=()
            self.data=self.data+data
            print(self.data)
        else:
            data+=(artist,album,pict,filex,lyric)
        print(data)
        # self.insertdb(data)
 
    
    # 改成实时获取时长,这个没有必要写在数据库里
    # def audio_duration(self,length):
    #     hours = length // 3600  # calculate in hours
    #     hours1=int(hours)
    #     length %= 3600
        
    #     mins = length // 60  # calculate in minutes
    #     length %= 60
    #     mins1=int(mins)
    #     seconds = length  # calculate in seconds
    #     seconds1=int(seconds)
    #     return hours,hours1, mins,mins1, seconds,seconds1  # returns the duration
        

    
    def searchlyric(self,songname):
        print('here')
        self.timer4=QTimer()
        self.timer4.start(1)
        self.timer4.timeout.connect(lambda:self.searchword(songname))
        
    def searchword(self,songname):
        artist,album,lyric=opensele(songname)
        print(artist,album,lyric)

        self.data=self.data+(artist,album,lyric)
        print(self.data)#这里代码会在之后会有所改动,敬请留意
        self.timer4.stop()
        self.timer4.deleteLater()
        
    def loading(self):
        #关于qthread的内容......
        print('searching')
        # keyword=song_get(self.lineEdit.text())
        
    
    
#2####################################################################################    
    def coverplace(self,picture):#封面显示
        self.cover.setPixmap(QPixmap(picture))
    
    def sqlconn(self):
        # conn = pymysql.connect(host='localhost', port=3306, user='root', password="123456", db="tb1")
        conn = sqlite3.connect(f'{self.dirname}admin.db')
        return conn
    def testup(self):
        try:
            self.readdb()
        except:
            self.createdb()
        if not os.path.isfile(f'{self.dirname}settings.ini'):
            self.config=configparser.ConfigParser()
            self.config['DEFAULT']={'pic':'0','saver':'0','down':'0','skinpath':'0'}
            

            
            
    def createdb(self):
        # try:
        conn=self.sqlconn()
        cur=conn.cursor()
        sql="""CREATE TABLE "song" (
	"id"	INTEGER,
	"songname"	TEXT,
	"name"	TEXT,
	"album"	TEXT,
	"timelength"	TEXT,
	"cover"	TEXT,
	"lyricpath"	TEXT,
	"filepath"	TEXT,
	"lyric"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);"""
        cur.execute(sql)
        
        self.timer1=QTimer()
        self.timer1.timeout.connect(lambda :self.status1(3))
        self.timer1.start(1)
        # except:
        #     self.timer1=QTimer()
        #     self.timer1.timeout.connect(lambda :self.status1(4))
        #     self.timer1.start(1)
        cur.close()
            
    def readdb(self):
        try:
            conn = self.sqlconn()

            cur = conn.cursor()
            
            sql="select songname,name,album,lyricpath,cover,filepath from 'song'"
        
            cur.execute(sql)
            self.listdata=cur.fetchall()
            
            self.playlist.setRowCount(len(self.listdata[0]))
            
            y=0
            self.namelist=[]
            self.musiclist=[]
            for i in self.listdata:
                x=0
                for j in i:
                    if x==0:
                        self.namelist.append(j)
                        self.playlist.setItem(y,x,QtWidgets.QTableWidgetItem(str(j)))
                    elif x==4:
                        try:
                            picture=QPixmap()
                            picture.loadFromData(QByteArray.fromBase64(j))
                            picture.scaled(32, 32)
                            self.playlist.setItem(y,5,picture)
                        except:
                            pass                    
                        #j是cover的数据,里面就是存放的图片的blob,其实应该再tag里面找,这里只是测试
                    elif x==3:
                        pass# 歌词暂且略过
                    
                    
                    elif x==5:
                        self.musiclist.append(j)
                    # 这个是把封面放到列表,也可在别的地方显示
                    
                    else:
                        self.playlist.setItem(y,x,QtWidgets.QTableWidgetItem(str(j)))


                    print(f'column{x},row{y},值:{j}')
                    x+=1
                y+=1
        except:     
            self.timer1=QTimer()
            self.timer1.timeout.connect(lambda :self.status1(7))
            self.timer1.start(1)

    def insertdb(self,i):
        conn = self.sqlconn1()

        cur = conn.cursor()
        sql = """insert into 'song' ("songname","name","album","lyricpath","cover","filepath") values (?,?,?,?,
                                                    ?,?)"""

        try:
      
            cur.execute(sql,i)
            conn.commit()
            self.timer1=QTimer()
            self.timer1.timeout.connect(lambda :self.status1(1))
            self.timer1.start(1)
        except:
            self.timer1=QTimer()
            self.timer1.timeout.connect(lambda :self.status1(2))
            self.timer1.start(1)
            conn.rollback()
        self.readdb()
   
    
    def deldb(self):
        id=self.playlist.selectedItems()[0].text()
        # file=self.tableWidget.selectedItems()[1].text()
        
        try:
            # os.remove(file)#删除文件
            pass
        except:
            self.timer1=QTimer()
            self.timer1.timeout.connect(lambda :self.status1(6))
            self.timer1.start(1)
            return
        conn = self.sqlconn1()        
        cur = conn.cursor()
        

        sql = f"delete from 'tb1' where 序号={id}"

        cur.execute(sql)
        conn.commit()
        conn.close()
    
        self.readdb()
    
    def status1(self,a):
        if a==1:
            self.status.setText('音乐文件已导入')
            
        elif a==2:
            self.status.setText('导入失败')
            
        elif a==3:
            self.status.setText('播放列表创建成功')
            
        elif a==4:
            self.status.setText('列表创建失败')
        
        elif a==5:
            self.status.setText('图片已导入')
        elif a==6:
            self.status.setText('文件无法删除')
        elif a==7:
            self.status.setText('暂未有音乐文件导入')
        elif a==8:
            self.status.setText('音乐无法播放')
        elif a==9:
            self.status.setText(self.cursongname)
        elif a==10:
            self.status.setText('')
        elif a==11:
            self.status.setText('')
        elif a==12:
            self.status.setText('')
        elif a==13:
            self.status.setText('')
        elif a==14:
            self.status.setText('')
        elif a==15:
            self.status.setText('')
        elif a==16:
            self.status.setText('')
        elif a==17:
            self.status.setText('')
        elif a==18:
            self.status.setText('')
        elif a==19:
            self.status.setText('')
        elif a==20:
            self.status.setText('')
        elif a==21:
            self.status.setText('')
        elif a==22:
            self.status.setText('')
        self.timer1.stop()
        self.timer1.deleteLater()
        pass
#3####################################################################################    
    def setvolume(self):
        
        self.volume=self.volm.value()
        if self.volume > 0 and self.mute == True:
            self.mutesong()  
        mixer.music.set_volume(self.volume/100)
    def mutesong(self):
        _translate = QtCore.QCoreApplication.translate
        if self.mute == False:
            mixer.music.set_volume(0.0)
            self.mutebtn.setIcon(self.muteic)
            self.mutebtn.setToolTip(_translate("Mute", "静音"))
            self.volm.setValue(0)
            self.mute = True
        else:
            self.mutebtn.setIcon(self.soundic)   
            self.mutebtn.setToolTip(_translate("Unmute", "有声"))
            self.volm.setValue(70)
            self.mute = False
            
    
#2####################################################################################    
    def shuffleplaylist(self):
        # self.readdb()
        if self.ransw == True:
            self.ranser.setIcon(self.ran1)
            self.ramdomlist=[]
            self.ransw=False
            self.playsong()
        else:
            
            self.randomlist=[i for i in self.musiclist]
            #千万不要用 self.randomlist=self.musiclist 因为会直接从指针层面把两个挂钩,连个列表同生共死
            random.shuffle(self.randomlist)
            self.ranser.setIcon(self.ran2)      
            self.playsong()
            self.ransw=True
    
    
    
    def playsong(self):
        # 按play按钮的功能
        if self.randomlist==[]:
            self.musiclist1=[i for i in self.musiclist]
        else:
            self.musiclist1=[i for i in self.randomlist]

        
        self.musictimer = QTimer()
        self.musictimer.setInterval(1000)
        self.musictimer.timeout.connect(self.updateslider)
        self.index = self.playlist.currentRow()
        if self.playsw == False:
            if current_song == self.index:
                self.playsw = True
                self.play.setIcon(self.playic)
                # self.playtimer=QTimer()
                self.musictimer.start()
                mixer.music.unpause()

            else:   
                try:
                    self.count=0
                    mixer.music.load(self.musiclist1[self.index])
                    
                    self.current_song=self.index
                    f=music_tag.load_file(self.musiclist1[self.index])
                    
                    try:
                        self.cursongname=str(f['tracktitle'])
                    except:    
                        path = Path(self.musiclist1[self.index])
                        self.cursongname=path.name
                        
                        pass
                    
                    self.timer5=QTimer()
                    self.timer5.timeout.connect(lambda:self.status1(9))
                    self.timer5.start()
                    mixer.music.play()
                    # self.load_lyric()
                    self.play.setIcon(self.pauseic)
                    current_song = self.index
                    
                    sound = MP3(str(self.musiclist1[self.index]))
                    songLength = sound.info.length
                    self.songLength =round(self.songLength)
                    hours=0
                    min,sec=divmod(songLength,60)
                    if min>59:
                        hours,min=divmod(min,60)
                        min=min%60
                    self.total.setText(f"/ {str(hours).zfill(2)}:{str(min).zfill(2)}:{str(sec).zfill(2)}")
                    self.slider.setMaximum(songLength)
                    self.musictimer.start()
                except:
                    self.timer5=QTimer()
                    self.timer5.start()
                    self.timer5.timeout.connect(self.status1(8))
                    
            self.playsw = True        
        elif self.playsw ==True:
            self.playsw = False
            self.play.setIcon(self.pauseic)
            self.timer.stop()
            mixer.music.pause()        
    
    def previoussong(self):
        if self.musiclist1==[]:
            self.musiclist1=[i for i in self.musiclist]#预防第一次打开就按上一首,虽然是不可能可以成功播放的,而且默认是顺序播放的,所以一定是self.musiclist
        
        
            # 很绕,意思是 从randomlist找到musiclist[self.index]的需要
        try:
            self.musictimer.stop()
            self.musictimer.deleteLater()
        except:
            pass    
        if self.index ==0:
            self.timer7=QTimer()
            self.timer7.timeout.connect(lambda:self.status1(11))
            pass
        else:
            self.index-=1    
        
        if self.ransw==True:
            self.index=self.musiclist1.index(self.musiclist[self.index])
            #因为读取的播放列表是顺序的,
            # 所以当随机播放的时候self.index
            # 是不等于顺序播放时的self.index,
            # 我们就得用这个方法,重新找到这个行
        self.playlist.selectRow(self.index)
        self.songname=self.namelist[self.index]
        self.timer=QTimer()
        self.timer.timeout.connect(lambda:self.status1(14))
        self.timer.start()
        try:
            self.count = 0
            mixer.music.load(self.musiclist1[self.index])
            # self.load_lyric()#读取歌词部分带有爬虫我们下下章在完善
            self.play.setIcon(self.pauseic)
            self.musictimer=QTimer()
            self.musictimer.timeout.connect(self.updateslider())
            self.musictimer.start()
            sound = MP3(self.musiclist1[self.index])
            self.songLength = sound.info.length
            self.songLength =round(self.songLength)
            hours=0
            min,sec=divmod(self.songLength,60)
            if min>59:
                hours,min=divmod(min,60)
                min=min%60
            self.total.setText(f"/ {str(hours).zfill(2)}:{str(min).zfill(2)}:{str(sec).zfill(2)}")

            self.slider.setMaximum(self.songLength)
            mixer.music.play()
        except:
            pass 
    def nextsong(self):  
        if self.musiclist1==[]:#如果刚打开没有按播放而是按next,self.musiclist1肯定是空的,所以得做一次赋值
            self.musiclist1=self.musiclist
            self.index=1
            
        try:
            self.musictimer.stop()
            self.musictimer.deleteLater()
        except:
            pass
        if self.index ==len(self.musiclist1)-1:#最后一首的时候回归成第一个
            self.index = 0
        else:
            self.index+=1    
        music=self.musiclist1[self.index]
        self.songname=self.musiclist1[self.index]
        
        
        
        if self.ransw==True:
            self.index1=self.musiclist1.index(self.musiclist[self.index])
            #因为读取的播放列表是顺序的,
            # 所以当随机播放的时候self.index
            # 是不等于顺序播放时的self.index,
            # 我们就得用这个方法,重新找到这个行

        
        self.playlist.selectRow(self.index)
        
        try:
            self.count = 0
            mixer.music.load(music)
            # self.load_lyric()
            mixer.music.play()
            self.play.setIcon(self.pauseic)
            self.timer.start()
            sound = MP3(str(music))
            songLength = sound.info.length
            self.songLength =round(songLength)
            hours=0
            min,sec=divmod(self.songLength,60)
            if min>59:
                hours,min=divmod(min,60)
                min=min%60
            self.total.setText(f"/ {str(hours).zfill(2)}:{str(min).zfill(2)}:{str(sec).zfill(2)}")

            self.slider.setMaximum(self.songLength)
    
        except:
            pass       
    def updateslider(self):
        
        self.count +=1
        self.slider.setValue(self.count)
        self.time1.setText(time.strftime("%H:%M:%S",time.gmtime(self.count)))
        if self.count == self.songLength:
            # self.musictimer.stop()
            # self.musictimer.deleteLater()
            self.nextsong()
    
    
    def slidersettime(self):
        self.time1.setText(time.strftime("%H:%M:%S",time.gmtime(self.slider.value())))
        mixer.music.set_pos(self.slider.value())


    
#1#############################################################################################
    def set2(self):
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(250, 30, 411, 421))
        # self.gridLayoutWidget_2.hide()
        pass
    
    def set3(self):
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(250, 30, 411, 421))
        # self.gridLayoutWidget_2.hide()
        pass
    def disa2(self):
        pass
    def toggle2(self):
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 681, 431))

        self.timer=QTimer()
        self.timer.setTimerType(Qt.PreciseTimer)
        self.timer.setInterval(1)
        self.timer.timeout.connect(self.smoothy2)
        self.timer.start()

    def toggle1(self):
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 681, 431))
        
        self.timer=QTimer()
        self.timer.setTimerType(Qt.PreciseTimer)
        self.timer.setInterval(1)
        self.timer.timeout.connect(self.smoothy2)
        self.timer.start()

    def toggle0(self):

        self.timer=QTimer()
        self.timer.setTimerType(Qt.PreciseTimer)
        self.timer.setInterval(1)
        self.timer.timeout.connect(self.smoothy1)
        self.timer.start()
        
    def smoothy1(self):
        
        if self.ena==True:
            self.a-=3
            self.playlist.resize(self.a, 241)
            if self.a<1:
                self.a=0
                

                self.ena=False
                self.timer.stop()
                self.timer.deleteLater()
                self.playlist.hide()

        if self.ena==False:

            if self.a!=0:
                self.playlist.show()
            self.a+=1
            self.playlist.resize(self.a, 241)
            if self.a>219:
                self.a=221
                self.ena=True
                self.timer.stop()
                self.timer.deleteLater()
    
    
    def smoothy1(self):
        
        if self.ena==True:
            self.a-=3
            self.playlist.resize(self.a, 241)
            if self.a<1:
                self.a=0
                

                self.ena=False
                self.timer.stop()
                self.timer.deleteLater()
                self.playlist.hide()

        if self.ena==False:

            if self.a!=0:
                self.playlist.show()
            self.a+=1
            self.playlist.resize(self.a, 241)
            if self.a>219:
                self.a=221
                self.ena=True
                self.timer.stop()
                self.timer.deleteLater()
                
    def smoothy2(self):
        
        if self.ena==True:
            self.a-=3
            self.playlist.resize(self.a, 241)
            if self.a<1:
                self.a=0
                

                self.ena=False
                self.timer.stop()
                self.timer.deleteLater()
                self.playlist.hide()

        if self.ena==False:

            if self.a!=0:
                self.playlist.show()
            self.a+=1
            self.playlist.resize(self.a, 241)
            if self.a>219:
                self.a=221
                self.ena=True
                self.timer.stop()
                self.timer.deleteLater()
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    
    window=Ui_Form()
    window.show()
    sys.exit(app.exec_())
    
    # Form = QtWidgets.QWidget()
    # ui = Ui_Form()
    
    # ui.setupUi(self)
    
    # Form.setMouseTracking(True)

    # Form.show()
    # sys.exit(app.exec_())


