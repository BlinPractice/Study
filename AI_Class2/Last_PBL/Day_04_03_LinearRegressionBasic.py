# Day_04_03_LinearRegressionBasic.py

# ML(old AI), DL(recent AI)
# DL Basic
# - linear regression, multiple regression, logistic regression, softmax regression
# DL Advanced
# - image processing (CNN), NLP(RNN), RL, recommend algorithm

import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt


def linear_basic():
    x = [1, 2, 3]   # column, feature
    y = [1, 2, 3]   # answer, label, target

    # Dense is good at regression (숫자예측)
    # Dense layer = fully connected (행렬 곱셈)
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(1))

    # sgd : 경사하강법 (가장 기초)
    model.compile(optimizer='sgd',  # stochastic gradient descent
                  loss='mse')       # mean square error

    # 학습
    model.fit(x, y, epochs=100)    # epochs : 학습 횟수

    print(model.predict(x))
    print(model.predict([5, 7]))


# Quiz : cars.csv 파일을 읽어서 speed를 학습하여 dist 타겟을 예측하세요.
"""
1. 파일을 읽어옵니다.
2. X, y 데이터를 추출합니다.
3. 모델을 구축합니다.
4. 결과를 예측합니다.
5. 시각화로 표현합니다.
"""


def linear_cars():
    # 1. 파일 읽기
    cars = pd.read_csv('./data/cars.csv', index_col=0)

    # 2. X, y 데이터 추출
    ## 2.1 컬럼 하나만 적용 가능
    # x = cars.speed
    # y = cars.dist
    ## 2.2 여러 컬럼을 적용 가능 (실무적, 매우 중요!!)
    values = cars.values
    x = values[:, 0]
    y = values[:, 1]

    # 3. 모델 구출
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(1))
    # inf : infinite
    # nan : not a number
    # learning_rate 작게, epochs 크게
    model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=0.001),     # class
                  loss=tf.keras.losses.mse)     # function
    model.fit(x, y, epochs=100)

    # 4. 결과 예측
    pred = model.predict(x)
    pred = pred.reshape(-1)

    # 5. 시각화
    plt.plot(x, y, 'ro')    # 'o'를 쓰면 산점도
    plt.plot(x, pred, 'g')
    plt.show()


# linear_basic()
linear_cars()
