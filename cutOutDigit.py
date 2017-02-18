from PIL import Image
import os

import theano



def cutOutDigit(img):

	imgList=[]
	width,height = img.size
	winWidth= width/4-2
	winHeight= height

	digit1Shift=6
	digit1=img.crop((0+digit1Shift,0,winWidth+digit1Shift,winHeight))
	imgList.append(digit1)
	
	digit2Shift=14
	digit2=img.crop((0+digit2Shift,0,winWidth+digit2Shift,winHeight))
	imgList.append(digit2)


	digit3Shift=22
	digit3=img.crop((0+digit3Shift,0,winWidth+digit3Shift,winHeight))
	imgList.append(digit3)

	digit4Shift=30
	digit4=img.crop((0+digit4Shift,0,winWidth+digit4Shift,winHeight))
	imgList.append(digit4)

	return imgList
# cut out numbers



sourceDir = "C:/Users/development/Desktop/hack/rawData/"
saveDir = "./dataSet/"







idx = [0 for x in range(10)]
for file in os.listdir(sourceDir):

	if file.endswith(".png"):

		fileName=file
		img = Image.open(sourceDir+fileName)
		width,height = img.size

		winWidth= width/4-2
		winHeight= height

		digit1Shift=6
		digit1=img.crop((0+digit1Shift,0,winWidth+digit1Shift,winHeight))

		digit1.save(saveDir+"/"+fileName[0]+str(idx[int(fileName[0])])+".png")
		idx[int(fileName[0])]+=1
		digit2Shift=14
		digit2=img.crop((0+digit2Shift,0,winWidth+digit2Shift,winHeight))
		#digit2.show()
		digit2.save(saveDir+"/"+fileName[1]+str(idx[int(fileName[1])])+".png")
		idx[int(fileName[1])]+=1
		digit3Shift=22
		digit3=img.crop((0+digit3Shift,0,winWidth+digit3Shift,winHeight))
		#digit3.show()
		digit3.save(saveDir+"/"+fileName[2]+str(idx[int(fileName[2])])+".png")
		idx[int(fileName[2])]+=1
		digit4Shift=30
		digit4=img.crop((0+digit4Shift,0,winWidth+digit4Shift,winHeight))
		#digit4.show()
		digit4.save(saveDir+"/"+fileName[3]+str(idx[int(fileName[3])])+".png")
		idx[int(fileName[3])]+=1

