
from selenium import webdriver
import time
import pyscreenshot as ImageGrab
from PIL import Image
from multiprocessing import Process, freeze_support
if __name__ == '__main__':
	freeze_support() 

	web = webdriver.Chrome()
	web.get('https://elearning.rad.gov.tw/fet/home/courses/')

	for i in range(200):
		
		web.set_window_position(0,0) 
	
		web.set_window_size(500,500)


		winWidth , winHeight = (44,18)  #44,18
		leftPointX=138
		leftPointY=408

		im=ImageGrab.grab(bbox=(leftPointX,leftPointY,leftPointX+winWidth,leftPointY+winHeight)) # X1,Y1,X2,Y2
		im.save("./rawData/"+str(i)+".png")
		
		web.refresh()

	web.close()
