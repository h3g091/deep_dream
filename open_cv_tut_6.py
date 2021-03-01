import numpy as np 
import cv2

img = cv2.imread('test_4.jpg')
#img = cv2.imread('test_3.jpg')
img[40:80, 60:90] = [255,255,255]
retval, threshold = cv2.threshold(img, 37 , 255, cv2.THRESH_BINARY)

grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#retval2, threshold2 = cv2.threshold(grayscaled, 37 , 255, cv2.THRESH_BINARY)

#cv2.imshow('gray', grayscaled)
#bayesian adaptive threshold
gaus_sd_array = np.arange(3,103, 4)

#gaus_sd_array = np.array([11,31,51,71,91])
iteration = -1
new_picname= '/Users/heiko.langer/grayscaled/gray_'+str(iteration+1).zfill(3)+'.jpg'
cv2.imwrite(new_picname,grayscaled)
for value in gaus_sd_array:
	gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
	cv2.THRESH_BINARY,value,1)
	#name = 'value' + str(value)
	new_picname= '/Users/heiko.langer/grayscaled/gray_'+str(iteration+1).zfill(3)+'.jpg'
	cv2.imwrite(new_picname,gaus)
	
	iteration +=1
	#cv2.imshow(name, gaus)

#gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#	cv2.THRESH_BINARY,115,1)
#gaus2 = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,1)

#cv2.imshow('original', img)
#cv2.imshow('threshold', threshold)
#cv2.imshow('threshold2', threshold2)
#cv2.imshow('gaus', gaus)
#cv2.imshow('double_sd', gaus2)
#cv2.waitKey(0)
#cv2.destroyAllWindows()