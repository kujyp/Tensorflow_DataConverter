from load.loadfile import load_allimage
from visualize.visualizer_pillow import smallest_size, average_size
from process.normalizer_pillow import normalize_images

rootdir = "data"
images = load_allimage(rootdir)
#print(len(images))
#print(smallest_size(images))
#print(average_size(images))
images = normalize_images(images)
#images = convert_images_to_numpy(images)