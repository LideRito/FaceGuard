import re
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QSlider, QLabel, QWidget
from PySide6.QtGui import QIcon, QImage, QPixmap, QCursor, QPainter
from PySide6.QtCore import Slot, QTime, QDateTime, Qt, QPoint, QSize, QRect, QThread
from PySide6 import QtCore
from PySide6.QtCore import Signal, QUrl, QCoreApplication, QObject
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput, QVideoFrame
from module import image_util as i_util
from module import deepfake_detector as dd
import pyvirtualcam as pycam
import numpy as np
from module import face_recognition as FR
from module.DeepFaceLab import VideoProcessing

#人脸真伪检测用线程
class Detect_Thread(QObject):
    start_signal = Signal(list,float)
    finish_signal = Signal(str,float)

    def __init__(self):
        super().__init__()
    
    def detect_proc(self,frames,fps):
        print('detect_process_entered')
        tmp_frames = []
        len = 0
        for img in frames:
            tmp = i_util.QImage2cv(img)
            tmp_frames.append(tmp)
            len += 1
        landmarks = dd.get_landmarks(tmp_frames, fps)
        label, pd = dd.categorize(landmarks)
        self.finish_signal.emit(label,pd)

#人脸身份识别用线程
class Face_Recog_Thread(QObject):
    start_signal = Signal(np.ndarray)
    finish_signal = Signal(str,float,np.ndarray,float,float,float,float)

    def __init__(self):
        super().__init__()

    def face_recog(self, img):
        print('face_recog')
        print(img)
        try:
            img = i_util.QImage2cv(img)
            res,conf,tar_region, x, w, y, h = FR.get_result(img)
            if tar_region != []:
                tar_region = i_util.cv2QImage(tar_region)
            self.finish_signal.emit(res,conf,tar_region,x,w,y,h)
        except Exception as e:
            self.finish_signal.emit('error',-1,[],0,0,0,0)
        

#人脸匿名化用线程
class Anonymize_Thread(QObject):
    start_signal = Signal()
    finish_signal = Signal()

    def __init__(self):
        super().__init__()

    def anonymize_proc(self):
        vid_pro = VideoProcessing.VideoProcessing()

        try:
            vid_pro.Cut()                      #将视频切割成帧
            vid_pro.ExtractFace()              #人脸预处理
            vid_pro.MergeSADE()                #换脸
            # vid_pro.MergeVedio()               #帧合成视频，当前版本无法合成视频
            
            pass
        except Exception as e:
            print(e)

        self.finish_signal.emit()

