import librosa


def convert_snd_to_mfcc(ys, srs):
    mfccs = []
    n_mfcc = 40
    for idx, y in enumerate(ys):
        mfcc = librosa.feature.mfcc(y=y, sr=srs[idx], n_mfcc=n_mfcc)
        mfcc = mfcc[:,:n_mfcc]
        mfccs.append(mfcc)

    return mfccs