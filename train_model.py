import pandas as pd
import pickle
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

def train_model():
    # Define paths
    dataset_path = os.path.join('dataset', 'medical_notes.csv')
    model_dir = 'model'
    classifier_path = os.path.join(model_dir, 'classifier.pkl')
    vectorizer_path = os.path.join(model_dir, 'vectorizer.pkl')

    # Create model directory if it doesn't exist
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    # Load dataset
    print("Loading dataset...")
    df = pd.read_csv(dataset_path)

    # Simple exploration
    print(f"Dataset size: {len(df)} samples")
    print(f"Categories: {df['disease'].unique()}")

    # Initialize TF-IDF Vectorizer
    print("Vectorizing text...")
    vectorizer = TfidfVectorizer(stop_words='english', lowercase=True)
    
    # Transform text data
    X = vectorizer.fit_transform(df['note'])
    y = df['disease']

    # Initialize and train Logistic Regression model
    print("Training Logistic Regression model...")
    classifier = LogisticRegression(random_state=42, max_iter=1000)
    classifier.fit(X, y)

    # Save the vectorizer and classifier
    print("Saving model and vectorizer...")
    with open(classifier_path, 'wb') as f:
        pickle.dump(classifier, f)
    
    with open(vectorizer_path, 'wb') as f:
        pickle.dump(vectorizer, f)

    print("Training complete! Files saved in 'model/' directory.")

if __name__ == "__main__":
    train_model()
