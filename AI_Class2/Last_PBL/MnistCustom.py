# MnistCustom.py

import tensorflow as tf
# Pillow


# Quiz : Generator 기본 코드를 사용해서 베이스라인 모델을 구축하세요.
def custom_mnist_1():
    gen_train = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1/255)
    flow_train = gen_train.flow_from_directory('train', target_size=[32, 32],
                                               batch_size=16, class_mode='sparse')

    gen_test = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1/255)
    flow_test = gen_test.flow_from_directory('test', target_size=[32, 32],
                                             batch_size=16, class_mode='sparse')

    # X, y = flow_train.next()
    # print(X.shape, y.shape)

    model = tf.keras.Sequential()
    model.add(tf.keras.layers.InputLayer(input_shape=[32, 32, 3]))

    # model.add(tf.keras.layers.Conv2D(filters=6, kernel_size=3, strides=1))
    model.add(tf.keras.layers.Conv2D(6, 3, 1, 'same', activation='relu'))
    model.add(tf.keras.layers.Conv2D(10, 3, 1, 'same', activation='relu'))
    model.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))

    model.add(tf.keras.layers.Conv2D(16, 3, 1, 'same', activation='relu'))
    model.add(tf.keras.layers.Conv2D(26, 3, 1, 'same', activation='relu'))
    model.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))

    model.add(tf.keras.layers.Flatten())

    model.add(tf.keras.layers.Dense(64, activation='relu'))
    model.add(tf.keras.layers.Dense(10, activation='softmax'))
    # model.summary()

    # compile
    model.compile(optimizer=tf.keras.optimizers.Adam(0.001),
                  loss=tf.keras.losses.sparse_categorical_crossentropy,
                  metrics='acc')

    model.fit(flow_train, epochs=10, verbose=2, validation_data=flow_test)


def custom_mnist_2():
    gen_train = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1 / 255,
                                                                rotation_range=30,
                                                                zoom_range=0.1)
    flow_train = gen_train.flow_from_directory('train', target_size=[32, 32],
                                               batch_size=16, class_mode='sparse')

    gen_test = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1 / 255)
    flow_test = gen_test.flow_from_directory('test', target_size=[32, 32],
                                             batch_size=16, class_mode='sparse')

    model = tf.keras.Sequential()
    model.add(tf.keras.layers.InputLayer(input_shape=[32, 32, 3]))

    model.add(tf.keras.layers.Conv2D(6, 3, 1, 'same'))
    model.add(tf.keras.layers.BatchNormalization())
    model.add(tf.keras.layers.ReLU())
    model.add(tf.keras.layers.Conv2D(10, 3, 1, 'same'))
    model.add(tf.keras.layers.BatchNormalization())
    model.add(tf.keras.layers.ReLU())
    model.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))

    model.add(tf.keras.layers.Conv2D(16, 3, 1, 'same'))
    model.add(tf.keras.layers.BatchNormalization())
    model.add(tf.keras.layers.ReLU())
    model.add(tf.keras.layers.Conv2D(26, 3, 1, 'same'))
    model.add(tf.keras.layers.BatchNormalization())
    model.add(tf.keras.layers.ReLU())
    model.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))

    model.add(tf.keras.layers.Flatten())

    model.add(tf.keras.layers.Dense(64, activation='relu'))
    model.add(tf.keras.layers.Dense(10, activation='softmax'))
    # model.summary()

    # compile
    model.compile(optimizer=tf.keras.optimizers.Adam(0.001),
                  loss=tf.keras.losses.sparse_categorical_crossentropy,
                  metrics='acc')

    model.fit(flow_train, epochs=10, verbose=2, validation_data=flow_test)


def custom_mnist_3():
    gen_train = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1/255)
    flow_train = gen_train.flow_from_directory('train', target_size=[32, 32],
                                               batch_size=16, class_mode='sparse')

    gen_test = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1/255)
    flow_test = gen_test.flow_from_directory('test', target_size=[32, 32],
                                             batch_size=16, class_mode='sparse')

    # ResNet50에서 학습도 하고 웨이트 값 등을 가져와서 내 모델이랑 합침
    # include_top : 보통은 False를 사용하여 학습만 가져옴
    # 이미 이미지 경시대회에서 학습하고 예측한 모델이라 업데이트 하면 안됨
    conv_base = tf.keras.applications.VGG16(include_top=False,
                                            input_shape=[32, 32, 3])
    conv_base.trainable = False

    model = tf.keras.Sequential()
    model.add(conv_base)

    model.add(tf.keras.layers.Flatten())

    model.add(tf.keras.layers.Dense(64, activation='relu'))
    model.add(tf.keras.layers.Dense(10, activation='softmax'))
    model.summary()

    model.compile(optimizer=tf.keras.optimizers.Adam(0.001),    # RMSProp
                  loss=tf.keras.losses.sparse_categorical_crossentropy,
                  metrics='acc')
    model.fit(flow_train, epochs=10, verbose=2, validation_data=flow_test)


# custom_mnist_1()
# custom_mnist_2()
custom_mnist_3()

# 김정훈 : applekoong@naver.com
