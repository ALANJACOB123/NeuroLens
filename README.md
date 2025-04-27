# NeuroLens

Brainwave-Based Adaptive Learning System using non-invasive EEG and Machine Learning.

## Structure

- eeg_acquisition: EEG data streaming
- preprocessing: Signal cleaning
- feature_extraction: PSD & entropy
- models: Training & saving classifier
- lms_integration: Flask API
- calibration: User calibration routines
- extension: VSCode inline extension
- docs: Documentation & diagrams

## Setup

```bash
pip install -r requirements.txt
python models/train_classifier.py
python lms_integration/api_server.py
```
