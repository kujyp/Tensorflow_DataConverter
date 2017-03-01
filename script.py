from load.loadfile import load_allimage
from visualize.visualize_pillow import smallest_size, average_size

rootdir = "data"
images = load_allimage(rootdir)
print(len(images))
print(smallest_size(images))
print(average_size(images))

#images = normalize(images)
#images = convert_images_to_numpy(images)

