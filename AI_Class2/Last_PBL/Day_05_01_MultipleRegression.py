# Day_05_01_MultipleRegression.py
import numpy as np
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt


def multiple_basic():
    # 공부 시간, 출석 일수
    x = [[1, 0],
         [0, 2],
         [3, 0],
         [0, 4],
         [5, 0],
         [0, 6]]
    y = [[1],
         [2],
         [3],
         [4],
         [5],
         [6]]

    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(1))
    model.compile(optimizer='sgd', loss='mse')
    model.fit(x, y, epochs=100)
    print(model.predict(x))


# Quiz : trees.csv 파일에서 Girth, Height로 학습해서 Volume을 예측하세요.
def multiple_trees():
    trees = pd.read_csv('./data/trees.csv', index_col=0)
    values = trees.values
    # x = values[:, :2]
    # y = values[:, 2:]
    x = values[:, :-1]
    y = values[:, -1:]

    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(1))
    model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=0.1**4),
                  loss=tf.keras.losses.mse)
    model.fit(x, y, epochs=100)

    pred = model.predict(x)
    mae = np.mean(np.abs(pred - y))     # mean absolute error
    print(f"mae : {mae}")

    pred = pred.reshape(-1)
    plt.plot(x, y, 'ro')
    plt.plot(x, pred, 'go')
    plt.show()


# multiple_basic()
multiple_trees()
