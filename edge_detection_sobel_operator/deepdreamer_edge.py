#deepdreamer_edge
from deepdreamer import model, load_image, recursive_optimize
import numpy as np
import PIL.Image
import timeit
import cv2 as cv


start = timeit.default_timer()

#Your statements here

layer_tensor = model.layer_tensors[3]
#for iteration in range(10):
    #iteration=0
file_name = "test.png"
#file_name = "the-starry-night/the-starry-night-800x450.jpg"
img = load_image(filename='{}'.format(file_name))
#layer_tensor = model.layer_tensors[iteration]


img_result = recursive_optimize(layer_tensor=layer_tensor, image=img,
                 # how clear is the dream vs original image
                 num_iterations=100, step_size=0.1, rescale_factor=0.5,
                                #num_iterations=20, step_size=1.0, rescale_factor=0.5,
                 # How many "passes" over the data. More passes, the more granular the gradients will be.
                 num_repeats=8, blend=0.2)

img_result = np.clip(img_result, 0.0, 255.0)
img_result = img_result.astype(np.uint8)
result = PIL.Image.fromarray(img_result, mode='RGB')

result.save('picture_dream.jpg')
#    result.show()


img = cv.imread('picture_dream.jpg')
    
    
    
stop = timeit.default_timer()
print('Time: ', stop - start)  