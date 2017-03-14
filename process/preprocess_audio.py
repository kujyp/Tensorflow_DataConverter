def crop_sounds(sounds, srs, dur):
    cropped = []
    for idx, snd in enumerate(sounds):
        cropped.append(crop_sound(snd, srs[idx], dur))

    return cropped

def crop_sound(y, sr, dur):
    st = dur[0]
    ed = dur[1]

    st_idx = int(st*sr)
    ed_idx = int(ed*sr)
    return y[st_idx:ed_idx]