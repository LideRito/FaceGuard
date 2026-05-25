import tensorflow as tf
tf.get_logger().setLevel('ERROR')

#忽略
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from module.face_rec_util import face_recognition
import cv2

#读取图片

face_recog = face_recognition()

def get_result(tar_img):
  known_imgs = 'images/known/'  ##已知图片路径
  max_conf = -1
  image_files = os.listdir(known_imgs)
  res = "default"
  for image_file in image_files:
    check_image = cv2.imread(known_imgs + "/" + image_file)
    temp_conf = float(get_single_result(tar_img, check_image))
    if temp_conf > max_conf :
      max_conf = temp_conf
      res = image_file

  tmp_region = []

  tmp_x = 0
  tmp_w = 0
  tmp_y = 0
  tmp_h = 0

  gray = cv2.cvtColor(tar_img, cv2.COLOR_BGR2GRAY)  # 转换为灰度
  face_detector = cv2.CascadeClassifier('model/recognition_model/haarcascade_frontalface_alt2.xml')  # 加载人脸分类器
  face = face_detector.detectMultiScale(gray, 1.20, 5, cv2.CASCADE_SCALE_IMAGE, )  # 分类器函数  某些参数会影响辨别？
  # face=face_detector.detectMultiScale(gray)
  for x, y, w, h in face:
    #输出人脸左上角和右下角坐标
    tmp_x = x
    tmp_w = w
    tmp_y = y
    tmp_h = h

    tmp_region = tar_img[tmp_y:tmp_y + tmp_h, tmp_x:tmp_x + tmp_w]

  return res, max_conf, tmp_region, tmp_x, tmp_w, tmp_y, tmp_h

def get_single_result(img_1, img_2):

  ret = -1

  try:
      v1 = face_recog.get_single_feature_vector(img_1)
      v2 = face_recog.get_single_feature_vector(img_2)
      res = face_recog.cos_sim(v1, v2).tolist()[0][0]
      res = format(res * 100, '.2f')
      # name.configure(text=str(res[0][0]))
      if (float(res) >= 0) :
        ret = res
      else :
        ret = -float(res)
  except Exception as e:
    print(e)

  # # 计算两张图片的余弦相似度
  # v1 = face_recog.get_single_feature_vector(img_1)
  # v2 = face_recog.get_single_feature_vector(img_2)
  # res = face_recog.cos_sim(v1, v2).tolist()[0][0]
  # res = format(res * 100, '.2f')
  # # name.configure(text=str(res[0][0]))
  # if (float(res) >= 0) :
  #   ret = res
  # else :
  #   ret = -float(res)

  return ret


if __name__ == '__main__':
  get_result()
