import tensorflow as tf
from tensorflow import keras
import numpy as np

xs = np.array([-2.0, 0.0, 4.0, 1.0, 6.0, 5.0, 3.0, -3.0], dtype=float)
ys = np.array([-10.0, -4.0, 8.0, -1.0, 14.0, 11.0, 5.0, -13.0], dtype=float)

model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')

model.fit(xs, ys, epochs=300)
print(model.predict([8.0]))