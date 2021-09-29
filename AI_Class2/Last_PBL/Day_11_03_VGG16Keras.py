# Day_11_03_VGG16Keras.py

# Quiz : 케라스에서 제공하는 VGG16 모델의 소스코드를 찾아서 보기 좋게 정리하세요.
import tensorflow as tf

model = tf.keras.Sequential()
model.add(tf.keras.layers.InputLayer(input_shape=[224, 224, 3]))

model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same', name='block1_conv1'))
model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same', name='block1_conv2'))
model.add(tf.keras.layers.MaxPool2D((2, 2), strides=(2, 2), name='block1_pool'))

model.add(tf.keras.layers.Conv2D(128, (3, 3), activation='relu', padding='same', name='block2_conv1'))
model.add(tf.keras.layers.Conv2D(128, (3, 3), activation='relu', padding='same', name='block2_conv2'))
model.add(tf.keras.layers.MaxPool2D((2, 2), strides=(2, 2), name='block2_pool'))

model.add(tf.keras.layers.Conv2D(256, (3, 3), activation='relu', padding='same', name='block3_conv1'))
model.add(tf.keras.layers.Conv2D(256, (3, 3), activation='relu', padding='same', name='block3_conv2'))
model.add(tf.keras.layers.Conv2D(256, (3, 3), activation='relu', padding='same', name='block3_conv3'))
model.add(tf.keras.layers.MaxPool2D((2, 2), strides=(2, 2), name='block3_pool'))

model.add(tf.keras.layers.Conv2D(512, (3, 3), activation='relu', padding='same', name='block4_conv1'))
model.add(tf.keras.layers.Conv2D(512, (3, 3), activation='relu', padding='same', name='block4_conv2'))
model.add(tf.keras.layers.Conv2D(512, (3, 3), activation='relu', padding='same', name='block4_conv3'))
model.add(tf.keras.layers.MaxPool2D((2, 2), strides=(2, 2), name='block4_pool'))

model.add(tf.keras.layers.Conv2D(512, (3, 3), activation='relu', padding='same', name='block5_conv1'))
model.add(tf.keras.layers.Conv2D(512, (3, 3), activation='relu', padding='same', name='block5_conv2'))
model.add(tf.keras.layers.Conv2D(512, (3, 3), activation='relu', padding='same', name='block5_conv3'))
model.add(tf.keras.layers.MaxPool2D((2, 2), strides=(2, 2), name='block5_pool'))

model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same', name='block1_conv1'))
model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same', name='block1_conv2'))
model.add(tf.keras.layers.MaxPool2D((2, 2), strides=(2, 2), name='block5_pool'))

model.add(tf.keras.layers.Flatten(name='flatten'))

model.add(tf.keras.layers.Dense(4096, activation='relu', name='fc1'))
model.add(tf.keras.layers.Dense(4096, activation='relu', name='fc2'))
model.add(tf.keras.layers.Dense(1000, activation='softmax', name='predictions'))

model.add(tf.keras.layers.Dense(4096, activation='relu', name='fc1'))

model.summary()
