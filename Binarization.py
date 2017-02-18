

import os
from PIL import Image

imgs = os.listdir("./dataSet/")
num = len(imgs)

for i in range(num):
	img = Image.open("./dataSet/"+imgs[i])
	img=img.convert("1")

	img.save("./dataSetB/"+imgs[i].split(".")[0]+"tt."+imgs[i].split(".")[1])	