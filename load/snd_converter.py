import librosa


def convert_snd_to_mfcc(sounds):
    mfccs = []
    for sound in sounds:
        y = sound[0]
        sr = sound[1]
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
        mfccs.append(mfcc)

    return mfccs