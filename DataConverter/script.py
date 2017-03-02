from load.loadfile import load_data
from load.converter import convert_data_to_numpy
from process.normalizer_pillow import normalize_images
from visualize.visualizer_numpy import show_nbyn_images


rootdir = "data"
images, labels = load_data(rootdir)
images = normalize_images(images)
images, labels = convert_data_to_numpy(images, labels)
print("Load success : " + str(images.shape))
#show_nbyn_images(images)

from DataConverter import inputdata
datasets = inputdata.read_datasets(rootdir)
show_nbyn_images(datasets.train.images)
show_nbyn_images(datasets.test.images)