from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np
import edgeDetection

model = Sequential()

model.add(Dense(410, input_shape=(1,1), activation='relu'))

model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])

x = np.array([1])
x = np.reshape(x, (1,1,1))
y = np.array(edgeDetection.getRedImage("ePicture.png"))
y = np.reshape(y, (1, 396,410))
print(len(y), len(y[0]))

model.fit(x,y, epochs = 5)
