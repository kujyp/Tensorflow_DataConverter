from .load.classifier import shuffle_numpy_together
from .load.img_loader import load_img_data
from .load.snd_loader import load_snd_mfcc_data
from .load.img_converter import convert_data_to_numpy
from .process.normalizer_pillow import normalize_images
from .visualize.visualizer_numpy import show_nbyn_images
from .object.dataset import DataSet, Datasets


def input_image_data(root):
    images, labels = load_img_data(root)
    images = normalize_images(images)
    images, labels = convert_data_to_numpy(images, labels)
    print("Load success : " + str(images.shape))
    #show_nbyn_images(images)

    images, labels = shuffle_numpy_together(images, labels)
    return images, labels

def input_snd_mfcc_data(root):
    sounds, labels = load_snd_mfcc_data(root)
    sounds = normalize_images(sounds)
    sounds, labels = convert_data_to_numpy(sounds, labels)
    print("Load success : " + str(sounds.shape))
    #show_nbyn_images(images)

    sounds, labels = shuffle_numpy_together(sounds, labels)
    return sounds, labels

def read_datasets(train_dir,
                   reshape=True,
                   validation_size=100):
    train_images, train_labels = input_image_data(train_dir)

    if not 0 <= validation_size <= len(train_images):
        raise ValueError(
            'Validation size should be between 0 and {}. Received: {}.'
                .format(len(train_images), validation_size))
    test_images = train_images[:validation_size]
    test_labels = train_labels[:validation_size]
    train_images = train_images[validation_size:]
    train_labels = train_labels[validation_size:]

    train = DataSet(train_images, train_labels, reshape=reshape)
    test = DataSet(test_images,
                   test_labels,
                   reshape=reshape)

    return Datasets(train=train, test=test)