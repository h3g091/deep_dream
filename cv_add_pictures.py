import cv2 
import numpy as np


pic1 = cv2.imread('0dream_image_out.jpg')

pic2 = cv2.imread('19dream_image_out.jpg')
steps= 10
for iteration in range(steps):
	new_picname = '/Users/heiko.langer/deep_dream_fun/neue_pics/picture_'+str(iteration+1).zfill(3)+'.jpg'
	transparency_value= (iteration+1)/steps
	print(transparency_value)
	img_combine_1 = cv2.addWeighted(pic1, 1-transparency_value, pic2, transparency_value, 0)
	cv2.imwrite(new_picname,img_combine_1)

#cv2.imshow('0', pic1)
#cv2.imshow('1', pic2)
#cv2.imshow('res', img_combine_1)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

