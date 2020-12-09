from deepdreamer import model, load_image, recursive_optimize
import numpy as np
import PIL.Image

layer_tensor = model.layer_tensors[3]
file_name = "/Users/heiko.langer/deep_dream_fun/IMG_0960.jpeg"
#file_name = "the-starry-night/the-starry-night-800x450.jpg"
img = load_image(filename='{}'.format(file_name))
for iteration in range(20):
    #layer_tensor = model.layer_tensors[iteration]
    
    
    img_result = recursive_optimize(layer_tensor=layer_tensor, image=img,
                     # how clear is the dream vs original image
                     num_iterations=iteration+1, step_size=1.0, rescale_factor=0.5,
                                    #num_iterations=20, step_size=1.0, rescale_factor=0.5,
                     # How many "passes" over the data. More passes, the more granular the gradients will be.
                     num_repeats=8, blend=0.2)
    
    img_result = np.clip(img_result, 0.0, 255.0)
    img_result = img_result.astype(np.uint8)
    result = PIL.Image.fromarray(img_result, mode='RGB')
  
    result.save(str(iteration)+'dream_image_out.jpg')
    result.show()

