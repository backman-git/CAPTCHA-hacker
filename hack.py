


#hack CAPTCHA https://elearning.rad.gov.tw/fet/home/courses

from selenium import webdriver
import pyscreenshot as ImageGrab
from PIL import Image
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D,Activation, Dropout, Flatten, Dense
from keras.optimizers import SGD, Adadelta, Adagrad
from multiprocessing import Process, freeze_support

from digitSet import load_data2, load_data
import numpy as np

from cutOutDigit import cutOutDigit

def getCAPTCHA(web):

	
	web.set_window_position(0,0) 
	web.set_window_size(200,500)
	web.get('https://elearning.rad.gov.tw/fet/home/courses/')
	winWidth , winHeight = (44,18)  #44,18
	leftPointX=138
	leftPointY=408
	im=ImageGrab.grab(bbox=(leftPointX,leftPointY,leftPointX+winWidth,leftPointY+winHeight))
	
	return im


def getDigit_CNN(generator,model):
	print model.predict_generator(generator,4)



def genCNN(imgHeight,imgWidth):

	model = Sequential()
	model.add(Convolution2D(20, 3, 3, border_mode='valid', input_shape=(1, imgHeight, imgWidth), activation='relu'))
	model.add(MaxPooling2D(pool_size=(2, 2)))
	model.add(Dropout(0.2))
	model.add(Flatten())
	model.add(Dense(128, activation='relu'))
	model.add(Dense(10, activation='softmax'))
	opt = SGD(lr=0.05)
	model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
	
	model.load_weights('CNN.h5')

	return model



if __name__ == '__main__':
	freeze_support() 
	
	imgHeight=18
	imgWidth=9
	
	

	web = webdriver.Chrome()
	CAPTCHA=getCAPTCHA(web)




	imgList=cutOutDigit(CAPTCHA)

	for i in range(len( imgList)):
		imgList[i]=imgList[i].convert("1")


	data=load_data2(imgList)

	#data,label=load_data()
	

	model=genCNN(imgHeight,imgWidth)

	

	print model.predict_classes(data)
	




		


