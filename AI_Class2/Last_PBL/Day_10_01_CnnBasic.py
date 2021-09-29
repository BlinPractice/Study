# Day_10_01_CnnBasic.py

import tensorflow as tf

# Quiz : 케라스에서 제공하는 mnist 데이터셋에 대해 CNN 모델을 구축하세요.
# model = tf.keras.Sequential()

# model.add(tf.keras.layers.Conv2D(filters=6, kernel_size=[5, 5], strides=[1, 1]))
# model.add(tf.keras.layers.Conv2D(filters=6, kernel_size=5, strides=1))

# Quiz : pooling layer를 추가하세요.
# model.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))


def mnist_cnn():
    (X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()
    X_train = X_train.reshape(-1, 28, 28, 1)
    X_test = X_test.reshape(-1, 28, 28, 1)

    X_train = X_train / 255
    X_test = X_test / 255

    model = tf.keras.Sequential()
    # model.add(tf.keras.layers.InputLayer(input_shape=[28, 28, 1]))
    model.add(tf.keras.layers.InputLayer(input_shape=X_train.shape[1:]))
    # 필터 1개 : 5 x 5 x 1
    # 전체 : 필터 x 6 + 6 = (5*5) * 6 + 6 = 156
    model.add(tf.keras.layers.Conv2D(filters=6, kernel_size=5, strides=1))
    model.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))

    # 3차원을 1차원으로
    # model.add(tf.keras.layers.Reshape([12*12*6]))
    # model.add(tf.keras.layers.Reshape([-1]))
    model.add(tf.keras.layers.Flatten())

    model.add(tf.keras.layers.Dense(64, activation='relu', name='L2'))
    model.add(tf.keras.layers.Dense(10, activation='softmax', name='L3'))
    model.summary()

    model.compile(optimizer=tf.keras.optimizers.Adam(0.001),
                  loss=tf.keras.losses.sparse_categorical_crossentropy,
                  metrics='acc')

    model.fit(X_train, y_train, epochs=10, batch_size=100, verbose=2)
    print(f"acc : {model.evaluate(X_test, y_test, verbose=0)}")


mnist_cnn()
