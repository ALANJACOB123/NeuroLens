# Flask server for LMS Integration

from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load('models/trained_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = data['features']
    prediction = model.predict([features])[0]
    return jsonify({'state': prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
