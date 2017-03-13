from .dir_loader import get_folder_name


def load_label(path, map):
    return map[get_folder_name(path)]

def load_alllabel(paths, map):
    res = []

    for path in paths:
        res.append(load_label(path, map))

    return res