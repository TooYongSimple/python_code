from PIL import Image, ImageDraw, ImageFont, ImageColor

def add_num(img):
	draw = ImageDraw.Draw(img)
	myfont = ImageFont.truetype('/Users/zhangjianyun/Documents/ios_code/swift/project/firefox-ios-master/Client/Assets/Fonts/CharisSILB.ttf', size = 40)
	fillcolor = ImageColor.colormap.get('red')
	width, height = img.size
	draw.text((width-30, 0), '1', font = myfont, fill = fillcolor)
	img.save('result.jpg', 'jpeg')
	return 0

def ():
	pass

if __name__ == '__main__':
	image = Image.open('22.jpg')
	add_num(image)
