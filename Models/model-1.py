from tensorflow.python.keras.models import Model
from tensorflow.python.keras.layers import Input,Dense,Dropout
from tensorflow.python.keras.layers import Conv2D, MaxPooling2D, Flatten

def model_one():
    # one conv2d and dense
    inputs = Input(shape=input_shape)
    x = Conv2D(filters=32,
               kernel_size=3,
               activation='relu')(inputs)
    x = Flatten()(x)
    outputs = Dense(24, activation='softmax')(x)
