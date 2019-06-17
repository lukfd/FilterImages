#Luca Comba and Evan Hanson, CISC 131 Week 10 Lab - Problem 1
from PIL import Image
import sys
import argparse

def Main():

	#Parse cmd line arg
	
	parser = argparse.ArgumentParser()
	parser.add_argument('-g', '--gray', action="store_true", dest="gray", default=False, help='convert to gray scale image')
	parser.add_argument('-i', '--invert', action="store_true", dest="invert", default=False, help='invert image colors (create image negative)')
	parser.add_argument('-m', '--mono', action="store", dest="COLOR", type=str, default="...", help='convert to a monochromatic image with only specified color')
	parser.add_argument("image", default="...", nargs=1)	
	
	user_args = parser.parse_args(sys.argv[1:])
	
	# read image from file
	file = user_args.image[0] # can also be .png
	img = Image.open(file)

	# get resolution of image
	width, height = img.size

	# extract pixels from image as a list of lists (each element is a pixel, and each pixel is R,G,B colors)
	pixels = list(map(list, img.getdata()))

	#modify green red blue values
	GrayScale(pixels, width, height, user_args.gray)
	Invert(pixels, width, height, user_args.gray, user_args.invert)
	Mono(pixels, width, height, user_args.gray, user_args.invert, user_args.COLOR)
	# store pixel values back in image
	img.putdata(list(map(tuple, pixels)))

	# save new image to a file
	img.save("Final.bmp") # MUST be .bmp


def Invert(pixels, width, height, gray, invert):
	if invert == True:
		if gray == True:
			grayscale = GrayScale(pixels, width, height, gray)
			for i in range(len(grayscale)):
				for j in range(len(grayscale[i])):
					for k in range(len(grayscale[i][j])):
						grayscale[i][j][k] = 255 - grayscale[i][j][k]
			return grayscale
		if gray != True:
			colorpixels=[]
			colorpixels.append(pixels)
			for i in range(len(colorpixels)):
				for j in range(len(colorpixels[i])):
					for k in range(len(colorpixels[i][j])):
						colorpixels[i][j][k] = 255 - colorpixels[i][j][k]
			return colorpixels
				

def Mono(pixels, width, height, gray, invert, mono):
	if mono != "...":
		colorpixels = HexToColor(mono)
		if gray == True:
			graypixels = GrayScale(pixels, width, height, gray)
			for i in range(len(graypixels)):
				for j in range(len(graypixels[i])):
					for k in range(len(graypixels[i][j])):
						graypixels[i][j][k] = int(((graypixels[i][j][k])/255) * colorpixels[k])
			return graypixels
		if gray != True:
			monopixels=[]
			monopixels.append(pixels)
			for i in range(len(monopixels)):
				for j in range(len(monopixels[i])):
					#average = ((monopixels[i][j][0] + monopixels[i][j][1] + monopixels[i][j][2]) / 3)
					for k in range(len(monopixels[i][j])):
						#x = (average//255)
						#monopixels[i][j][k] = average//255
						#monopixels = monopixels[i][j][k] * (average//255) * colorpixels[k]
						monopixels[i][j][k] = int(((monopixels[i][j][0] + monopixels[i][j][1] + monopixels[i][j][2]) / 3)/255 * colorpixels[k])
			return monopixels
	
def GrayScale(pixels, width, height, gray):
	if gray == True:
		graypixels=[]
		graypixels.append(pixels)
		for i in range(len(graypixels)):
			for j in range(len(graypixels[i])):
				average = int((graypixels[i][j][0] + graypixels[i][j][1] + graypixels[i][j][2]) / 3)
				for k in range(len(graypixels[i][j])):
					graypixels[i][j][k] = average
		return graypixels

def HexToColor(hexstr):
	hexstr = hexstr.upper()
	new_list = []
	x = 0
	for i in range(1,3):
		if ord(hexstr[i]) <= 57 and ord(hexstr[i]) >= 48:
			if i == 1:
				x = x + (ord(hexstr[i]) - 48 )* 16
			if i == 2:
				x = x + ord(hexstr[i]) - 48
		else:
			if i == 1:
				x = x + (ord(hexstr[i]) - 55) * 16
			if i == 2:
				x = x + ord(hexstr[i]) - 55
	new_list.append(x)
	x = 0
	for i in range(3,5):
		if ord(hexstr[i]) <= 57 and ord(hexstr[i]) >= 48:
			if i == 3:
				x = x + (ord(hexstr[i]) - 48 )* 16
			if i == 4:
				x = x + ord(hexstr[i]) - 48
		else:
			if i == 3:
				x = x + (ord(hexstr[i]) - 55) * 16
			if i == 4:
				x = x + ord(hexstr[i]) - 55
	new_list.append(x)
	x=0
	for i in range(5,7):
		if ord(hexstr[i]) <= 57 and ord(hexstr[i]) <= 48:
			if i == 5:
				x = x + (ord(hexstr[i]) - 48 )* 16
			if i == 6:
				x = x + ord(hexstr[i]) - 48
		else:
			if i == 5:
				x = x + (ord(hexstr[i]) - 55) * 16
			if i == 6:
				x = x + ord(hexstr[i]) - 55
	new_list.append(x)
	return new_list

Main()