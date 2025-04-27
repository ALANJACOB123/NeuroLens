# Extract features: PSD and entropy

import numpy as np
from scipy.signal import welch
from scipy.stats import entropy

def extract_features(epoch_data, sfreq=256):
    features = []
    for epoch in epoch_data:
        f, Pxx = welch(epoch, fs=sfreq, nperseg=sfreq)
        psd_bands = [np.mean(Pxx[(f>=low)&(f<high)]) for (low,high) in [(1,4),(4,8),(8,13),(13,30)]]
        ent = entropy(Pxx)
        features.append(psd_bands + [ent])
    return np.array(features)
