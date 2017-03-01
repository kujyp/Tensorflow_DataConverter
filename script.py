from load.loadfile import load_allimage
from load.converter import convert_images_to_numpy
from process.normalizer_pillow import normalize_images
from visualize.visualizer_numpy import show_nbyn_images


rootdir = "data"
images = load_allimage(rootdir)
images = normalize_images(images)
images = convert_images_to_numpy(images)
print("Load success : " + str(images.shape))
show_nbyn_images(images)