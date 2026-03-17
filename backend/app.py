from flask import Flask, request, jsonify
from flask_cors import CORS
from model_loader import ModelLoader
import os

app = Flask(__name__)
# Enable CORS so frontend can communicate with backend
CORS(app)

# Initialize the model loader
model_loader = ModelLoader()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    if not data or 'note' not in data:
        return jsonify({'error': 'No medical note provided'}), 400
    
    medical_note = data['note']
    
    if not medical_note.strip():
        return jsonify({'error': 'Medical note is empty'}), 400
    
    try:
        prediction = model_loader.predict(medical_note)
        return jsonify({
            'note': medical_note,
            'prediction': prediction
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'Backend is running'})

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True, port=5000)
