from .load.classifier import shuffle_numpy_together
from .load.img_loader import load_img_data
from .load.converter_img import convert_data_to_numpy
from .process.normalizer_pillow import normalize_images
from .object.dataset import DataSet, Datasets
from .visualize.visualizer_numpy import show_nbyn_images


def input_image_data(root):
    images, labels = load_img_data(root)
    images = normalize_images(images)
    images, labels = convert_data_to_numpy(images, labels)
    print("Load success : " + str(images.shape))
    #show_nbyn_images(images)

    images, labels = shuffle_numpy_together(images, labels)
    return images, labels


def read_image_datasets(train_dir, test_dir,
                   reshape=True):
    train_images, train_labels = input_image_data(train_dir)
    test_images, test_labels = input_image_data(test_dir)

    train = DataSet(train_images,
                    train_labels,
                    reshape=reshape)
    test = DataSet(test_images,
                   test_labels,
                   reshape=reshape)

    return Datasets(train=train, test=test)