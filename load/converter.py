import numpy


def convert_images_to_numpy(images):
    arr = numpy.empty([len(images), 48, 28], dtype=float)
    for idx, image in enumerate(images):
        arr[idx][:][:] = convert_image_to_numpy(image)
    return arr

def convert_image_to_numpy(image):
    np_image = numpy.array(image, dtype=float)
    np_image = normalize_if_its_integer(np_image)
    return np_image

def normalize_if_its_integer(image):
    if (image > 1).any() :
        image = image / 255
    return image