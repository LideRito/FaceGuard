import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QSlider, QLabel, QWidget
from PySide6.QtGui import *
from PySide6.QtCore import Slot, QTime, QDateTime, Qt, QPoint, QSize, QRect
from PySide6 import QtCore
from PySide6.QtCore import Signal, QUrl, QCoreApplication
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput, QVideoFrame
import cv2

def QImage2cv(qimage: QImage):
    #处理为cv2可以接受的BGR格式
    qimage = qimage.convertToFormat(QImage.Format.Format_BGR888)

    width = qimage.width()
    height = qimage.height()

    ptr = qimage.constBits()
    arr = np.array(ptr).reshape(height, width, 3) 
    return arr

def  cv2QImage(cv_image: np.ndarray):
    width = cv_image.shape[1]
    height = cv_image.shape[0]

    pixmap = QPixmap(width,height)
    qimage = pixmap.toImage()

    for row in range(0,height):
        for col in range(0, width):
            b = cv_image[row,col,0]
            g = cv_image[row,col,1]
            r = cv_image[row,col,2]

            pix = qRgb(r, g, b)
            qimage.setPixel(col, row, pix)

    return qimage
