import VideoProcessing
#import os


if __name__ == "__main__":

    VideoPro = VideoProcessing.VideoProcessing()
    VideoPro.Cut()                      #将视频切割成帧
    VideoPro.ExtractFace()              #人脸预处理
    VideoPro.MergeSADE()                #换脸
    VideoPro.MergeVedio()               #帧合成视频