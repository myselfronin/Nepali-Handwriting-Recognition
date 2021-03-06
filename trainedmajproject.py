# -*- coding: utf-8 -*-
"""trainedMajProject.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/157hmynJi-McG7iT_bPxIrgsng8G7YLRO
"""

# !wget "https://doc-0k-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/cjfao9149pmmju9ths6m54u0kgf2olvm/1562738400000/18360421921604353805/*/1CeXRoxtDBSabqbI9yplFSPhaItDjy7N0?e=download" -O dataset.zip
#
# !wget https://archive.ics.uci.edu/ml/machine-learning-databases/00389/DevanagariHandwrittenCharacterDataset.zip
#
# !unzip -q DevanagariHandwrittenCharacterDataset.zip
#
# !pip install tensorflow==1.13.1
# !pip install tensorflow-gpu==1.13.1
#
# !unzip -q '/content/dataset.zip'

import numpy as np 
import pandas as pd 
import random
import sys
import cv2
import glob
import matplotlib.pyplot as plt
from subprocess import check_output


# from keras.models import Sequential,Model
# from keras.layers import Conv2D,MaxPooling2D,Dense,Flatten,Input,Dropout,Activation,BatchNormalization
# from keras import losses
# from keras.optimizers import Adam, Adagrad
# from keras.callbacks import EarlyStopping
# from keras import regularizers
# from sklearn.model_selection import GridSearchCV
# from keras.preprocessing.image import ImageDataGenerator
# from keras.layers.normalization import BatchNormalization
# import keras
# from keras.layers import LeakyReLU, PReLU
# import os
# from keras.applications.vgg16 import VGG16
# from keras.applications.resnet50 import ResNet50
# from tqdm import tqdm


# import tensorflow
# from tensorflow.python.keras.models import Sequential,Model
# from tensorflow.python.keras.layers import Conv2D,MaxPooling2D,Input,Dense,Flatten,Dropout,Activation,BatchNormalization,GlobalAveragePooling2D
# from tensorflow.python.keras.layers import PReLU
# from tensorflow.python.keras import losses
# from tensorflow.python.keras.optimizers import Adam, Adagrad
# from tensorflow.python.keras.callbacks import EarlyStopping
# from tensorflow.python.keras import regularizers
# from sklearn.model_selection import GridSearchCV
# from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
# import keras
# from tensorflow.python.keras.layers import LeakyReLU, PReLU
# import os
# # from tensorflow.python.keras.applications.vgg16 import VGG16
# # from tensorflow.python.keras.applications.resnet50 import ResNet50
# from tensorflow.python.keras.applications.inception_resnet_v2 import InceptionResNetV2
# from tensorflow.python.keras.applications.inception_v3 import InceptionV3
# from tqdm import tqdm
from tensorflow.python.keras.callbacks import TensorBoard

train_datagen = ImageDataGenerator(
    rescale=1./255,
    #validation_split=0.2)
    shear_range=0.2,
#     zoom_range=[0.5, 1.25],
    rotation_range=15,
#     width_shift_range=0.1,
#     height_shift_range=0.1,
#     horizontal_flip=True,
    fill_mode="nearest",
    data_format='channels_last',
    brightness_range=[0.5, 1.5])
#     validation_split =0.2)


test_datagen = ImageDataGenerator(
#     horizontal_flip=True,
#                                   zoom_range=[0.5, 1.25],
    rescale=1./255, 
#     preprocessing_function=custom_func
  )

train_generator = train_datagen.flow_from_directory(
    '/content/DevanagariHandwrittenCharacterDataset/Train',
    target_size=(28, 28),
    batch_size=64,
    color_mode = 'grayscale',
    shuffle = True,
#     seed = 42,
    class_mode='categorical',
 )



valid_generator = train_datagen.flow_from_directory(
    directory="/content/DevanagariHandwrittenCharacterDataset/Test",
    target_size=(28, 28),
    color_mode="grayscale",
    batch_size=64,
    class_mode="categorical",
    shuffle=True,
#     seed=42,
)


# test_generator = test_datagen.flow_from_directory(
#     directory="/content/preprocessed/test",
#     target_size=(224, 224),
#     color_mode="rgb",
#     batch_size=16,
#     class_mode=None,
#     shuffle=False,
#     seed=42
# )

# x, y = train_generator.next()
# image = x[0]
# plt.imshow(image)

# base_model =ion_resnet_v2.InceptionResNetV2(include_top=True, weights='imagenet', classes=1000)
# # base_model.summary()

# base_model= InceptionV3(include_top=False, weights='imagenet',input_shape=(512,512,3))
# base_model.summary()

# base_model2 = ResNet50(include_top=True, weights='imagenet', input_tensor=None, input_shape=None, pooling=None, classes=1000)
# base_model2.summary()

# for layer in base_model.layers:
#     layer.trainable = False

def createmodel():
  visible = Input(shape=(28,28,1))
  conv1 = Conv2D(32, kernel_size=4, activation='relu')(visible)
#   pool1 = MaxPooling2D(pool_size=(2, 2))(conv1)
#   conv2 = Conv2D(16, kernel_size=4, activation='relu')(pool1)
#   pool2 = MaxPooling2D(pool_size=(2, 2))(conv2)
  flat = Flatten()(conv1)
  hidden1 = Dense(100, activation='relu')(flat)
  output = Dense(46, activation='softmax')(hidden1)
  model = Model(inputs=visible, outputs=output)



  model.compile(optimizer="adam",loss='categorical_crossentropy', metrics=['accuracy'])
  model.summary()
  return model

model = createmodel()

# def createmodel():
#   model = Sequential()
#   model.add(base_model)
# #   model.add(Conv2D(32,kernel_size = (7,7),strides=2, input_shape=(512,512,3), padding='same',activation=PReLU()))
# #   model.add(BatchNormalization())
# #   model.add(MaxPooling2D(pool_size=(2, 2),strides=2))
  
  
# #   model.add(Conv2D(32,kernel_size = (2,2),strides=1,padding='same', activation=PReLU()))  
# #   model.add(BatchNormalization())
  
# #   model.add(Conv2D(32,kernel_size = (2,2),strides=1,padding='same', activation=PReLU()))  
# #   model.add(BatchNormalization())
# #   model.add(MaxPooling2D(pool_size=(2, 2),strides=2, padding='valid'))

# #   model.add(Conv2D(32,kernel_size = (2,2),strides=1,padding='same', activation=PReLU()))  
# #   model.add(BatchNormalization())
# #   model.add(Conv2D(32,kernel_size = (2,2),strides=1,padding='same', activation=PReLU()))  
# #   model.add(BatchNormalization())
# #   model.add(MaxPooling2D(pool_size=(2, 2),strides=2, padding='valid'))

  
# #   model.add(Conv2D(128,kernel_size = (3,3),strides=1,padding='same', activation=PReLU()))
# #   model.add(BatchNormalization())  
# #   model.add(Conv2D(128,kernel_size = (3,3),strides=1,padding='same', activation=PReLU()))
# #   model.add(BatchNormalization())
# #   model.add(Conv2D(128,kernel_size = (3,3),strides=1,padding='same', activation=PReLU()))
# #   model.add(BatchNormalization())
# #   model.add(Conv2D(128,kernel_size = (3,3),strides=1,padding='same', activation=PReLU()))
# #   model.add(BatchNormalization())
  
  
# #   model.add(MaxPooling2D(pool_size=(2, 2),strides=2, padding='valid'))
  
  
  
# #   model.add(Conv2D(256,kernel_size = (3,3),strides=1,padding='same', activation=PReLU()))
# #   model.add(BatchNormalization())
# #   model.add(Conv2D(256,kernel_size = (3,3),strides=1,padding='same', activation=PReLU()))
# #   model.add(BatchNormalization())
# #   model.add(Conv2D(256,kernel_size = (3,3),strides=1,padding='same', activation=PReLU()))
# #   model.add(BatchNormalization())
# #   model.add(Conv2D(256,kernel_size = (3,3),strides=1,padding='same', activation=PReLU()))
# #   model.add(BatchNormalization())
  
  
# #   model.add(MaxPooling2D(pool_size=(2, 2),strides=2, padding='valid'))
# #   model.add(Dropout(0.5))
  
# #   model.add(Flatten())
  
  
# #   model.add(Dense(1024, activation=PReLU()))
# #   model.add(Dropout(0.5))
  
# #   model.add(Dense(512, activation=PReLU()))
# #   model.add(Dropout(0.1))
  
  
# #   model.add(Dense(5,activation = 'softmax'))
# #   model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.Adam(), metrics=["accuracy"])
  
  
  
#     #  here we added new layersD
#   model.add(GlobalAveragePooling2D())
#   model.add(Dense(1024, activation='relu'))
# #   model.add(Dropout(0.5))
#   model.add(Dense(5, activation='softmax', name ='output'))
  
# #   model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=["accuracy"])
# #   model.summary()
#   return model

# tbc = TensorBoardColab()
# tbc.save_image(title="test_title" , image=image)
# tbc.save_value("graph_name", "line_name", epoch, value)

# tbc.save_value("graph_name2", "line_name2", epoch, value2)
# tbc.flush_line(line_name)
# tbc.flush_line(line_name2)
# tbc.close()

LOG_DIR = '/gdrive/My Drive/ML/diabetic/training_logs/retinopathy'
MODEL_CHECKPOINT_NAME = 'model{epoch:03d}.hdf5'
MODEL_CHECKPOINT_DIRNAME = LOG_DIR + '/checkpoints/'

# rm -rf MODEL_CHECKPOINT_DIRNAME + '*.*'

!mkdir -p "{MODEL_CHECKPOINT_DIRNAME}"

!wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
!unzip ngrok-stable-linux-amd64.zip

from tensorflow.python.keras.callbacks import TensorBoard
base_dir = './logs'
tbCallBack = TensorBoard(log_dir=base_dir,
                         write_graph=True,
                         write_grads=True,
                         batch_size=32,
                         write_images=True,
                         update_freq='batch')

get_ipython().system_raw(
    'tensorboard --logdir {} --host 0.0.0.0 --port 6006 &'
    .format(base_dir)
)

get_ipython().system_raw('./ngrok authtoken 45Npt76HKnzZUgWh4ciwi_3wa9qRRs65bKe4SVbNLkz &')
get_ipython().system_raw('./ngrok http 6006 &')

!curl -s http://localhost:4040/api/tunnels | python3 -c \
    "import sys, json; print(json.load(sys.stdin)['tunnels'][0]['public_url'])"

import glob, os
from tensorflow.python.keras.callbacks import ModelCheckpoint
from tensorflow.python.keras.models import load_model

def get_init_epoch(check_point_path):
    check_point_list = glob.glob(os.path.join(check_point_path, 'model*.hdf5'))
    base_names = [os.path.basename(check_point) for check_point in check_point_list]
    epochs = [int(re.search(r'\d+', string).group()) for string in base_names]
    return np.max(epochs) if epochs else 0

def load_saved_model(model_path):
    model = load_model(model_path)
    return model

import re

# rm -rf "/gdrive/My Drive/ML/"

init_epoch = get_init_epoch(MODEL_CHECKPOINT_DIRNAME)
print(init_epoch)
if init_epoch:
    model_path = MODEL_CHECKPOINT_DIRNAME + MODEL_CHECKPOINT_NAME.format(epoch=init_epoch)
    model = load_saved_model(model_path)
    model.summary()
else:
    model = createmodel()

model_checkpoint_callback = ModelCheckpoint(MODEL_CHECKPOINT_DIRNAME + MODEL_CHECKPOINT_NAME)

model = createmodel()

history=model.fit_generator(
    train_generator,
    #steps_per_epoch=300,
    epochs=1000,
    validation_data=valid_generator,
    #validation_steps=75,
    verbose=1, 
#     callbacks=[model_checkpoint_callback, tbCallBack], initial_epoch=init_epoch
    )

import cv2

img = cv2.imread('/content/101562723945.3303716.png', 0)
img.shape

import numpy as np

img = np.expand_dims(img, axis=0)
img = np.expand_dims(img, axis=-1)

pred = model.predict(img)

np.argmax(pred)

train_generator.class_indices

r5plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])


plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()

# Plot training & validation loss values
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])

plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()

import sys
import matplotlib
print("Generating plots...")
sys.stdout.flush()
matplotlib.use("Agg")
matplotlib.pyplot.style.use("ggplot")
matplotlib.pyplot.figure()
N = EPOCHS
matplotlib.pyplot.plot(np.arange(0, N), history.history["loss"], label="train_loss")
matplotlib.pyplot.plot(np.arange(0, N), history.history["val_loss"], label="val_loss")
matplotlib.pyplot.plot(np.arange(0, N), history.history["acc"], label="train_acc")
matplotlib.pyplot.plot(np.arange(0, N), history.history["val_acc"], label="val_acc")
matplotlib.pyplot.title("Training Loss and Accuracy on diabetic retinopathy detection")
matplotlib.pyplot.xlabel("Epoch #")
matplotlib.pyplot.ylabel("Loss/Accuracy")
matplotlib.pyplot.legend(loc="lower left")
matplotlib.pyplot.savefig("plot.png")

STEP_SIZE_TRAIN=train_generator.n//train_generator.batch_size
STEP_SIZE_VALID=valid_generator.n//valid_generator.batch_size
model.evaluate_generator(generator=valid_generator,
steps=STEP_SIZE_VALID)

test_generator = test_datagen.flow_from_directory(
    directory="/content/resized/test/",
    target_size=(224, 224),
    color_mode="rgb",
    batch_size=1,
    class_mode=None,
    shuffle=False,
    seed=42
)

STEP_SIZE_TEST=test_generator.n//test_generator.batch_size
test_generator.reset()
pred=model.predict_generator(test_generator,
steps=STEP_SIZE_TEST,
verbose=1)

predicted_class_indices=np.argmax(pred,axis=1)

labels = (train_generator.class_indices)
labels = dict((v,k) for k,v in labels.items())
predictions = [labels[k] for k in predicted_class_indices]

predictions

filenames=test_generator.filenames
results=pd.DataFrame({"Filename":filenames,
                      "Predictions":predictions})
results.to_csv("results.csv",index=False)

