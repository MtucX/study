#stegano challenge
import Image
img = Image.open('image.png')
img = img.convert('RGB')
width = img.size[0]
height = img.size[1]/2
key = ""
for i in range(25,width,50):
	r, g, b = img.getpixel((i, height))
	key += chr(r)+chr(g)+chr(b)
	
print key