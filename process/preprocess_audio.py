def crop_sounds(sounds, srs, dur):
    cropped = []
    for idx, snd in enumerate(sounds):
        cropped.append(crop_sound(snd, srs[idx], dur))

    return cropped

def crop_sound(y, sr, dur):
    dur_idx = int(dur*sr)
    return y[-dur_idx:]