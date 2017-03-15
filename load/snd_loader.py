# -*- coding: euc-kr -*-
import librosa
from .dir_loader import load_allpath
from .label_loader import load_alllabel
from .snd_converter import convert_snd_to_mfcc
from ..process.preprocess_audio import crop_sounds

snd_label_map = {
    'ga': 0,
    'na': 1,
    'da': 2,
    'ra': 3,
    'ma': 4,
    'ba': 5,
    'sa': 6,
    'aa': 7,
    'ja': 8,
    'cha': 9,
    'ka': 10,
    'ta': 11,
    'pa': 12,
    'ha': 13,
    'none': 14,
}

def load_snd_mfcc_data(root):
    paths = load_allpath(root)

    ys, srs = load_allsnd(paths)
    dur = 1.0
    ys = crop_sounds(ys, srs, dur)
    return convert_snd_to_mfcc(ys, srs), load_alllabel(paths, snd_label_map)

def load_snd(path):
    y, sr = librosa.core.load(path)
    return y, sr

def load_allsnd_data(root):
    paths = load_allpath(root)
    return load_allsnd(paths)

def load_allsnd(paths):
    ys, srs = [], []

    for path in paths:
        y, sr = load_snd(path)
        ys.append(y)
        srs.append(sr)

    return ys, srs

