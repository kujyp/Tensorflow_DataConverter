from .load.snd_loader import load_snd_mfcc_data
from .load.converter_snd import convert_sound_data_to_numpy
from .process.normalizer_numpy import normalize_numpy
from .load.classifier import shuffle_numpy_together
from .object.dataset import DataSet, Datasets


def input_snd_mfcc_data(root):
    mfccs, labels = load_snd_mfcc_data(root)
    mfccs, labels = convert_sound_data_to_numpy(mfccs, labels)
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