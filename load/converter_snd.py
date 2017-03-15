import numpy


def convert_sound_data_to_numpy(sounds, labels):
    sounds = convert_sounds_to_numpy(sounds)
    labels = convert_labels_to_numpy(labels)
    return sounds, labels

def convert_labels_to_numpy(labels):
    np_labels = numpy.array(labels, dtype=int)

    return np_labels

def convert_sounds_to_numpy(sounds):
    arr = numpy.empty([len(sounds), sounds[0].shape[0], sounds[0].shape[1]], dtype=float)
    for idx, sound in enumerate(sounds):
        arr[idx][:][:] = sound
    return arr
