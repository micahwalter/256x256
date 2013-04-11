from PIL import Image
from random import randint

size = 256,256

im = Image.new("L", size)

for w in range(256):
	for h in range(256):
		im.putpixel((w,h), randint(0,256))

im.show()
