import pickle
import os

class ModelLoader:
    def __init__(self):
        self.model_dir = os.path.join(os.path.dirname(__file__), '..', 'model')
        self.classifier_path = os.path.join(self.model_dir, 'classifier.pkl')
        self.vectorizer_path = os.path.join(self.model_dir, 'vectorizer.pkl')
        self.classifier = None
        self.vectorizer = None
        self.load_model()

    def load_model(self):
        try:
            if os.path.exists(self.classifier_path) and os.path.exists(self.vectorizer_path):
                with open(self.classifier_path, 'rb') as f:
                    self.classifier = pickle.load(f)
                with open(self.vectorizer_path, 'rb') as f:
                    self.vectorizer = pickle.load(f)
                print("Model and Vectorizer loaded successfully.")
            else:
                print("Model files not found. Please run train_model.py first.")
        except Exception as e:
            print(f"Error loading model: {e}")

    def predict(self, text):
        if self.classifier is None or self.vectorizer is None:
            return "Model not loaded"
        
        # Vectorize the input text
        vectorized_text = self.vectorizer.transform([text])
        
        # Predict the disease
        prediction = self.classifier.predict(vectorized_text)
        return prediction[0]
