import numpy as np
import cv2
img = cv2.imread('test.jpg', cv2.IMREAD_COLOR)


cv2.line(img, (0,0), (150,460), (255,255,0), 15)
cv2.rectangle(img,(15,25), (200,150), (0,0,0),15)
cv2.circle(img,(400,250), 55,  (0,0,0), -1)
pts = np.array([[10,5], [20,30], [70,20], [30,600], [400,90]], np.int32)

cv2.polylines(img, [pts], True, (0,255,255), 3)


font = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(img, 'OpenCV tut!',(250,250), font, 1, (0,0,120), 5, cv2.LINE_AA)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()