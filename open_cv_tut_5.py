import 	cv2
import numpy as np 
img1 = cv2.imread('test.jpg')
img2 = cv2.imread('test_2.jpg')
logo = cv2.imread('test_3.jpg')
height, width, channels = img1.shape
height1, width2, channels3 = img2.shape

#print(height1,width2,channels3)
#print(height,width,channels)

rows,cols,channels = logo.shape

roi = img1[0:rows, 0:cols]

logo2gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
ret,mask = cv2.threshold(logo2gray,80, 255, cv2.THRESH_BINARY_INV) # threshold everything bigger than 80 is converted to 255 (white)

#cv2.imshow('mask',mask)
mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi,roi, mask= mask_inv)
img2_fg = cv2.bitwise_and(logo,logo, mask=mask)
dst= cv2.add(img1_bg, img2_fg)

img1[0:rows, 0:cols] = dst


cv2.imshow('mask_inv', mask_inv)
cv2.imshow('img1_bg', img1_bg)
cv2.imshow('img2_fg', img2_fg)
cv2.imshow('dst', dst)
cv2.imshow('results', img1)
#add = img1 + img2
#cv2.imshow('both', add)
#add1 = cv2.add(img1, img2)
#weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0) ## for my project


#cv2.imshow('lala',weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()