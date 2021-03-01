import numpy as np
import cv2

img = cv2.imread('test.jpg', cv2.IMREAD_COLOR)
### switch to grayscale

px = img[55,55] # value of location

img[55,55]= [255,255,255]
px = img[55,55]
print(px)

#ROI = Region of Image specifiy an region of the image

roi = img[100:150, 100:150]
#print(roi)
img[100:150, 100:150] = [255,255,255]

x1= 37
x2 = 294
x_diff = x1-x2
y1 = 107
y2 = 444
y_diff = y2-y1

#watch_face = img[x1:x2, y1:y2]
watch_face = img[250:460, 250:450]
img[0:210, 0:200] = watch_face

cv2.imshow('lalelutitle', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
