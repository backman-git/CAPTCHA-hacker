

import os
from PIL import Image
import numpy as np



num_data = 792
imgWidth , imgHeight = 9,18 
def load_data():
	data = np.empty((num_data,1,imgHeight,imgWidth),dtype="float32")
	label = np.empty((num_data,),dtype="uint8")
	
	
	imgs = os.listdir("./dataSetB/")
	num = len(imgs)
	for i in range(num):
		img = Image.open("./dataSetB/"+imgs[i])
		arr = np.asarray(img,dtype="float32")
		data[i,:,:,:] = arr

		#print imgs[i]+","+imgs[i][0]

		label[i] = int(imgs[i][0])
	data /= np.max(data)
	data -= np.mean(data)
	return data,label


def load_data2(imgList):
	data = np.empty((len(imgList),1,imgHeight,imgWidth),dtype="float32")
	
	num = len(imgList)
	for i in range(num):
		img = imgList[i]
		arr = np.asarray(img,dtype="float32")
		data[i,:,:,:] = arr

		#print imgs[i]+","+imgs[i][0]

		
	data /= np.max(data)
	data -= np.mean(data)
	return data

