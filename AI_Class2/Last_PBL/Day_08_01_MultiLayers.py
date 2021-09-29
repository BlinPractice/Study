# Day_08_01_MultiLayers.py

import tensorflow as tf
import numpy as np


# Quiz : load_data()로 가져온 데이터셋을 train, test로 분리하세요.
def mnist_basic():
    # data = tf.keras.datasets.mnist.load_data()

    # print(type(data), len(data))
    # # print(data[0])
    #
    # train_set, test_set = data
    # print(type(train_set), type(test_set))
    # print(len(train_set), len(test_set))
    #
    # X_train, y_train = train_set
    # X_test, y_test = test_set
    # print(X_train.shape, X_test.shape)
    # print(y_train.shape, y_test.shape)  # 1차원이므로 One-Hot vector가 아니구나~

    # Quiz : mnist 데이터셋에 대해 정확도를 구하세요.
    (X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()
    X_train = X_train.reshape(-1, 784)
    X_test = X_test.reshape(-1, 784)

    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(10, activation='softmax'))

    model.compile(optimizer=tf.keras.optimizers.SGD(0.1),
                  loss=tf.keras.losses.sparse_categorical_crossentropy,
                  metrics='acc')
    model.fit(X_train, y_train, epochs=1)

    pred = model.predict(X_test)
    pred_arg = np.argmax(pred, axis=1)  # 0:수직, 1:수평
    print(f"acc : {np.mean(pred_arg == y_test):.4f}")


def mnist_softmax():
    (X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()
    X_train = X_train.reshape(-1, 784)
    X_test = X_test.reshape(-1, 784)
    # print(np.min(X_train), np.max(X_train))
    # 영상처리에서는 항상 0 ~ 255

    # 0 ~ 1로 바꿔주는 min-max scaling
    X_train = X_train / 255
    X_test = X_test / 255

    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(10, activation='softmax'))

    # 이제 무조건 Adam 쓰기 (default=0.001)
    model.compile(optimizer=tf.keras.optimizers.Adam(0.001),
                  loss=tf.keras.losses.sparse_categorical_crossentropy,
                  metrics='acc')

    # verbose=0 : no show version
    # verbose=1 : default (full version)
    # verbose=2 : minimum version

    # batch_size
    # 60,000 개 --> 가중치 갱신 1 회 수행
    # 200 개 --> 가중치 갱신 300 회 수행

    # mini-batch algorithm
    model.fit(X_train, y_train, epochs=10, batch_size=32, verbose=2)
    print(f"acc : {model.evaluate(X_test, y_test, verbose=0)}")


# mnist_basic()
mnist_softmax()
