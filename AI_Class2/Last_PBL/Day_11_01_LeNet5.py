# Day_11_01_LeNet5.py

import tensorflow as tf


def mnist_LeNet5():
    (X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()
    X_train = X_train.reshape(-1, 28, 28, 1)
    X_test = X_test.reshape(-1, 28, 28, 1)

    X_train = X_train / 255
    X_test = X_test / 255

    model = tf.keras.Sequential()
    model.add(tf.keras.layers.InputLayer(input_shape=X_train.shape[1:]))

    # padding 추가
    # valid : 24, 24
    # same : 28, 28 --> padding이 두 픽셀씩 추가됐다. (왼쪽에 2 pixel, 오른쪽에 2 pixel)
    model.add(tf.keras.layers.Conv2D(filters=6, kernel_size=5, strides=1, padding='same', activation='relu'))
    # 위의 코드는 same 적용
    model.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))    # same, valid 동일하다.
    model.add(tf.keras.layers.Conv2D(filters=16, kernel_size=5, strides=1,  padding='valid', activation='relu'))
    # LeNet5 에서는 valid가 맞는 값이다. (바로 위의 코드)
    model.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))

    model.add(tf.keras.layers.Flatten())

    model.add(tf.keras.layers.Dense(120, activation='relu', name='L1'))
    model.add(tf.keras.layers.Dense(84, activation='relu', name='L2'))
    model.add(tf.keras.layers.Dense(10, activation='softmax', name='L3'))
    model.summary()

    model.compile(optimizer=tf.keras.optimizers.Adam(0.001),
                  loss=tf.keras.losses.sparse_categorical_crossentropy,
                  metrics='acc')

    # validation_split 추가 : train 데이터를 나눠서 20% validation 진행
    # model.fit(X_train, y_train, epochs=10, batch_size=100, verbose=2, validation_split=0.2)
    # print(f"acc : {model.evaluate(X_test, y_test, verbose=0)}")

    # validation 셋이 따로 존재할 때
    model.fit(X_train, y_train, epochs=10, batch_size=100, verbose=2, validation_data=(X_test, y_test))
    print(f"acc : {model.evaluate(X_test, y_test, verbose=0)}")


mnist_LeNet5()
