# Preprocess EEG data

import mne
import numpy as np

def preprocess_eeg(raw_data, sfreq=256):
    info = mne.create_info(['TP9','AF7','AF8','TP10'], sfreq=sfreq, ch_types='eeg')
    raw = mne.io.RawArray(raw_data, info)
    raw.filter(1., 40., fir_design='firwin')
    ica = mne.preprocessing.ICA(n_components=4, random_state=42)
    ica.fit(raw)
    clean_raw = ica.apply(raw)
    return clean_raw
