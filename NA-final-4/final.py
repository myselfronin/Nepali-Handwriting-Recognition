from keras.models import Model
from keras.layers import Input,Dense,Dropout
from keras.layers import Conv2D, MaxPooling2D, Flatten
import cv2
import numpy as np

inputs = Input(shape=(28,28,1))
x = Conv2D(filters = 64,
           kernel_size = 5,
           activation = 'relu')(inputs)
x = MaxPooling2D()(x)
x = Conv2D(filters = 32,
           kernel_size = 3,
           activation = 'relu')(x)
x = MaxPooling2D()(x)
x = Flatten()(x)
x=Dense(256,activation='relu')(x)
outputs = Dense(48, activation = 'softmax')(x)

model = Model(inputs = inputs, outputs = outputs)

model.summary()

# Convolutional Neural Network
from keras.utils import plot_model
plot_model(model, to_file='convolution_neural_network.png',show_shapes = True)

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.load_weights('FinalModelMajorProject.h5')

def predict(path):
    img = cv2.imread(path)
    img = np.expand_dims(img, axis=0)
    img = np.expand_dims(img, axis=-1)
    predit = model.predict(img)
    class_number = np.argmax(predict)
    return class_number


