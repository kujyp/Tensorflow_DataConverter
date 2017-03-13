# -*- coding: utf-8 -*-
from PIL import Image
import librosa
from .dir_loader import load_allpath
from .label_loader import load_alllabel
from .snd_converter import convert_snd_to_mfcc


snd_label_map = {
    '가': 0,
    '나': 1,
    '다': 2,
    '라': 3,
    '마': 4,
    '바': 5,
    '사': 6,
    '아': 7,
    '자': 8,
    '차': 9,
    '카': 10,
    '타': 11,
    '파': 12,
    '하': 13,
    '무음': 14,
}

def load_snd_mfcc_data(root):
    paths = load_allpath(root)
    return convert_snd_to_mfcc(load_allsnd(paths)), load_alllabel(paths, snd_label_map)

def load_snd(path):
    y, sr = librosa.core.load(path)
    return y, sr

def load_allsnd(paths):
    res = []

    for path in paths:
        res.append(load_snd(path))

    return res

