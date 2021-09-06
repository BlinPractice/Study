# Day_04_03_LinearRegressionBasic.py

# ML(old AI), DL(recent AI)
# DL Basic
# - linear regression, multiple regression, logistic regression, softmax regression
# DL Advanced
# - image processing (CNN), NLP(RNN), RL, recommend algorithm

import tensorflow as tf

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
