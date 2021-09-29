# Day_10_02_LeNet5.py

import tensorflow as tf


# Quiz : mnist 데이터셋에 대해 LeNet5 모델을 구축하세요.
def mnist_LeNet5():
    (X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()
    X_train = X_train.reshape(-1, 28, 28, 1)
    X_test = X_test.reshape(-1, 28, 28, 1)

    X_train = X_train / 255
    X_test = X_test / 255

    model = tf.keras.Sequential()
    model.add(tf.keras.layers.InputLayer(input_shape=X_train.shape[1:]))

    model.add(tf.keras.layers.Conv2D(filters=6, kernel_size=5, strides=1, activation='relu'))
    model.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))
    model.add(tf.keras.layers.Conv2D(filters=16, kernel_size=5, strides=1, activation='relu'))
    model.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))

    model.add(tf.keras.layers.Flatten())

    model.add(tf.keras.layers.Dense(120, activation='relu', name='L1'))
    model.add(tf.keras.layers.Dense(84, activation='relu', name='L2'))
    model.add(tf.keras.layers.Dense(10, activation='softmax', name='L3'))
    model.summary()

    model.compile(optimizer=tf.keras.optimizers.Adam(0.001),
                  loss=tf.keras.losses.sparse_categorical_crossentropy,
                  metrics='acc')

    model.fit(X_train, y_train, epochs=10, batch_size=100, verbose=2)
    print(f"acc : {model.evaluate(X_test, y_test, verbose=0)}")


mnist_LeNet5()
