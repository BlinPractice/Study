# Day_07_01_SoftmaxRegression.py

import numpy as np
import tensorflow as tf
import pandas as pd
from sklearn import preprocessing, model_selection


def softmax_basic():
    # 공부 시간, 출석 일수
    x = [[1, 2],    # C
         [2, 1],
         [4, 5],    # B
         [5, 4],
         [8, 9],    # A
         [9, 8]]
    y = [[0, 0, 1],     # one-hot vector
         [0, 0, 1],
         [0, 1, 0],
         [0, 1, 0],
         [1, 0, 0],
         [1, 0, 0]]

    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(3, activation='softmax'))

    model.compile(optimizer=tf.keras.optimizers.SGD(0.1),
                  loss=tf.keras.losses.categorical_crossentropy,
                  metrics='acc')
    model.fit(x, y, epochs=100)

    pred = model.predict(x)
    print(pred, end='\n\n')

    # argmax : max의 위치
    pred_arg = np.argmax(pred, axis=1)  # 0:수직, 1:수평
    print(pred_arg)

    y_arg = np.argmax(y, axis=1)
    print(y_arg, end='\n\n')

    print(f"acc : {np.mean(pred_arg == y_arg)}")


# Quiz : iris_OneHot 파일을 읽어서 70%로 학습 후 30%를 예측하세요.
def softmax_iris_OneHot():
    iris = pd.read_csv('./data/iris_OneHot.csv')
    values = iris.values
    x = values[:, :-3]
    y = values[:, -3:]

    # indexing --> 그루핑(편향)됐기 때문에 결과를 잘 예측하지 못 함.
    # x_train, x_test = x[:105], x[105:]
    # y_train, y_test = y[:105], y[105:]
    # 한마디로 setosa, virsicolor를 학습하고 virginica만 예측하는 꼴

    # 70:30
    x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y,
                                                                        train_size=0.7)

    # training
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(3, activation='softmax'))
    model.compile(optimizer=tf.keras.optimizers.SGD(0.1),
                  loss=tf.keras.losses.categorical_crossentropy,
                  metrics='acc')
    model.fit(x_train, y_train, epochs=100)

    # prediction
    pred = model.predict(x_test)
    print(pred, end='\n\n')
    pred_arg = np.argmax(pred, axis=1)
    print(pred_arg)
    y_arg = np.argmax(y_test, axis=1)
    print(y_arg, end='\n\n')
    print(f"acc : {np.mean(pred_arg == y_arg)*100:.2f} %")


def softmax_iris_binarizer():
    iris = pd.read_csv('./data/iris.csv')
    x = iris.values[:, :-1]     # object data
    x = np.float32(x)           # float data

    # string --> one-hot encoding
    y = preprocessing.LabelBinarizer().fit_transform(iris.variety)

    # 70:30
    x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y,
                                                                        train_size=0.7)

    # training
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(3, activation='softmax'))
    model.compile(optimizer=tf.keras.optimizers.SGD(0.1),
                  loss=tf.keras.losses.categorical_crossentropy,
                  metrics='acc')
    model.fit(x_train, y_train, epochs=100)

    # prediction
    pred = model.predict(x_test)
    print(pred, end='\n\n')
    pred_arg = np.argmax(pred, axis=1)
    print(pred_arg)
    y_arg = np.argmax(y_test, axis=1)
    print(y_arg, end='\n\n')
    print(f"acc : {np.mean(pred_arg == y_arg)*100:.2f} %")


def softmax_iris_encoder():
    iris = pd.read_csv('./data/iris.csv')
    x = iris.values[:, :-1]
    x = np.float32(x)

    # LabelEncoder() : argmax 처리까지 진행 --> 단순 인코딩
    y = preprocessing.LabelEncoder().fit_transform(iris.variety)

    # 70:30
    x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y,
                                                                        train_size=0.7)

    # training
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(3, activation='softmax'))
    model.compile(optimizer=tf.keras.optimizers.SGD(0.1),
                  # sparse~ : y가 단순 인코딩 됐다고 알려줌
                  loss=tf.keras.losses.sparse_categorical_crossentropy,
                  metrics='acc')
    model.fit(x_train, y_train, epochs=100)

    # prediction
    pred = model.predict(x_test)
    pred_arg = np.argmax(pred, axis=1)
    print(f"acc : {np.mean(pred_arg == y_test):.4f}")


# softmax_basic()
# softmax_iris_OneHot()
# softmax_iris_binarizer()
softmax_iris_encoder()
