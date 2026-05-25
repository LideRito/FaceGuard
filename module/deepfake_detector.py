import numpy as np
import tensorflow.keras as K
import os
from tensorflow.keras import layers
from module.landmark_utils import detect_frames_track
import cv2

def deepfake_detect(input_path):
    landmarks = get_landmarks(input_path)
    categorize(landmarks)
    pass

def get_landmarks(frames,fps):
    raw_data = detect_frames_track(frames, fps, True, 'test')
    return np.array(raw_data)

block_size = 60
DROPOUT_RATE = 0.5
RNN_UNIT = 64
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

def data_process(landmarks):
    x = []
    x_diff = []

    video_y = []
    count_y = {}
    sample_to_video = []

    file = 'default'
    block = block_size
    fake = 1.0

    vectors = landmarks
    video_y.append(fake)

    for i in range(0, vectors.shape[0] - block, block):
        vec = vectors[i:i + block, :]
        x.append(vec)
        vec_next = vectors[i + 1:i + block, :]
        vec_next = np.pad(vec_next, ((0, 1), (0, 0)), 'constant', constant_values=(0, 0))
        vec_diff = (vec_next - vec)[:block - 1, :]
        x_diff.append(vec_diff)

        if file not in count_y:
            count_y[file] = 1
        else:
            count_y[file] += 1

        # Recording each samples belonging
        sample_to_video.append(file)

    return np.array(x), np.array(x_diff), np.array(sample_to_video), count_y

def categorize(landmarks):
    """
    categorize faces according to the landmarks get from get_landmarks()
    :param
    landmarks: landmarks from get_landmarks()  
    :return:

    """

    test_samples, test_samples_diff, test_sv, test_vc = data_process(landmarks)

    model = K.Sequential([
        layers.InputLayer(input_shape=(block_size, 136)),
        layers.Dropout(0.25),
        layers.Bidirectional(layers.GRU(RNN_UNIT)),
        layers.Dropout(DROPOUT_RATE),
        layers.Dense(64, activation='relu'),
        layers.Dropout(DROPOUT_RATE),
        layers.Dense(2, activation='softmax')
    ])
    model_diff = K.Sequential([
        layers.InputLayer(input_shape=(block_size - 1, 136)),
        layers.Dropout(0.25),
        layers.Bidirectional(layers.GRU(RNN_UNIT)),
        layers.Dropout(DROPOUT_RATE),
        layers.Dense(64, activation='relu'),
        layers.Dropout(DROPOUT_RATE),
        layers.Dense(2, activation='softmax')
    ])

    lossFunction = K.losses.SparseCategoricalCrossentropy(from_logits=False)
    optimizer = K.optimizers.Adam(learning_rate=0.001)
    model.compile(optimizer=optimizer,
                  loss=lossFunction,
                  metrics=['accuracy'])
    model_diff.compile(optimizer=optimizer,
                  loss=lossFunction,
                  metrics=['accuracy'])

    #----Using Deeperforensics 1.0 Parameters----#
    model.load_weights('model/pre_model/deeper/g1.h5')
    model_diff.load_weights('model/pre_model/deeper/g2.h5')

    #----Using FF++ Parameters----#
    # model.load_weights('./pre_model/ff/g1.h5')
    # model_diff.load_weights('./pre_model/ff/g2.h5')

    prediction = model.predict(test_samples)
    prediction_diff = model_diff.predict(test_samples_diff)
    mix_predict = []
    for i in range(len(prediction)):
        mix = prediction[i][1] + prediction_diff[i][1]
        mix_predict.append(mix/2)

    prediction_video = []
    pre_count = {}
    for p, v_label in zip(mix_predict, test_sv):
        p_bi = 0
        if p >= 0.5:
            p_bi = 1
        if v_label in pre_count:
            pre_count[v_label] += p_bi
        else:
            pre_count[v_label] = p_bi
    for key in pre_count.keys():
        prediction_video.append(pre_count[key] / test_vc[key])

    print("\n\n", "#----Prediction Results----#")
    video_names = []
    for key in test_vc.keys():
        video_names.append(key)
    for i, pd in enumerate(prediction_video):
        if pd >= 0.5:
            label = "Fake"
        else:
            label = "Real"
        # print("{}-Prediction label: {}; Scores:{}".format(video_names[i], label, pd))
        ret_label = label
        ret_pd = pd
    return ret_label, ret_pd