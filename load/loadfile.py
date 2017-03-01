from PIL import Image
from loaddir import load_allpath


def load_image(path):
    return Image.open(path)

def load_allimage(root):
    paths = load_allpath(root)
    res = []

    for path in paths:
        res.append(load_image(path))

    return res