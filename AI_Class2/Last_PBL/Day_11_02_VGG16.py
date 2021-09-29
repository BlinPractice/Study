# Day_11_02_VGG16.py

import tensorflow as tf
from tensorflow.keras.layers import Conv2D, MaxPool2D, InputLayer, Dense, Flatten


# Quiz : 224 크기의 이미지셋을 대상으로 VGG16 모델을 구축하세요.
model = tf.keras.Sequential([
    InputLayer(input_shape=[224, 244, 3]),

    Conv2D(64, 3, 1, 'same', activation='relu'),
    Conv2D(64, 3, 1, 'same', activation='relu'),
    MaxPool2D(name='block1'),

    Conv2D(128, 3, 1, 'same', activation='relu'),
    Conv2D(128, 3, 1, 'same', activation='relu'),
    MaxPool2D(name='block2'),

    Conv2D(256, 3, 1, 'same', activation='relu'),
    Conv2D(256, 3, 1, 'same', activation='relu'),
    Conv2D(256, 3, 1, 'same', activation='relu'),
    MaxPool2D(name='block3'),

    Conv2D(512, 3, 1, 'same', activation='relu'),
    Conv2D(512, 3, 1, 'same', activation='relu'),
    Conv2D(512, 3, 1, 'same', activation='relu'),
    MaxPool2D(name='block4'),

    Conv2D(512, 3, 1, 'same', activation='relu'),
    Conv2D(512, 3, 1, 'same', activation='relu'),
    Conv2D(512, 3, 1, 'same', activation='relu'),
    MaxPool2D(name='block5'),

    Flatten(),

    Dense(4096, activation='relu'),
    Dense(4096, activation='relu'),
    Dense(1000, activation='softmax')
])

model.summary()


tf.keras.applications.VGG16
