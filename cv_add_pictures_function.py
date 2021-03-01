import cv2
import numpy as np 
import os
save_folder = '/Users/heiko.langer/grayscaled/morphed_dream/'
image_folder ='/Users/heiko.langer/deep_dream_fun/all_pictures/'
#image_folder = '/Users/heiko.langer/grayscaled/'

#pic_1 = cv2.imread('/Users/heiko.langer/grayscaled/gray_000.jpg')
#pic_2 = cv2.imread('/Users/heiko.langer/grayscaled/gray_024.jpg')
images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]

images= sorted(images)
#pic_1 = cv2.imread(image_folder+images[0])
#pic_2 = cv2.imread(image_folder+images[2])

print(len(images))
def add_pictures_with_transparency_steps_between_pictures(pic1, pic2,steps, save_directory, picture_iterator):
	for iteration in range(steps):
		transparency_value= (iteration)/(steps+1)
		#new_picname = directory+'gray_morph_'+str(iteration+1).zfill(3)+'.jpg'
		new_picname = save_directory+'gray_morph_'+ str(picture_iterator).zfill(3)+str(iteration+1).zfill(3)+'.jpg'
		img_combine_1 = cv2.addWeighted(pic1, 1-transparency_value, pic2, transparency_value, 0)
		cv2.imwrite(new_picname,img_combine_1)

#add_pictures_with_transparency_steps_between_pictures(pic_1,pic_2, steps=10, save_directory= save_folder)
for i in range(len(images)-1):
#for i in range(25):
	pic_1 = cv2.imread(image_folder+images[i])
	pic_2 = cv2.imread(image_folder+images[i+1])
	add_pictures_with_transparency_steps_between_pictures(pic_1,pic_2, steps=10, save_directory= save_folder, picture_iterator= i)
