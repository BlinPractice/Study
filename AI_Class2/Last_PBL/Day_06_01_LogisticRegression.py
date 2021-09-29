# Day_06_01_LogisticRegression.py

import numpy as np
import tensorflow as tf
import pandas as pd
from sklearn import preprocessing, model_selection
# scikit-learn : 실제 작업하는 친구
# sklearn : 사용하기 편하게 만들어진 친구


def logistic_basic():
    # 공부 시간, 출석 일수
    # x : 공부 시간, 출석 일수
    # y : 성적(multiple), 과락(logistic), 학점(softmax)
    x = [[1, 2],    # 탈락
         [2, 1],
         [4, 5],
         [5, 4],
         [8, 9],    # 통과
         [9, 8]]
    y = [[0],
         [0],
         [0],
         [0],
         [1],
         [1]]

    model = tf.keras.Sequential()

    # sigmoid curve = 1 / (1 + e^(-z)) --> 0~1
    # e : 오일러 상수
    model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
    # model.add(tf.keras.layers.Activation(tf.keras.activations.sigmoid))
    # model.add(tf.keras.layers.Activation('sigmoid'))

    model.compile(optimizer='sgd',
                  loss=tf.keras.losses.binary_crossentropy,
                  metrics='acc')    # acc : accuracy
    model.fit(x, y, epochs=10)

    pred = model.predict(x)
    print(pred)
    print(pred.shape, np.int32(y).shape)

    pred_bool = (pred > 0.5)
    print(pred_bool)
    print(np.int32(pred_bool))

    equals = (pred_bool == y)   # 반드시 shape이 같아야 함
    print(equals)

    print(f"acc : {np.mean(equals)}")


# Quiz : 당뇨병 데이터를 학습하고 정확도를 구하세요.
def logistic_diabetes():
    diab = pd.read_csv('./data/pima-indians-diabetes.csv',
                       skiprows=9,      # row 10부터 시작
                       header=None)     # no column name
    values = diab.values
    x = values[:, :-1]
    y = values[:, -1:]

    # very very important
    x = preprocessing.scale(x)              # 77.86 %
    # x = preprocessing.minmax_scale(x)     # 66.28 %

    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
    model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=0.01),
                  loss=tf.keras.losses.binary_crossentropy,
                  metrics='acc')
    model.fit(x, y, epochs=100)

    pred = model.predict(x)
    pred_bool = (pred > 0.5)
    print(f"acc : {np.mean(pred_bool == y):.4f}")


# Quiz : 80% 데이터로 학습하고 20% 데이터로 정확도를 구하세요.
def logistic_diabetes_splits():
    diab = pd.read_csv('./data/pima-indians-diabetes.csv',
                       skiprows=9,      # row 10부터 시작
                       header=None)     # no column name
    values = diab.values
    x = values[:, :-1]
    y = values[:, -1:]

    # very very important
    x = preprocessing.scale(x)              # 77.86 %
    # x = preprocessing.minmax_scale(x)     # 66.28 %

    # x 데이터 분할
    # x_train, x_test = x[:600], x[600:]
    # y_train, y_test = y[:600], y[600:]
    # train_size = int(len(x) * 0.8)
    # x_train, x_test = x[:train_size], x[train_size:]
    # y_train, y_test = y[:train_size], y[train_size:]

    # 75:25
    # x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y)
    # print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)

    # 80:20
    # x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y,
    #                                                                     train_size=0.8)
    # print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)

    # 600:168
    x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y,
                                                                        train_size=600)
    print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)

    # modeling
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
    model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=0.01),
                  loss=tf.keras.losses.binary_crossentropy,
                  metrics='acc')
    model.fit(x_train, y_train, epochs=100)

    # prediction
    pred = model.predict(x_test)
    pred_bool = (pred > 0.5)
    print(f"acc : {np.mean(pred_bool == y_test)}")


# logistic_basic()
logistic_diabetes()
# logistic_diabetes_splits()
