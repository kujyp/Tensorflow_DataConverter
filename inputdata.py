from .load.classifier import shuffle_numpy_together
from .load.img_loader import load_img_data
from .load.snd_loader import load_snd_mfcc_data
from .load.converter_img import convert_data_to_numpy
from .process.normalizer_pillow import normalize_images
from .process.normalizer_numpy import normalize_numpy
from .visualize.visualizer_numpy import show_nbyn_images
from .object.dataset import DataSet, Datasets
from .process.preprocess_audio import crop_sounds


def input_image_data(root):
    images, labels = load_img_data(root)
    images = normalize_images(images)
    images, labels = convert_data_to_numpy(images, labels)
    print("Load success : " + str(images.shape))
    #show_nbyn_images(images)

    images, labels = shuffle_numpy_together(images, labels)
    return images, labels


def read_image_datasets(train_dir,
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

def input_snd_mfcc_data(root):
    mfccs, labels = load_snd_mfcc_data(root)
    mfccs, labels = convert_data_to_numpy(mfccs, labels)
    mfccs = normalize_numpy(mfccs)
    print("Load success : " + str(mfccs.shape))
    #show_nbyn_images(images)

    mfccs, labels = shuffle_numpy_together(mfccs, labels)
    return mfccs, labels

def read_sound_datasets(train_dir, test_dir,
                   reshape=True):
    train_images, train_labels = input_snd_mfcc_data(train_dir)
    test_images, test_labels = input_snd_mfcc_data(test_dir)

    train = DataSet(train_images,
                    train_labels,
                    reshape=reshape)
    test = DataSet(test_images,
                   test_labels,
                   reshape=reshape)

    return Datasets(train=train, test=test)