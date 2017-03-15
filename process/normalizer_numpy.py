import numpy as np


def normalize_numpy(ndarr):
    ndarr = (ndarr - np.min(ndarr))
    ndarr = ndarr / np.max(ndarr)
    return ndarr