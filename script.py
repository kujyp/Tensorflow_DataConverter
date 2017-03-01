from load.loadfile import load_allimage
from load.converter import convert_images_to_numpy
from process.normalizer_pillow import normalize_images
from visualize.visualizer_numpy import show_nbyn_images


rootdir = "data"
images = load_allimage(rootdir)
#from visualize.visualizer_pillow import smallest_size, average_size
#print(len(images))
#print(smallest_size(images))
#print(average_size(images))
images = normalize_images(images)
images = convert_images_to_numpy(images)
print(images.shape)
#images = convert_numpy_int_to_float(images)

show_nbyn_images(images, 10)