import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('test.png')
img_dreamed = cv.imread('picture_dreamed.jpg')
#logo = cv.imread('test.png')
grayscaled = cv.cvtColor(img_dreamed, cv.COLOR_BGR2GRAY)
#edges_high = cv.Canny(img,100,120)
edges = cv.Canny(img_dreamed,10,110)
ret, mask, = cv.threshold(edges, 102,255, cv.THRESH_BINARY_INV)
mask_inv = cv.bitwise_not(mask)



src1_mask=cv.cvtColor(mask,cv.COLOR_GRAY2BGR)#change mask to a 3 channel image 
mask_out1=cv.subtract(src1_mask,img_dreamed)
mask_out=cv.subtract(src1_mask,mask_out1)


img2=cv.bitwise_and(img,img,mask= mask_inv)




#img3 = img[mask_inv]

#edges = cv.Canny(img,100,140)
#edges_high = cv.Canny(img,60,80)
#edges_low = cv.Canny(img,40,60)
#cv.imshow('grayscaled', grayscaled)
#cv.imshow('edges', edges)
#cv.imshow('edges_high', edges_high)
#cv.imshow('mask', mask)
cv.imshow('img_dreamed', img_dreamed)
#cv.imshow('img', img)
cv.imshow('img2', img2)
#cv.imshow('mask_out1', mask_out1)
#cv.imshow('mask_out', mask_out)


#cv.imwrite("edges_new.jpg",mask_out)
#cv.imshow('edges_low', edges_low)
cv.waitKey(0)
cv.destroyAllWindows()
#plt.subplot(121),plt.imshow(img,cmap = 'gray')
#plt.title('Original Image'), plt.xticks([]), plt.yticks([])
#plt.subplot(122),plt.imshow(edges,cmap = 'gray')
#plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
#plt.show()
