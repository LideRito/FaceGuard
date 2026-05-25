# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_Main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QStackedWidget, QStatusBar, QToolButton,
    QVBoxLayout, QWidget)
from .resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"")
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        self.styleSheet.setCursor(QCursor(Qt.ArrowCursor))
        self.styleSheet.setAutoFillBackground(False)
        self.styleSheet.setStyleSheet(u"/* === Shared === */\n"
"QStackedWidget, QLabel, QPushButton, QRadioButton, QCheckBox,\n"
"QGroupBox, QStatusBar, QToolButton, QComboBox, QDialog {\n"
"\n"
"    font-size: 14px;\n"
"    font-family: \"Monospaced\";\n"
"}\n"
"\n"
"/* ////////////Bg App */\n"
"#contentTopBg {\n"
"	background-color:#181818;\n"
"}\n"
"#contentBottomBg{background-color:rgb(40, 44, 52);}\n"
"	\n"
"QSlider::groove:horizontal {\n"
"	height: 5px;\n"
"	border:0px;\n"
"	border-radius:6px;\n"
"	background:rgba(25, 113, 255, 100);\n"
"}\n"
"QSlider::groove:vertical {\n"
"	width: 5px;\n"
"	border:0px;\n"
"	border-radius:6px;\n"
"	background: #233EEF;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"	background: qlineargradient(x1:0, y1:0, x2:0.5, y2:0.5, stop:0 #233EEF, stop:1 #8f8f8f);\n"
"	border: 1px solid rgba(0, 0, 0, 50);\n"
"	width: 14px;\n"
"	margin: -5px 0;\n"
"	border-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"	background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"	border: 1px solid rgba(0, 0, 0, 50);\n"
"	height: 1"
                        "4px;\n"
"	margin: 0 -5px;\n"
"	border-radius: 4px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"    background: white;\n"
"}\n"
"QSlider::add-page:vertical {\n"
"    background: white;\n"
"}\n"
"/* === QToolButton === */\n"
"#moreModelBtn {\n"
"\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-radius: 7px;\n"
"	border-style: solid;\n"
"	color: #a9b7c6;\n"
"\n"
"	padding: 2px;\n"
"	background-color: rgb(50, 8, 2);\n"
"}\n"
"\n"
"#moreModelBtn:hover{\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-radius: 7px;\n"
"	border-style: solid;\n"
"	color:#FFFFFF;\n"
"	padding-bottom: 1px;\n"
"	background-color: rgb(227, 227, 227);\n"
"}\n"
"QMainWindow {\n"
"	background-color:#1e1d23;\n"
"}\n"
"#functionsBox .QPushButton{\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
""
                        "	border-left-color: transparent;\n"
"	border-bottom-color: transparent;\n"
"	border-width: 3px;\n"
"	border-style: solid;\n"
"	border-color: rgb(60, 63, 65);\n"
"    border-radius: 7px;\n"
"	font-weight: bold;\n"
"   font-size: 14px;\n"
"	color: rgb(245,245,220);\n"
"	padding: 2px;\n"
"	background-color: rgb(45, 38, 33);\n"
"}\n"
"#functionsBox .QPushButton::hover{\n"
"	border-style: inset;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: transparent;\n"
"	border-color: yellow;\n"
"	border-width: 2px;\n"
"	color: #a9b7c6;\n"
"   font-size: 15px;\n"
"	padding: 2px;\n"
"	background-color: #1e1d23;\n"
"}\n"
"#startAnonBtn{\n"
"   color: #a9b7c6;\n"
"   font-size:14px;\n"
"}\n"
"#topInfo { font: 63 12pt \"Segoe UI Semibold\"; color:rgb(255,251,240); font-style: italic}\n"
"\n"
"#contentMidBg {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#functionsBox{\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#functionsBox .QLabel, QCheckBox{\n"
"	color: rgb(221, 221, 221);\n"
"\n"
"}\n"
"#functionsBox .QFrame{\n"
"	background-color: rgb(51, 51, 5"
                        "1);\n"
"	border-radius: 14px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border-width: 1px; border-radius: 4px;\n"
"	border-color: rgb(58, 58, 58);\n"
"	border-style: inset;\n"
"	padding: 0 8px;\n"
"	color: #a9b7c6;\n"
"	background:#1e1d23;\n"
"	selection-background-color:#007b50;\n"
"	selection-color: #FFFFFF;\n"
"}\n"
"QCheckBox {\n"
"	color: #a9b7c6;\n"
"	padding: 2px;\n"
"}\n"
"QCheckBox:disabled {\n"
"	color: #808086;\n"
"	padding: 2px;\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"	border-radius:4px;\n"
"	border-style:solid;\n"
"	padding-left: 1px;\n"
"	padding-right: 1px;\n"
"	padding-bottom: 1px;\n"
"	padding-top: 1px;\n"
"	border-width:1px;\n"
"	border-color: rgb(87, 97, 106);\n"
"	background-color:#1e1d23;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #04b97f;\n"
"	color: #a9b7c6;\n"
"	background-color: #04b97f;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:sol"
                        "id;\n"
"	border-width: 1px;\n"
"	border-color: #04b97f;\n"
"	color: #a9b7c6;\n"
"	background-color: transparent;\n"
"}\n"
"QComboBox {\n"
"	color: #a9b7c6;\n"
"	background: #1e1d23;\n"
"}\n"
"QComboBox:editable {\n"
"	background: #1e1d23;\n"
"	color: #a9b7c6;\n"
"	selection-background-color: #1e1d23;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: #a9b7c6;\n"
"	background: #1e1d23;\n"
"	selection-color: #FFFFFF;\n"
"	selection-background-color: #1e1d23;\n"
"}\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"	color: #a9b7c6;\n"
"	background: #1e1d23;\n"
"}\n"
"#videoSettingsBox {\n"
"	border-radius: 4px;\n"
"	border-color: #1e1d23;\n"
"}\n"
"\n"
"#videoInfoBox {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-width: 2px;\n"
"	border-color: rgb(60, 63, 65);\n"
"	border-style: solid;\n"
"	border-radius: 7px;\n"
"}\n"
"#videoInfoBox .QLabel {\n"
"	color: rgb(221, 221, 221);}\n"
"#faceInfoBox{\n"
"background-color: rgb(33, 37, 43);\n"
"	border-width: 2px;\n"
"	border-color: rgb(60, 63, 65)"
                        ";\n"
"	border-style: solid;\n"
"	border-radius: 7px;\n"
"}\n"
"#faceInfoBox .QLabel {\n"
"	color: rgb(221, 221, 221)}")
        self.appLayout = QVBoxLayout(self.styleSheet)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.bgAPP = QFrame(self.styleSheet)
        self.bgAPP.setObjectName(u"bgAPP")
        self.bgAPP.setFrameShape(QFrame.StyledPanel)
        self.bgAPP.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.bgAPP)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentBox = QFrame(self.bgAPP)
        self.contentBox.setObjectName(u"contentBox")
        self.verticalLayout_3 = QVBoxLayout(self.contentBox)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        sizePolicy.setHeightForWidth(self.rightButtons.sizePolicy().hasHeightForWidth())
        self.rightButtons.setSizePolicy(sizePolicy)
        self.rightButtons.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_6 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.appLogo = QLabel(self.rightButtons)
        self.appLogo.setObjectName(u"appLogo")
        self.appLogo.setMinimumSize(QSize(0, 50))
        self.appLogo.setMaximumSize(QSize(50, 1677215))

        self.horizontalLayout_6.addWidget(self.appLogo)

        self.topInfo = QLabel(self.rightButtons)
        self.topInfo.setObjectName(u"topInfo")

        self.horizontalLayout_6.addWidget(self.topInfo)


        self.horizontalLayout.addWidget(self.rightButtons)

        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy)
        self.leftBox.setMaximumSize(QSize(16777215, 16777215))
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_19)



        self.minimizeBtn = QPushButton(self.leftBox)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        self.minimizeBtn.setMinimumSize(QSize(0, 0))
        self.minimizeBtn.setMaximumSize(QSize(28, 28))
        self.minimizeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon1)
        self.minimizeBtn.setIconSize(QSize(20, 20))
        self.minimizeBtn.setFlat(True)

        self.horizontalLayout_3.addWidget(self.minimizeBtn)

        self.maximizeBtn = QPushButton(self.leftBox)
        self.maximizeBtn.setObjectName(u"maximizeBtn")
        self.maximizeBtn.setMinimumSize(QSize(0, 0))
        self.maximizeBtn.setMaximumSize(QSize(28, 28))
        self.maximizeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/images/icons/icon_restore.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeBtn.setIcon(icon2)
        self.maximizeBtn.setIconSize(QSize(20, 20))
        self.maximizeBtn.setFlat(True)

        self.horizontalLayout_3.addWidget(self.maximizeBtn)

        self.closeAppBtn = QPushButton(self.leftBox)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(0, 0))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon3)
        self.closeAppBtn.setIconSize(QSize(20, 20))
        self.closeAppBtn.setFlat(True)

        self.horizontalLayout_3.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.leftBox)


        self.verticalLayout_3.addWidget(self.contentTopBg)

        self.contentMidBg = QFrame(self.contentBox)
        self.contentMidBg.setObjectName(u"contentMidBg")
        self.contentMidBg.setMaximumSize(QSize(16777215, 16777215))
        self.contentMidBg.setFrameShape(QFrame.StyledPanel)
        self.contentMidBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.contentMidBg)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.mediaPlayerBox = QFrame(self.contentMidBg)
        self.mediaPlayerBox.setObjectName(u"mediaPlayerBox")
        self.mediaPlayerBox.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.mediaPlayerBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.videoWid = QVideoWidget(self.mediaPlayerBox)
        self.videoWid.setObjectName(u"videoWid")
        self.videoWid.setMinimumSize(QSize(0, 0))
        self.videoWid.setBaseSize(QSize(800, 400))

        self.verticalLayout_4.addWidget(self.videoWid)

        self.videoProgressBox = QWidget(self.mediaPlayerBox)
        self.videoProgressBox.setObjectName(u"videoProgressBox")
        self.videoProgressBox.setMaximumSize(QSize(16777215, 32))
        self.progressBox = QHBoxLayout(self.videoProgressBox)
        self.progressBox.setObjectName(u"progressBox")
        self.progressSlider = QSlider(self.videoProgressBox)
        self.progressSlider.setObjectName(u"progressSlider")
        self.progressSlider.setOrientation(Qt.Horizontal)

        self.progressBox.addWidget(self.progressSlider)

        self.progressText = QLineEdit(self.videoProgressBox)
        self.progressText.setObjectName(u"progressText")
        self.progressText.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.progressText.sizePolicy().hasHeightForWidth())
        self.progressText.setSizePolicy(sizePolicy2)
        self.progressText.setMaximumSize(QSize(150, 16777215))

        self.progressBox.addWidget(self.progressText)


        self.verticalLayout_4.addWidget(self.videoProgressBox)

        self.videoSettingsBox = QGroupBox(self.mediaPlayerBox)
        self.videoSettingsBox.setObjectName(u"videoSettingsBox")
        self.videoSettingsBox.setMaximumSize(QSize(16777215, 35))
        self.videoSettingsBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalLayout_4 = QHBoxLayout(self.videoSettingsBox)
        self.horizontalLayout_4.setSpacing(50)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.playVideoBtn = QPushButton(self.videoSettingsBox)
        self.playVideoBtn.setObjectName(u"playVideoBtn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.playVideoBtn.sizePolicy().hasHeightForWidth())
        self.playVideoBtn.setSizePolicy(sizePolicy3)
        self.playVideoBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/images/icons/cil-media-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.playVideoBtn.setIcon(icon4)
        self.playVideoBtn.setFlat(True)

        self.horizontalLayout_4.addWidget(self.playVideoBtn)

        self.openfileBtn = QPushButton(self.videoSettingsBox)
        self.openfileBtn.setObjectName(u"openfileBtn")
        sizePolicy3.setHeightForWidth(self.openfileBtn.sizePolicy().hasHeightForWidth())
        self.openfileBtn.setSizePolicy(sizePolicy3)
        self.openfileBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/images/icons/cil-folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.openfileBtn.setIcon(icon5)
        self.openfileBtn.setFlat(True)

        self.horizontalLayout_4.addWidget(self.openfileBtn)

        self.volumeBox = QHBoxLayout()
        self.volumeBox.setObjectName(u"volumeBox")
        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.volumeBox.addItem(self.horizontalSpacer_20)

        self.volumeText = QLabel(self.videoSettingsBox)
        self.volumeText.setObjectName(u"volumeText")
        sizePolicy.setHeightForWidth(self.volumeText.sizePolicy().hasHeightForWidth())
        self.volumeText.setSizePolicy(sizePolicy)
        self.volumeText.setLayoutDirection(Qt.LeftToRight)
        self.volumeText.setPixmap(QPixmap(u":/images/icons/cil-volume-high.png"))
        self.volumeText.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.volumeBox.addWidget(self.volumeText)

        self.volumeBar = QSlider(self.videoSettingsBox)
        self.volumeBar.setObjectName(u"volumeBar")
        sizePolicy3.setHeightForWidth(self.volumeBar.sizePolicy().hasHeightForWidth())
        self.volumeBar.setSizePolicy(sizePolicy3)
        self.volumeBar.setCursor(QCursor(Qt.PointingHandCursor))
        self.volumeBar.setValue(99)
        self.volumeBar.setOrientation(Qt.Horizontal)

        self.volumeBox.addWidget(self.volumeBar)


        self.horizontalLayout_4.addLayout(self.volumeBox)


        self.verticalLayout_4.addWidget(self.videoSettingsBox)


        self.horizontalLayout_5.addWidget(self.mediaPlayerBox)

        self.functionsBox = QFrame(self.contentMidBg)
        self.functionsBox.setObjectName(u"functionsBox")
        self.functionsBox.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.functionsBox)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.faceAnonBox = QFrame(self.functionsBox)
        self.faceAnonBox.setObjectName(u"faceAnonBox")
        self.faceAnonBox.setMaximumSize(QSize(16777215, 16777215))
        self.faceAnonBox.setFrameShape(QFrame.StyledPanel)
        self.faceAnonBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.faceAnonBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.faceAnonBtn = QPushButton(self.faceAnonBox)
        self.faceAnonBtn.setObjectName(u"faceAnonBtn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.faceAnonBtn.sizePolicy().hasHeightForWidth())
        self.faceAnonBtn.setSizePolicy(sizePolicy4)
        self.faceAnonBtn.setMaximumSize(QSize(16777215, 45))
        self.faceAnonBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.faceAnonBtn.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.faceAnonBtn)

        self.faceAnonFuncBox = QFrame(self.faceAnonBox)
        self.faceAnonFuncBox.setObjectName(u"faceAnonFuncBox")
        self.horizontalLayout_8 = QHBoxLayout(self.faceAnonFuncBox)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.faceAnonText = QLabel(self.faceAnonFuncBox)
        self.faceAnonText.setObjectName(u"faceAnonText")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.faceAnonText.sizePolicy().hasHeightForWidth())
        self.faceAnonText.setSizePolicy(sizePolicy5)

        self.horizontalLayout_8.addWidget(self.faceAnonText)

        self.startAnonBtn = QPushButton(self.faceAnonFuncBox)
        self.startAnonBtn.setObjectName(u"startAnonBtn")
        self.startAnonBtn.setCursor(QCursor(Qt.PointingHandCursor))


        self.horizontalLayout_8.addWidget(self.startAnonBtn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.faceAnonFuncBox)
        self.anonStausBox = QFrame(self.faceAnonBox)
        self.anonStausBox.setObjectName(u"anonStausBox")
        self.anonStausBox.setFrameShape(QFrame.StyledPanel)
        self.anonStausBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.anonStausBox)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_24)

        self.anonStausText = QLabel(self.anonStausBox)
        self.anonStausText.setObjectName(u"anonStausText")

        self.horizontalLayout_25.addWidget(self.anonStausText)

        self.anonStaus = QLineEdit(self.anonStausBox)
        self.anonStaus.setObjectName(u"anonStaus")
        sizePolicy2.setHeightForWidth(self.anonStaus.sizePolicy().hasHeightForWidth())
        self.anonStaus.setSizePolicy(sizePolicy2)
        self.anonStaus.setMaximumSize(QSize(70, 16777215))
        self.anonStaus.setAlignment(Qt.AlignCenter)
        self.anonStaus.setReadOnly(True)

        self.horizontalLayout_25.addWidget(self.anonStaus)



        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_25)


        self.verticalLayout_2.addWidget(self.anonStausBox)

        self.faceModelChooseBox = QFrame(self.faceAnonBox)
        self.faceModelChooseBox.setObjectName(u"faceModelChooseBox")
        self.faceModelChooseBox.setFrameShape(QFrame.StyledPanel)
        self.faceModelChooseBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.faceModelChooseBox)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_7)

        self.CurrentFaceModelText = QLabel(self.faceModelChooseBox)
        self.CurrentFaceModelText.setObjectName(u"CurrentFaceModelText")

        self.horizontalLayout_12.addWidget(self.CurrentFaceModelText)

        self.faceModelChoices = QComboBox(self.faceModelChooseBox)
        self.faceModelChoices.setObjectName(u"faceModelChoices")
        self.faceModelChoices.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_12.addWidget(self.faceModelChoices)

        self.moreModelBtn = QToolButton(self.faceModelChooseBox)
        self.moreModelBtn.setObjectName(u"moreModelBtn")
        self.moreModelBtn.setCursor(QCursor(Qt.OpenHandCursor))

        self.horizontalLayout_12.addWidget(self.moreModelBtn)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_8)


        self.verticalLayout_2.addWidget(self.faceModelChooseBox)


        self.verticalLayout_5.addWidget(self.faceAnonBox)

        self.faceDetectBox = QFrame(self.functionsBox)
        self.faceDetectBox.setObjectName(u"faceDetectBox")
        self.faceDetectBox.setMaximumSize(QSize(16777215, 16777215))
        self.faceDetectBox.setFrameShape(QFrame.StyledPanel)
        self.faceDetectBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.faceDetectBox)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.faceDetectBtn = QPushButton(self.faceDetectBox)
        self.faceDetectBtn.setObjectName(u"faceDetectBtn")
        sizePolicy4.setHeightForWidth(self.faceDetectBtn.sizePolicy().hasHeightForWidth())
        self.faceDetectBtn.setSizePolicy(sizePolicy4)
        self.faceDetectBtn.setMaximumSize(QSize(16777215, 45))
        self.faceDetectBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.faceDetectBtn.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.faceDetectBtn)

        self.faceDetectFuncBox = QFrame(self.faceDetectBox)
        self.faceDetectFuncBox.setObjectName(u"faceDetectFuncBox")
        self.horizontalLayout_9 = QHBoxLayout(self.faceDetectFuncBox)
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)

        self.faceDetectText = QLabel(self.faceDetectFuncBox)
        self.faceDetectText.setObjectName(u"faceDetectText")

        self.horizontalLayout_9.addWidget(self.faceDetectText)

        self.faceDetectCBox = QCheckBox(self.faceDetectFuncBox)
        self.faceDetectCBox.setObjectName(u"faceDetectCBox")
        self.faceDetectCBox.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_9.addWidget(self.faceDetectCBox)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)


        self.verticalLayout_6.addWidget(self.faceDetectFuncBox)

        self.showOnVideoFuncBox = QFrame(self.faceDetectBox)
        self.showOnVideoFuncBox.setObjectName(u"showOnVideoFuncBox")
        self.showOnVideoFuncBox.setFrameShape(QFrame.StyledPanel)
        self.showOnVideoFuncBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.showOnVideoFuncBox)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_18)

        self.label = QLabel(self.showOnVideoFuncBox)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_22.addWidget(self.label)

        self.faceShowCBox = QCheckBox(self.showOnVideoFuncBox)
        self.faceShowCBox.setObjectName(u"faceShowCBox")

        self.horizontalLayout_22.addWidget(self.faceShowCBox)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_21)


        self.verticalLayout_6.addWidget(self.showOnVideoFuncBox)

        self.detectLenBox = QFrame(self.faceDetectBox)
        self.detectLenBox.setObjectName(u"detectLenBox")
        self.detectLenBox.setFrameShape(QFrame.StyledPanel)
        self.detectLenBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.detectLenBox)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_5)

        self.detectLenText = QLabel(self.detectLenBox)
        self.detectLenText.setObjectName(u"detectLenText")

        self.horizontalLayout_11.addWidget(self.detectLenText)

        self.detectLenChoices = QComboBox(self.detectLenBox)
        self.detectLenChoices.addItem("")
        self.detectLenChoices.addItem("")
        self.detectLenChoices.addItem("")
        self.detectLenChoices.setObjectName(u"detectLenChoices")
        self.detectLenChoices.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_11.addWidget(self.detectLenChoices)

        self.secondText = QLabel(self.detectLenBox)
        self.secondText.setObjectName(u"secondText")

        self.horizontalLayout_11.addWidget(self.secondText)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_6)


        self.verticalLayout_6.addWidget(self.detectLenBox)


        self.verticalLayout_5.addWidget(self.faceDetectBox)
        '''
        self.sceneAnalysisBox = QFrame(self.functionsBox)
        self.sceneAnalysisBox.setObjectName(u"sceneAnalysisBox")
        self.sceneAnalysisBox.setFrameShape(QFrame.StyledPanel)
        self.sceneAnalysisBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.sceneAnalysisBox)
        self.verticalLayout_7.setSpacing(1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.sceneAnalysisBtn = QPushButton(self.sceneAnalysisBox)
        self.sceneAnalysisBtn.setObjectName(u"sceneAnalysisBtn")
        sizePolicy4.setHeightForWidth(self.sceneAnalysisBtn.sizePolicy().hasHeightForWidth())
        self.sceneAnalysisBtn.setSizePolicy(sizePolicy4)
        self.sceneAnalysisBtn.setMaximumSize(QSize(16777215, 45))
        self.sceneAnalysisBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.sceneAnalysisBtn)

        self.sceneAnalysisFuncBox = QFrame(self.sceneAnalysisBox)
        self.sceneAnalysisFuncBox.setObjectName(u"sceneAnalysisFuncBox")
        self.horizontalLayout_10 = QHBoxLayout(self.sceneAnalysisFuncBox)
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_9)

        self.sceneAnalysisText = QLabel(self.sceneAnalysisFuncBox)
        self.sceneAnalysisText.setObjectName(u"sceneAnalysisText")

        self.horizontalLayout_10.addWidget(self.sceneAnalysisText)

        self.sceneAnalysisCbox = QCheckBox(self.sceneAnalysisFuncBox)
        self.sceneAnalysisCbox.setObjectName(u"sceneAnalysisCbox")
        self.sceneAnalysisCbox.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_10.addWidget(self.sceneAnalysisCbox)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_10)


        self.verticalLayout_7.addWidget(self.sceneAnalysisFuncBox)

        self.analysisLenBox = QFrame(self.sceneAnalysisBox)
        self.analysisLenBox.setObjectName(u"analysisLenBox")
        self.analysisLenBox.setFrameShape(QFrame.StyledPanel)
        self.analysisLenBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.analysisLenBox)
        self.horizontalLayout_14.setSpacing(6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_11)

        self.analysisLenText = QLabel(self.analysisLenBox)
        self.analysisLenText.setObjectName(u"analysisLenText")

        self.horizontalLayout_14.addWidget(self.analysisLenText)

        self.analysisLenChoices = QComboBox(self.analysisLenBox)
        self.analysisLenChoices.addItem("")
        self.analysisLenChoices.addItem("")
        self.analysisLenChoices.addItem("")
        self.analysisLenChoices.setObjectName(u"analysisLenChoices")
        self.analysisLenChoices.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_14.addWidget(self.analysisLenChoices)

        self.secondText_2 = QLabel(self.analysisLenBox)
        self.secondText_2.setObjectName(u"secondText_2")

        self.horizontalLayout_14.addWidget(self.secondText_2)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_12)


        self.verticalLayout_7.addWidget(self.analysisLenBox)


        self.verticalLayout_5.addWidget(self.sceneAnalysisBox)
        '''

        self.horizontalLayout_5.addWidget(self.functionsBox)


        self.verticalLayout_3.addWidget(self.contentMidBg)

        self.contentBottomBg = QFrame(self.contentBox)
        self.contentBottomBg.setObjectName(u"contentBottomBg")
        self.contentBottomBg.setMaximumSize(QSize(16777215, 200))
        self.horizontalLayout_7 = QHBoxLayout(self.contentBottomBg)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(9, 0, 0, 4)
        self.videoInfoBox = QFrame(self.contentBottomBg)
        self.videoInfoBox.setObjectName(u"videoInfoBox")
        self.videoInfoBox.setMaximumSize(QSize(250, 200))
        self.videoInfoBox.setFrameShape(QFrame.StyledPanel)
        self.videoInfoBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.videoInfoBox)
        self.verticalLayout_8.setSpacing(1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(4, 0, 0, 0)
        self.videoSourceBox = QFrame(self.videoInfoBox)
        self.videoSourceBox.setObjectName(u"videoSourceBox")
        self.videoSourceBox.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_13 = QHBoxLayout(self.videoSourceBox)
        self.horizontalLayout_13.setSpacing(7)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.videoSourceText = QLabel(self.videoSourceBox)
        self.videoSourceText.setObjectName(u"videoSourceText")

        self.horizontalLayout_13.addWidget(self.videoSourceText)

        self.videoSource = QLineEdit(self.videoSourceBox)
        self.videoSource.setObjectName(u"videoSource")
        self.videoSource.setReadOnly(True)

        self.horizontalLayout_13.addWidget(self.videoSource)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_13)


        self.verticalLayout_8.addWidget(self.videoSourceBox)

        self.fileSizeBox = QFrame(self.videoInfoBox)
        self.fileSizeBox.setObjectName(u"fileSizeBox")
        self.fileSizeBox.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_15 = QHBoxLayout(self.fileSizeBox)
        self.horizontalLayout_15.setSpacing(7)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.fileSizeText = QLabel(self.fileSizeBox)
        self.fileSizeText.setObjectName(u"fileSizeText")

        self.horizontalLayout_15.addWidget(self.fileSizeText)

        self.fileSize = QLineEdit(self.fileSizeBox)
        self.fileSize.setObjectName(u"fileSize")
        self.fileSize.setReadOnly(True)

        self.horizontalLayout_15.addWidget(self.fileSize)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_14)


        self.verticalLayout_8.addWidget(self.fileSizeBox)

        self.frameRateBox = QFrame(self.videoInfoBox)
        self.frameRateBox.setObjectName(u"frameRateBox")
        self.frameRateBox.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_16 = QHBoxLayout(self.frameRateBox)
        self.horizontalLayout_16.setSpacing(7)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frameRateText = QLabel(self.frameRateBox)
        self.frameRateText.setObjectName(u"frameRateText")

        self.horizontalLayout_16.addWidget(self.frameRateText)

        self.frameRate = QLineEdit(self.frameRateBox)
        self.frameRate.setObjectName(u"frameRate")
        sizePolicy3.setHeightForWidth(self.frameRate.sizePolicy().hasHeightForWidth())
        self.frameRate.setSizePolicy(sizePolicy3)
        self.frameRate.setReadOnly(True)

        self.horizontalLayout_16.addWidget(self.frameRate)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_15)


        self.verticalLayout_8.addWidget(self.frameRateBox)

        self.dpiBox = QFrame(self.videoInfoBox)
        self.dpiBox.setObjectName(u"dpiBox")
        self.horizontalLayout_17 = QHBoxLayout(self.dpiBox)
        self.horizontalLayout_17.setSpacing(7)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.dpiText = QLabel(self.dpiBox)
        self.dpiText.setObjectName(u"dpiText")

        self.horizontalLayout_17.addWidget(self.dpiText)

        self.widthText = QLabel(self.dpiBox)
        self.widthText.setObjectName(u"widthText")

        self.horizontalLayout_17.addWidget(self.widthText)


        self.frameWidth = QLineEdit(self.dpiBox)
        self.frameWidth.setObjectName(u"frameWidth")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frameWidth.sizePolicy().hasHeightForWidth())
        self.frameWidth.setSizePolicy(sizePolicy6)
        self.frameWidth.setMaximumSize(QSize(100, 16777215))
        self.frameWidth.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.frameWidth.setReadOnly(True)

        self.horizontalLayout_17.addWidget(self.frameWidth)

        self.heightText = QLabel(self.dpiBox)
        self.heightText.setObjectName(u"heightText")

        self.horizontalLayout_17.addWidget(self.heightText)

        self.frameHeight = QLineEdit(self.dpiBox)
        self.frameHeight.setObjectName(u"frameHeight")
        sizePolicy6.setHeightForWidth(self.frameHeight.sizePolicy().hasHeightForWidth())
        self.frameHeight.setSizePolicy(sizePolicy6)
        self.frameHeight.setMaximumSize(QSize(100, 16777215))
        self.frameHeight.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.frameHeight.setReadOnly(True)
        self.horizontalLayout_17.addWidget(self.frameHeight)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_16)


        self.verticalLayout_8.addWidget(self.dpiBox)


        self.horizontalLayout_7.addWidget(self.videoInfoBox)

        self.faceInfoBox = QFrame(self.contentBottomBg)
        self.faceInfoBox.setObjectName(u"faceInfoBox")
        self.faceInfoBox.setFrameShape(QFrame.StyledPanel)
        self.faceInfoBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.faceInfoBox)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.faceDetectionBox = QFrame(self.faceInfoBox)
        self.faceDetectionBox.setObjectName(u"faceDetectionBox")
        self.faceDetectionBox.setMaximumSize(QSize(200, 16777215))
        self.faceDetectionBox.setFrameShape(QFrame.StyledPanel)
        self.faceDetectionBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.faceDetectionBox)
        self.verticalLayout_9.setSpacing(1)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.detectedFaceText = QLabel(self.faceDetectionBox)
        self.detectedFaceText.setObjectName(u"detectedFaceText")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.detectedFaceText.sizePolicy().hasHeightForWidth())
        self.detectedFaceText.setSizePolicy(sizePolicy6)

        self.verticalLayout_9.addWidget(self.detectedFaceText)

        self.detectedFace = QLabel(self.faceDetectionBox)
        self.detectedFace.setObjectName(u"detectedFace")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.detectedFace.sizePolicy().hasHeightForWidth())
        self.detectedFace.setSizePolicy(sizePolicy7)

        self.verticalLayout_9.addWidget(self.detectedFace)

        self.horizontalLayout_19.addWidget(self.faceDetectionBox)

        self.faceCredibilityBox = QFrame(self.faceInfoBox)
        self.faceCredibilityBox.setObjectName(u"faceCredibilityBox")
        sizePolicy6.setHeightForWidth(self.faceCredibilityBox.sizePolicy().hasHeightForWidth())
        self.faceCredibilityBox.setSizePolicy(sizePolicy6)
        self.faceCredibilityBox.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_10 = QVBoxLayout(self.faceCredibilityBox)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.faceCredibilityBox = QFrame(self.faceInfoBox)
        self.faceCredibilityBox.setObjectName(u"faceCredibilityBox")
        sizePolicy6.setHeightForWidth(self.faceCredibilityBox.sizePolicy().hasHeightForWidth())
        self.faceCredibilityBox.setSizePolicy(sizePolicy6)
        self.faceCredibilityBox.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_10 = QVBoxLayout(self.faceCredibilityBox)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.detectResultBox = QHBoxLayout()
        self.detectResultBox.setObjectName(u"detectResultBox")
        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.detectResultBox.addItem(self.horizontalSpacer_22)

        self.detectResultText = QLabel(self.faceCredibilityBox)
        self.detectResultText.setObjectName(u"detectResultText")

        self.detectResultBox.addWidget(self.detectResultText)

        self.detectResult = QLineEdit(self.faceCredibilityBox)
        self.detectResult.setObjectName(u"detectResult")
        sizePolicy2.setHeightForWidth(self.detectResult.sizePolicy().hasHeightForWidth())
        self.detectResult.setSizePolicy(sizePolicy2)
        self.detectResult.setReadOnly(True)

        self.detectResultBox.addWidget(self.detectResult)

        self.verticalLayout_10.addLayout(self.detectResultBox)

        self.detectCredibilityBox = QHBoxLayout()
        self.detectCredibilityBox.setObjectName(u"detectCredibilityBox")
        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.detectCredibilityBox.addItem(self.horizontalSpacer_23)

        self.currentCredibilityText = QLabel(self.faceCredibilityBox)
        self.currentCredibilityText.setObjectName(u"currentCredibilityText")
        self.currentCredibilityText.setMaximumSize(QSize(16777215, 15))

        self.detectCredibilityBox.addWidget(self.currentCredibilityText)

        self.credibility = QLineEdit(self.faceCredibilityBox)
        self.credibility.setObjectName(u"credibility")
        sizePolicy2.setHeightForWidth(self.credibility.sizePolicy().hasHeightForWidth())
        self.credibility.setSizePolicy(sizePolicy2)
        self.credibility.setReadOnly(True)

        self.detectCredibilityBox.addWidget(self.credibility)

        self.verticalLayout_10.addLayout(self.detectCredibilityBox)

        self.recognizeResultBox = QHBoxLayout()
        self.recognizeResultBox.setObjectName(u"recognizeResultBox")
        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.recognizeResultBox.addItem(self.horizontalSpacer_26)

        self.recognizeResultText = QLabel(self.faceCredibilityBox)
        self.recognizeResultText.setObjectName(u"recognizeResultText")

        self.recognizeResultBox.addWidget(self.recognizeResultText)

        self.recognizeResult = QLineEdit(self.faceCredibilityBox)
        self.recognizeResult.setObjectName(u"recognizeResult")
        self.recognizeResult.setReadOnly(True)

        self.recognizeResultBox.addWidget(self.recognizeResult)

        self.verticalLayout_10.addLayout(self.recognizeResultBox)

        self.recognizeCredibilityBox = QHBoxLayout()
        self.recognizeCredibilityBox.setObjectName(u"recognizeCredibilityBox")
        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.recognizeCredibilityBox.addItem(self.horizontalSpacer_27)

        self.recognizeCredibilityText = QLabel(self.faceCredibilityBox)
        self.recognizeCredibilityText.setObjectName(u"recognizeCredibilityText")

        self.recognizeCredibilityBox.addWidget(self.recognizeCredibilityText)

        self.recognizeCredibility = QLineEdit(self.faceCredibilityBox)
        self.recognizeCredibility.setObjectName(u"recognizeCredibility")
        self.recognizeCredibility.setReadOnly(True)

        self.recognizeCredibilityBox.addWidget(self.recognizeCredibility)

        self.verticalLayout_10.addLayout(self.recognizeCredibilityBox)

        self.horizontalLayout_19.addWidget(self.faceCredibilityBox)

        self.horizontalLayout_7.addWidget(self.faceInfoBox)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_17)

        self.verticalLayout_3.addWidget(self.contentBottomBg)


        self.horizontalLayout_2.addWidget(self.contentBox)


        self.appLayout.addWidget(self.bgAPP)

        MainWindow.setCentralWidget(self.styleSheet)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.appLogo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/images/images/faceguard.png\"/></p></body></html>", None))
        self.topInfo.setText(QCoreApplication.translate("MainWindow", u"Face Guard", None))

#if QT_CONFIG(tooltip)
        self.minimizeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u6700\u5c0f\u5316", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u6b63\u5e38", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.progressText.setText(QCoreApplication.translate("MainWindow", u"00:00:00/00:00:00", None))
#if QT_CONFIG(tooltip)
        self.playVideoBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u64ad\u653e", None))
#endif // QT_CONFIG(tooltip)
        self.playVideoBtn.setText("")
#if QT_CONFIG(tooltip)
        self.openfileBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6587\u4ef6", None))
#endif // QT_CONFIG(tooltip)
        self.openfileBtn.setText("")
        self.volumeText.setText("")
        self.faceAnonBtn.setText(QCoreApplication.translate("MainWindow", u"Face Anonymize", None))
        self.faceAnonText.setText(QCoreApplication.translate("MainWindow", u"\u4eba\u8138\u533f\u540d\u5316", None))

        self.CurrentFaceModelText.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u4eba\u8138\u6a21\u578b", None))
        self.anonStausText.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u8f6c\u6362\u72b6\u6001", None))
        self.anonStaus.setText(QCoreApplication.translate("MainWindow", u"\u672a\u542f\u7528", None))
        self.startAnonBtn.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u8f6c\u6362", None))
        self.moreModelBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.faceDetectBtn.setText(QCoreApplication.translate("MainWindow", u"Face Detection", None))
        self.faceDetectText.setText(QCoreApplication.translate("MainWindow", u"\u4eba\u8138\u68c0\u6d4b", None))
        self.faceDetectCBox.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u542f\u7528", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u4eba\u8138\u7a81\u51fa", None))
        self.faceShowCBox.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u663e\u793a\u5728\u753b\u9762", None))
        self.detectLenText.setText(QCoreApplication.translate("MainWindow", u"\u6bcf\u6b21\u68c0\u6d4b\u957f\u5ea6", None))
        self.detectLenChoices.setItemText(0, QCoreApplication.translate("MainWindow", u"5", None))
        self.detectLenChoices.setItemText(1, QCoreApplication.translate("MainWindow", u"10", None))
        self.detectLenChoices.setItemText(2, QCoreApplication.translate("MainWindow", u"20", None))

        self.secondText.setText(QCoreApplication.translate("MainWindow", u"\u79d2", None))
        '''
        self.sceneAnalysisBtn.setText(QCoreApplication.translate("MainWindow", u"Scene Analysis", None))
        self.sceneAnalysisText.setText(QCoreApplication.translate("MainWindow", u"\u573a\u666f\u5206\u6790", None))
        self.sceneAnalysisCbox.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u542f\u7528", None))
        self.analysisLenText.setText(QCoreApplication.translate("MainWindow", u"\u6bcf\u6b21\u5206\u6790\u957f\u5ea6", None))
        self.analysisLenChoices.setItemText(0, QCoreApplication.translate("MainWindow", u"5", None))
        self.analysisLenChoices.setItemText(1, QCoreApplication.translate("MainWindow", u"10", None))
        self.analysisLenChoices.setItemText(2, QCoreApplication.translate("MainWindow", u"20", None))
        self.secondText_2.setText(QCoreApplication.translate("MainWindow", u"\u79d2", None))
        '''
        self.videoSourceText.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u89c6\u9891\u6d41", None))
        self.fileSizeText.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u5927\u5c0f", None))
        self.frameRateText.setText(QCoreApplication.translate("MainWindow", u"\u5e27\u7387", None))
        self.dpiText.setText(QCoreApplication.translate("MainWindow", u"\u5206\u8fa8\u7387", None))
        self.widthText.setText(QCoreApplication.translate("MainWindow", u"\u5bbd", None))
        self.frameWidth.setText("")

        self.heightText.setText(QCoreApplication.translate("MainWindow", u"\u9ad8", None))
        self.detectedFaceText.setText(
                QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u68c0\u6d4b\u5230\u7684\u4eba\u8138\uff1a",
                                           None))
        self.detectedFace.setText("")
        self.detectResultText.setText(
                QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u68c0\u6d4b\u7ed3\u679c\uff1a", None))
        self.currentCredibilityText.setText(
                QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u4eba\u8138\u53ef\u4fe1\u5ea6\uff1a", None))
        self.detectResultText.setText(
                QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u68c0\u6d4b\u7ed3\u679c\uff1a", None))
        self.currentCredibilityText.setText(
                QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u4eba\u8138\u53ef\u4fe1\u5ea6\uff1a", None))
        self.recognizeResultText.setText(QCoreApplication.translate("MainWindow",
                                                                    u"\u5f53\u524d\u4eba\u7269\u8eab\u4efd\u8bc6\u522b\u7ed3\u679c",
                                                                    None))
        self.recognizeCredibilityText.setText(
                QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u8bc6\u522b\u53ef\u4fe1\u5ea6", None))
    # retranslateUi

    # retranslateUi

