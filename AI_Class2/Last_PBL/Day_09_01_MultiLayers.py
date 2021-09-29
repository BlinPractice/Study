# Day_09_01_MultiLayers.py

import tensorflow as tf


# Quiz : single layer로 되어 있는 mnist_softmax 함수를 multi layers 버전으로 수정하세요.
# (목표 : 이전 코드보다 정확도 향상)
def mnist_multi_layers():
    (X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()
    X_train = X_train.reshape(-1, 784)
    X_test = X_test.reshape(-1, 784)

    X_train = X_train / 255
    X_test = X_test / 255

    # 피처를 줄여야 정확도가 높아짐 ( 784 --> 10 )
    # single : 784 --> 10
    # multi  : 784 --> 256 --> 64 --> 10
    # model.add(tf.keras.layers.Dense(10)) 여러 개 쓰면 multi layers
    model = tf.keras.Sequential()   # 784
    # activation을 각각 추가해야 layer가 분리되어 정확도가 높아짐
    # sigmoid --> banishing gradient 발생
    # banishing gradient : 값이 너무 작아져서 소멸됨
    # 처음 Dense : sigmoid --> relu

    # 입력 데이터 생성 : shape을 나타내기 때문에 대괄호는 반드시 써야 함!!
    model.add(tf.keras.layers.InputLayer(input_shape=X_train.shape[-1]))    # 784

    # (60000, 256) = (60000, 784) @ (784, 256) + (256,) ==> hx = wx + b
    # wx : 위의 행렬곱셈을 표현함
    # bias = (256,)
    # 784 * 256 + 256 = 200,960
    model.add(tf.keras.layers.Dense(256, activation='relu', name='L1'))

    # Quiz : 아래 layer에서의 가중치 갯수를 구하세요
    # 256 * 64 + 64
    # (60000, 64) = (60000, 256) @ (256, 64) + (64,)
    model.add(tf.keras.layers.Dense(64, activation='relu', name='L2'))

    # Quiz : 아래 layer에서의 가중치 갯수를 구하세요
    # 64 * 10 + 10
    # (60000, 10) = (60000, 64) @ (64, 10) + (10,)
    model.add(tf.keras.layers.Dense(10, activation='softmax', name='L3'))
    # 반드시 non-linear 하도록 맞춰줘야함.
    # sigmoid, softmax, ...

    # 60000 : 데이터의 갯수로, 마지막까지 살아있음.
    # multi layers : 피처의 갯수만 줄여서 정확도를 높이는 것.

    # 요약 코드는 여기에 써야 함!!
    model.summary()     # 60000 --> None

    model.compile(optimizer=tf.keras.optimizers.Adam(0.001),
                  loss=tf.keras.losses.sparse_categorical_crossentropy,
                  metrics='acc')

    model.fit(X_train, y_train, epochs=10, batch_size=100, verbose=2)
    print(f"acc : {model.evaluate(X_test, y_test, verbose=0)}")
    #
    # pred = model.predict(X_test)
    # print(pred.shape)


mnist_multi_layers()
