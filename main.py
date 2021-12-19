from PIL import Image
import os

for file in os.listdir('original'):
	if file.endswith('.jpg'):
		image_file = Image.open(os.path.join('original', file)) 
		image_file = image_file.convert('L') 
		image_file.save(os.path.join('result', file[:3] + "_grey.png"))