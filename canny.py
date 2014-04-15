''' file name : lander.py

Description: This shows how to detect a shape with contrasting color in an image for the purpose of detecting a landing platform for a Drone

Writen By: George W. Melcer

Website: www.GetTheGizmo.com

Contact: gmelcer@gmail.com

Based on Code by: Abid K. (abidrahman2@gmail.com) , Visit opencvpython.blogspot.com

License: GPL

This file is part of Lander.

    Lander is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Lander is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Lander.  If not, see <http://www.gnu.org/licenses/>.

'''


import cv2
import numpy as np

def boxer(image):
	boxValue = 0
	boxSize = 20
	boxSizeSqaured = boxSize *boxSize
	for dy in range(0, height-boxSize, boxSize):
		for dx in range(0, width-boxSize, boxSize): 
			for y in range(dy, dy+boxSize):
				for x in range(dx, dx+boxSize):
					boxValue = boxValue + image[y][x]
			boxValue = boxValue/(boxSizeSqaured)
			if boxValue < 230:
				for y2 in range(dy, dy+boxSize):
					for x2 in range(dx, dx + boxSize):
						image[y2][x2] = 0
	return image

def getMinMax(image):
	minx =100000
	miny =100000
	maxx = 0
	maxy = 0 
	for dy in range(0, height):
		for dx in range(0, width):
			if image[dy][dx] > 5:
				if dy < miny:
					miny = dy
				if dx < minx:
					minx = dx
				if dx > maxx:
					maxx = dx
				if dy > maxy:
					maxy = dy
	return maxx, maxy, minx, miny 
	
	
def CannyThreshold(lowThreshold):
    detected_edges = cv2.GaussianBlur(gray,(kernel_size,kernel_size),5)
    detected_edges = cv2.Canny(detected_edges,lowThreshold,lowThreshold*ratio,apertureSize = kernel_size)
    cv2.imshow('canny demo',detected_edges)

    dst = cv2.bitwise_and(tempgray,detected_edges)  # just add some colours to edges from original image.
    maxx, maxy, minx, miny = getMinMax(dst)
    cv2.line(img,(minx,miny),(minx,maxy),255,5) #left verticle edge
    cv2.line(img,(minx,miny),(maxx,maxy),255,5) #diagnol
    cv2.line(img,(minx,maxy),(maxx,maxy),255,5) #bottom  horizontal edge
    cv2.line(img,(maxx,miny),(maxx,maxy),255,5) #right  verticle edge
    cv2.line(img,(maxx,miny),(minx,miny),255,5) #right  verticle edge
    cv2.imshow('canny demo2',img)
    
    print maxx, maxy , minx, miny
	
	

def main():
	#init vars	
	lowThreshold = 0
	max_lowThreshold = 100
	ratio = 12
	kernel_size = 3


	#read in image from file
	img = cv2.imread('image1.jpg')


	#open windows that display image data at different stages					
	cv2.namedWindow('canny demo2')
	cv2.namedWindow('canny demo')



	cv2.imshow('e2',img)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	tempgray = gray
	height, width, depth = img.shape
	gray = boxer(gray)
	CannyThreshold(66)
	if cv2.waitKey(0)==27:
		cv2.destroyAllWindows()



main()

