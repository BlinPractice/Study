# Day_13_01_KerasFunctional.py

# 파이썬 라이브러리 7개
# Python        : requests, re, BeautifulSoup, sqlite3, csv, os, ...
# Data Analysis : numpy, matplotlib, seaborn, mpld3, pandas, scipy, sympy
# ML            : scikit-learn
# DL            : tensorflow, keras, pytorch

import tensorflow as tf
import numpy as np


# Quiz : 아래 데이터로부터 X, y를 추출한 다음, 딥러닝 모델을 구축하세요.
def model_and():
    data = [[0, 0, 0],
            [0, 1, 0],
            [1, 0, 0],
            [1, 1, 1]]
    data = np.int32(data)

    # data set extract
    X = data[:, :-1]
    y = data[:, -1]

    # modeling
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
    model.compile(optimizer=tf.keras.optimizers.SGD(0.1),
                  loss=tf.keras.losses.binary_crossentropy,
                  metrics='acc')

    # train and predict
    model.fit(X, y, epochs=1000, verbose=2)
    pred = model.predict(X, verbose=0)
    print(pred)


# Quiz : 기존 데이터를 xor 데이터로 변환해서 모델을 구축하세요.
def model_xor():
    data = [[0, 0, 0],
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 0]]
    data = np.int32(data)

    # data set extract
    X = data[:, :-1]
    y = data[:, -1:]

    # modeling
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.InputLayer(input_shape=X.shape[1:]))
    model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
    model.compile(optimizer=tf.keras.optimizers.SGD(0.1),
                  loss=tf.keras.losses.binary_crossentropy,
                  metrics='acc')

    # train and predict
    model.fit(X, y, epochs=1000, verbose=2)
    pred = model.predict(X, verbose=0)
    print(pred)


def model_functional_1():
    data = [[0, 0, 0],
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 0]]
    data = np.int32(data)

    X = data[:, :-1]
    y = data[:, -1:]

    # 1번
    # inputs = tf.keras.layers.Input(shape=X.shape[1:])
    # dense1 = tf.keras.layers.Dense(2, activation='sigmoid')
    # dense2 = tf.keras.layers.Dense(1, activation='sigmoid')
    #
    # output1 = dense1.__call__(inputs)
    # output2 = dense2.__call__(output1)

    # 2번
    # inputs = tf.keras.layers.Input(shape=X.shape[1:])
    # dense1 = tf.keras.layers.Dense(2, activation='sigmoid')
    # dense2 = tf.keras.layers.Dense(1, activation='sigmoid')
    #
    # output1 = dense1(inputs)
    # output2 = dense2(output1)

    # 3번
    inputs = tf.keras.layers.Input(shape=X.shape[1:])
    output1 = tf.keras.layers.Dense(2, activation='sigmoid')(inputs)
    output2 = tf.keras.layers.Dense(1, activation='sigmoid')(output1)

    model = tf.keras.Model(inputs, output2)
    model.compile(optimizer=tf.keras.optimizers.Adam(0.01),
                  loss=tf.keras.losses.binary_crossentropy,
                  metrics='acc')

    model.fit(X, y, epochs=1000, verbose=2)
    pred = model.predict(X, verbose=0)
    print(pred)


def model_functional_2():
    data = [[0, 0, 0],
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 0]]
    data = np.int32(data)

    X1 = data[:, 0:1]
    X2 = data[:, 1:2]
    y  = data[:, 2:3]

    # 1번
    # inputs1 = tf.keras.layers.Input(shape=X1.shape[1:])
    # inputs2 = tf.keras.layers.Input(shape=X2.shape[1:])
    #
    # output0 = tf.keras.layers.concatenate([inputs1, inputs2], axis=1)
    # output1 = tf.keras.layers.Dense(2, activation='sigmoid')(output0)
    # output2 = tf.keras.layers.Dense(1, activation='sigmoid')(output1)

    # 2번
    inputs1 = tf.keras.layers.Input(shape=X1.shape[1:])
    left = tf.keras.layers.Dense(2, activation='sigmoid')(inputs1)

    inputs2 = tf.keras.layers.Input(shape=X2.shape[1:])
    right = tf.keras.layers.Dense(1, activation='sigmoid')(inputs2)

    output0 = tf.keras.layers.concatenate([left, right], axis=1)
    output1 = tf.keras.layers.Dense(2, activation='sigmoid')(output0)
    output2 = tf.keras.layers.Dense(1, activation='sigmoid')(output1)

    model = tf.keras.Model([inputs1, inputs2], output2)
    model.compile(optimizer=tf.keras.optimizers.Adam(0.01),
                  loss=tf.keras.losses.binary_crossentropy,
                  metrics='acc')
    model.fit([X1, X2], y, epochs=1000, verbose=2)
    pred = model.predict([X1, X2], verbose=0)
    print(pred)


# Quiz : 입력과 출력이 각각 2개인 함수형 모델을 만드세요.
def model_functional_3():
    data = [[0, 0, 0, 0],
            [0, 1, 1, 0],
            [1, 0, 1, 0],
            [1, 1, 0, 1]]
    data = np.int32(data)

    X1 = data[:, 0:1]
    X2 = data[:, 1:2]
    y1 = data[:, 2:3]
    y2 = data[:, 3:4]

    inputs1 = tf.keras.layers.Input(shape=X1.shape[1:])
    output_left = tf.keras.layers.Dense(2, activation='sigmoid')(inputs1)

    inputs2 = tf.keras.layers.Input(shape=X2.shape[1:])
    output_right = tf.keras.layers.Dense(1, activation='sigmoid')(inputs2)

    output0 = tf.keras.layers.concatenate([output_left, output_right], axis=1)

    output_left = tf.keras.layers.Dense(2, activation='sigmoid')(output0)
    output_left = tf.keras.layers.Dense(1, activation='sigmoid')(output_left)

    output_right = tf.keras.layers.Dense(2, activation='sigmoid')(output0)
    output_right = tf.keras.layers.Dense(1, activation='sigmoid')(output_right)

    model = tf.keras.Model([inputs1, inputs2], [output_left, output_right])
    model.compile(optimizer=tf.keras.optimizers.Adam(0.01),
                  loss=tf.keras.losses.binary_crossentropy,
                  metrics='acc')
    model.fit([X1, X2], [y1, y2], epochs=1000, verbose=2)
    pred = model.predict([X1, X2], verbose=0)
    print(pred)


# model_and()
# model_xor()
# model_functional_1()
# model_functional_2()
model_functional_3()
