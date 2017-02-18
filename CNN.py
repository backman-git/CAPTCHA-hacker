



from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.advanced_activations import PReLU
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.optimizers import SGD, Adadelta, Adagrad
from keras.utils import np_utils, generic_utils
from six.moves import range
from digitSet import load_data
import numpy

seed = 7
numpy.random.seed(seed)

imgHeight=18
imgWidth=9


data, label = load_data()

print(data.shape[0], ' samples')

label = np_utils.to_categorical(label, 10)
num_classes=10


def baseline_model(num_pixels,num_classes):
	# create model
	model = Sequential()
	model.add(Dense(num_pixels, input_dim=num_pixels, init='normal', activation='relu'))
	model.add(Dense(num_classes, init='normal', activation='softmax'))
	# Compile model
	model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
	return model


def CNN(imgHeight,imgWidth):

	model = Sequential()
	model.add(Convolution2D(20, 3, 3, border_mode='valid', input_shape=(1, imgHeight, imgWidth), activation='relu'))
	model.add(MaxPooling2D(pool_size=(2, 2)))
	model.add(Dropout(0.2))
	model.add(Flatten())
	model.add(Dense(128, activation='relu'))
	model.add(Dense(num_classes, activation='softmax'))
	opt = SGD(lr=0.02)
	model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
	return model





#model=baseline_model(imgHeight*imgWidth,10)
#data = data.reshape(data.shape[0],imgHeight*imgWidth).astype("float32")

model =CNN(imgHeight,imgWidth)



model.fit(data, label, batch_size=32, nb_epoch=100,shuffle=True,verbose=1,show_accuracy=True,validation_split=0.06)

model.save("CNN.h5") 