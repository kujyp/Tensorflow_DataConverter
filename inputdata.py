from load.loadfile import load_data
from load.converter import convert_data_to_numpy
from process.normalizer_pillow import normalize_images
from visualize.visualizer_numpy import show_nbyn_images


def inputdata(root):
    images, labels = load_data(root)
    images = normalize_images(images)
    images, labels = convert_data_to_numpy(images, labels)
    print("Load success : " + str(images.shape))
    #show_nbyn_images(images)

    return images, labels