import re
import sys
import PySide6
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QSlider, QLabel, QWidget
from PySide6.QtGui import QIcon, QImage, QPixmap, QCursor, QPainter
from PySide6.QtCore import Slot, QTime, QDateTime, Qt, QPoint, QSize, QRect
from PySide6 import QtCore
from PySide6.QtCore import Signal, QUrl, QCoreApplication, QThread
from design.Ui_Main import Ui_MainWindow
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput, QVideoFrame
from module.video_prober import VideoProber
from module import image_util as i_util
from module import deepfake_detector as dd
from module.my_thread import *


class MyWid(QWidget):

    def __init__(self, parent=None):
        super(MyWid, self).__init__(parent)

        self.resize(parent.size())
        self.label = QLabel(self)
        self.need_paint = False
        self.area = None

    def draw(self, x=0, y=0, w=100, h=300):
        self.area = QRect(x, y, w, h)
        self.need_paint = True
        self.update()

    def paintEvent(self, event):
        if self.need_paint:
            painter = QPainter(self)
            painter.setPen(Qt.yellow)
            painter.drawRect(self.area)

        self.need_paint = False

    def move_with(self, pos: QPoint):
        self.move(pos)

    def resize_with(self, size: QSize):
        self.resize(size)


class MainWin(QMainWindow, Ui_MainWindow):
    sigIsPlayTrue = Signal()

    def __init__(self, parent=None):

        super(MainWin, self).__init__(parent)
        self.m_flag = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowTitle('Face Guard')
        # 播放器准备
        self.player = QMediaPlayer()
        self.audioOutput = QAudioOutput()  # 不能实例化为临时变量，否则被自动回收导致无法播放
        self.player.setAudioOutput(self.audioOutput)
        self.player.setVideoOutput(self.ui.videoWid)
        self.videoSink = self.ui.videoWid.videoSink()
        self.videoSink.videoFrameChanged.connect(self.processFrame)
        self.scaleRatio = 1
        self.fp = None

        # 文件信息探测器准备
        self.video_prober = VideoProber()
        # 用来绘制框
        self.glass = MyWid(self)
        self.glass.setWindowFlags(Qt.SubWindow | Qt.FramelessWindowHint | Qt.Tool)

        self.glass.setAttribute(Qt.WA_TranslucentBackground)

        self.glass.show()

        self.ui.volumeBar.setValue(50)
        self.ui.volumeBar.setTickInterval(10)
        self.ui.volumeBar.setTickPosition(QSlider.TicksBelow)  # 刻度位置
        self.connect_slot()
        self.showMaximized()

        # frames处理相关，人脸识别相关
        self.deepfake_detect_flag = False
        self.temp_frames = []
        self.frames_num = 0
        self.detect_len = 5
        self.is_show = False

        # 进程相关
        self.face_recog_valid = False
        self.is_anon = False
        self.thread_temp_1 = None
        self.thread_temp_2 = None
        self.thread_temp_3 = None

    def connect_slot(self):
        self.ui.closeAppBtn.clicked.connect(self.closeApp)
        self.ui.minimizeBtn.clicked.connect(self.showMinimized)
        self.ui.maximizeBtn.clicked.connect(self.maximizeOrRestoreApp)

        self.ui.playVideoBtn.clicked.connect(self.play_or_pause)
        self.player.positionChanged.connect(self.get_time)
        self.ui.openfileBtn.clicked.connect(self.open_file)
        self.ui.volumeBar.valueChanged.connect(self.change_volume)
        self.ui.progressSlider.sliderMoved.connect(self.change_time)
        self.player.playbackStateChanged.connect(self.clear)

        self.ui.startAnonBtn.clicked.connect(self.face_anon)
        self.ui.faceDetectCBox.stateChanged.connect(self.face_detect)
        # self.ui.sceneAnalysisCbox.stateChanged.connect(self.scene_analysis)
        self.ui.faceShowCBox.stateChanged.connect(self.face_show)

        self.ui.faceModelChoices.currentIndexChanged.connect(self.face_model_choose)
        self.ui.detectLenChoices.currentIndexChanged.connect(self.detect_len_choose)
        # self.ui.analysisLenChoices.currentIndexChanged.connect(self.analysis_len_choose)
        self.ui.moreModelBtn.clicked.connect(self.open_model)

    def clear(self, state):

        if state is QMediaPlayer.StoppedState:
            self.glass.repaint()

    # 关闭
    def closeApp(self):
        app = QApplication.instance()
        app.quit()

    # 最大化或正常化窗口
    def maximizeOrRestoreApp(self):
        if not self.isMaximized():
            self.showMaximized()
            icon = QIcon()
            icon.addFile(u"design/images/icons/icon_restore.png", QtCore.QSize(), QIcon.Normal, QIcon.Off)
            self.ui.maximizeBtn.setIcon(icon)
            self.ui.maximizeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"正常", None))
        else:
            self.showNormal()
            icon = QIcon()
            icon.addFile(u"design/images/icons/icon_maximize.png", QtCore.QSize(), QIcon.Normal, QIcon.Off)
            self.ui.maximizeBtn.setIcon(icon)
            self.ui.maximizeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"最大化", None))

    # 视频暂停
    def pause(self):
        self.player.pause()
        icon = QIcon()
        icon.addFile(u"design/images/icons/cil-media-play.png", QtCore.QSize(), QIcon.Normal, QIcon.Off)
        self.ui.playVideoBtn.setIcon(icon)
        self.ui.playVideoBtn.setToolTip(QCoreApplication.translate("MainWindow", u"播放", None))

    # 视频播放
    def play(self):
        if self.fp is not None:

            self.player.play()
            icon = QIcon()
            icon.addFile(u"design/images/icons/cil-media-pause.png", QtCore.QSize(), QIcon.Normal, QIcon.Off)
            self.ui.playVideoBtn.setIcon(icon)
            self.ui.playVideoBtn.setToolTip(QCoreApplication.translate("MainWindow", u"暂停", None))
            self.scaleRatio = self.ui.videoWid.height() / int(self.ui.frameHeight.text())
            print(self.scaleRatio)
            self.wid_x = self.ui.videoWid.width()
            self.deta_x = (self.wid_x - int(self.ui.frameWidth.text())*self.scaleRatio)/2
            self.deta_y = self.ui.contentTopBg.height()/2
            print(self.deta_x,self.deta_y)
        else:

            QMessageBox.information(self, "warning", "当前没有文件")

    # 点击播放按钮后判断当前视频状态决定播放还是暂停
    def play_or_pause(self):

        state = self.player.playbackState()

        if state is QMediaPlayer.PlayingState:
            print('pause')
            self.pause()
        elif state is QMediaPlayer.PausedState:
            print('play')
            self.play()
        elif state is QMediaPlayer.StoppedState:
            QMessageBox.information(self, "warning", "当前无视频播放或已播放完")

    # 获得当前视频时间
    def get_time(self, num):
        self.ui.progressSlider.setMaximum(self.player.duration())
        self.ui.progressSlider.setValue(num)
        d = QDateTime.fromMSecsSinceEpoch(num).toString("mm:ss")
        all = self.player.duration()
        all_d = QDateTime.fromMSecsSinceEpoch(all).toString("mm:ss")
        if d == all_d:
            icon = QIcon()
            icon.addFile(u"design/images/icons/cil-media-play.png", QtCore.QSize(), QIcon.Normal, QIcon.Off)
            self.ui.playVideoBtn.setIcon(icon)
            self.ui.playVideoBtn.setToolTip(QCoreApplication.translate("MainWindow", u"播放", None))
        self.ui.progressText.setText(d + '/ ' + all_d)

    # 打开视频文件
    def open_file(self):
        url = QFileDialog.getOpenFileUrl(None,
                                         '选择文件', "./",
                                         '音频文件(*.mp4 *.avi)')
        self.fp = url[0]

        self.video_prober.probe(self.fp.toString())
        self.change_video_info()
        self.player.setSource(self.fp)
        self.play()
        # 清空并重新初始化
        self.ui.detectedFace.clear()
        self.ui.recognizeCredibility.clear()
        self.ui.recognizeResult.clear()
        self.ui.credibility.clear()
        self.ui.detectResult.clear()
        self.temp_frames = []
        self.frames_num = 0
    # 改变视频信息栏中信息
    def change_video_info(self):
        video_info = self.video_prober.get_video_info()

        self.ui.videoSource.setText(video_info['path'])
        self.ui.fileSize.setText(video_info['file_size'])
        self.ui.frameRate.setText(video_info['frame_rate'])
        self.ui.frameHeight.setText(str(video_info['height_width'][0]))
        self.ui.frameWidth.setText(str(video_info['height_width'][1]))

    # 改变视频音量
    def change_volume(self, num):
        self.audioOutput.setVolume(float(num / 100))

        if num == 0:
            self.ui.volumeText.setPixmap(QPixmap(u"design/images/icons/cil-volume-off.png"))
        elif num < 50:

            self.ui.volumeText.setPixmap(QPixmap(u"design/images/icons/cil-volume-low.png"))
        else:

            self.ui.volumeText.setPixmap(QPixmap(u"design/images/icons/cil-volume-high.png"))

    # 改变视频播放位置
    def change_time(self, num):

        self.player.setPosition(num)

    # 处理帧
    def processFrame(self, frame):
        # print('framechange')
        frame.map(QVideoFrame.ReadOnly)

        # 这里用来写对frame进行操作

        if self.ui.faceDetectCBox.isChecked():
            tmp = frame.toImage()

            
            if self.deepfake_detect_flag:
                self.frames_num += 1
                self.temp_frames.append(tmp)

            # print(self.frames_num)

            fps = float(self.ui.frameRate.text())

            # print(self.detect_len * fps)

            # 判断是否已收集帧数超过平均帧率乘以长度
            if self.deepfake_detect_flag and self.frames_num >= self.detect_len * fps:
                self.deepfake_detect_flag = False
                self.add_detect_thread(self.temp_frames, fps)

            if self.face_recog_valid:
                self.face_recog_valid = False
                self.face_recog(tmp)

        # 这里用来绘制框体
        # self.glass.draw()

        frame.unmap()

    #   人脸匿名化启用或停止
    def face_anon(self):
        if not self.is_anon:
            print('start face anonymize')
            self.start_anonymize_thread()
            self.is_anon = True
            self.ui.anonStaus.setText("正在转化")
            # 开始人脸匿名化
        else:
            print('end face anonymize')
        # 结束人脸匿名化

    # 打开文件夹选择额外模型
    def open_model(self):
        url = QFileDialog.getOpenFileUrl(None,
                                         '选择文件', "./"
                                         )
        fp = url[0].toString()
        res = re.match(r'file:///', fp)
        if res.group():
            res = re.split(r'file:///', fp)[1]
        fp = res

        self.ui.faceModelChoices.addItem(fp)

    # 人脸模型选择
    def face_model_choose(self):

        print(self.ui.faceModelChoices.currentText())
        # 改变匿名化模型

    # 人脸检测启用或停止
    def face_detect(self):
        if self.ui.faceDetectCBox.isChecked():
            print('start face detect')

            # 初始化frames相关
            self.temp_frames = []
            self.frames_num = 0

            self.face_recog_valid = True
            self.deepfake_detect_flag = True

        # 开始人脸检测

        else:
            print('end face detect')
            self.temp_frames = []
            self.frames_num = 0

            self.face_recog_valid = False
        # 结束人脸检测

    # 人脸画框显示
    def face_show(self):
        if self.ui.faceDetectCBox.isChecked():
            if self.ui.faceShowCBox.isChecked():
                self.is_show = True

            else:
                self.is_show = False


    # 人脸检测长度选择
    def detect_len_choose(self):

        self.detect_len = self.ui.detectLenChoices.currentText()
        self.detect_len = float(self.detect_len)
        # 改变人脸检测

    '''
    # 场景分析启用或停止
    def scene_analysis(self):
        if self.ui.sceneAnalysisCbox.isChecked():
            print('start scene analysis')
        # 开始场景分析

        else:
            print('end scene analysis')
        # 结束场景分析

    # 场景分析长度选择
    def analysis_len_choose(self):

        len = self.ui.analysisLenChoices.currentText()
        # 改变场景分析

    '''
    # 下面为窗口鼠标的操作
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def moveEvent(self, event) -> None:

        self.glass.move_with(event.pos())

    def resizeEvent(self, event) -> None:

        self.glass.resize_with(self.size())

    def closeEvent(self, event: PySide6.QtGui.QCloseEvent) -> None:

        if self.thread_temp_1 :
            if self.thread_temp_1.isRunning():
                print('still')
                self.thread_temp_1.terminate()
                print('done')
        if self.thread_temp_2 :
            if self.thread_temp_2.isRunning():
                print('still')
                self.thread_temp_2.terminate()
                print('done')
        if self.thread_temp_3 :
            if self.thread_temp_3.isRunning():
                print('still')
                self.thread_temp_3.terminate()
                print('done')
    
    def add_detect_thread(self, frames, fps):
        print('detect_thread_start')
        self.thread_temp_1 = QThread(self)
        self.detect_thread = Detect_Thread()
        self.detect_thread.moveToThread(self.thread_temp_1)
        self.detect_thread.start_signal.connect(self.detect_thread.detect_proc)
        self.detect_thread.finish_signal.connect(self.update_detect_result)

        self.thread_temp_1.start()
        self.detect_thread.start_signal.emit(frames, fps)

        pass

    # def finish_detect(self, label, pd):
    #     print(label, pd)
    #     self.test_flag = True

    def start_anonymize_thread(self):
        self.thread_temp_2 = QThread(self)
        self.anonymize_thread = Anonymize_Thread()
        self.anonymize_thread.moveToThread(self.thread_temp_2)
        self.anonymize_thread.start_signal.connect(self.anonymize_thread.anonymize_proc)
        self.anonymize_thread.finish_signal.connect(self.anonymize_finished)

        self.thread_temp_2.start()
        self.anonymize_thread.start_signal.emit()

    def face_recog(self, img):
        print('face_recog_start')
        self.thread_temp_3 = QThread(self)
        self.face_recog_thread = Face_Recog_Thread()
        self.face_recog_thread.moveToThread(self.thread_temp_3)
        self.face_recog_thread.start_signal.connect(self.face_recog_thread.face_recog)
        self.face_recog_thread.finish_signal.connect(self.update_recog_result)

        self.thread_temp_3.start()
        self.face_recog_thread.start_signal.emit(img)
        pass

    def update_detect_result(self, label, pd):
        print('face_forgery_detect:result:{},conf:{}'.format(label, pd))
        self.deepfake_detect_flag = True
        self.ui.detectResult.setText(label)
        self.ui.credibility.setText(str(1 - pd))
        self.temp_frames = []
        self.frames_num = 0

    def update_recog_result(self, res, conf, tar_region, x, w, y, h,):
        print('face_recog:result:{},conf:{}'.format(res, conf))
        if conf > 50:

            self.ui.recognizeResult.setText(res)
            self.ui.recognizeCredibility.setText(str(conf))

        if tar_region != []:

            tar_region = QPixmap(tar_region)

            self.ui.detectedFace.setPixmap(tar_region)
            if self.is_show:
                val_x = x - self.deta_x/3 if x + self.deta_x > self.wid_x/2 else x + self.deta_x

                self.glass.draw(val_x, y+self.deta_y,w*self.scaleRatio,h*self.scaleRatio)
        
        self.face_recog_valid = True

        pass

    def anonymize_finished(self):
        self.ui.anonStaus.setText("匿名化结束")
        self.is_anon = False
        pass


if __name__ == "__main__":
    # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    # 初始化
    myWin = MainWin()

    # 将窗口控件显示在屏幕上
    myWin.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec())
