from PIL import Image
from .dir_loader import load_allpath
from .label_loader import load_alllabel


img_label_map = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    }

def load_img_data(root):
    paths = load_allpath(root)
    return load_allimage(paths), load_alllabel(paths, img_label_map)

def load_image(path):
    return Image.open(path)

def load_allimage(paths):
    res = []

    for path in paths:
        res.append(load_image(path))

    return res

