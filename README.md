# Medical Note Classifier

A full-stack NLP application for academic purposes that classifies medical notes into disease categories using Machine Learning.

## Objective
The goal of this project is to demonstrate a simple end-to-end NLP pipeline. It takes raw medical text as input and uses a trained Logistic Regression model (with TF-IDF vectorization) to predict the likely disease category.

## System Architecture

1.  **Frontend**: Built with vanilla HTML, CSS, and JavaScript. It provides a clean, modern interface for users to enter medical notes and view results.
2.  **Backend**: A Flask (Python) API that serves prediction requests.
3.  **Machine Learning**: 
    - **Vectorization**: TF-IDF (Term Frequency-Inverse Document Frequency) to convert text into numerical features.
    - **Model**: Logistic Regression classifier trained on a curated dataset.
    - **Persistence**: Model and vectorizer are saved as `.pkl` files using Python's `pickle` module.

## Project Structure
```
medical-note-classifier/
├── backend/
│   ├── app.py              # Flask API entry point
│   └── model_loader.py     # Class to handle model loading/prediction
├── frontend/
│   ├── index.html          # Web interface
│   ├── style.css           # Styling
│   └── script.js           # Frontend logic & API calls
├── dataset/
│   └── medical_notes.csv   # Training data
├── model/
│   ├── classifier.pkl      # Saved Logistic Regression model
│   └── vectorizer.pkl      # Saved TF-IDF vectorizer
├── train_model.py          # Script to train and save the model
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## Dataset Description
The model is trained on `dataset/medical_notes.csv`, which contains two columns:
- `note`: Short text descriptions of patient symptoms or history.
- `disease`: The corresponding category label.

**Example Categories**:
- Diabetes
- Heart Disease
- Respiratory Infection
- Hypertension

## Steps to Run the Project

### 1. Set up Python Environment
It is recommended to use a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Train the Model
Run the training script to generate the model files:
```bash
python train_model.py
```
This will create the `model/` directory with `classifier.pkl` and `vectorizer.pkl`.

### 3. Start the Backend
Navigate to the root and run:
```bash
python backend/app.py
```
The server will start at `http://localhost:5000`.

### 4. Run the Frontend
Open `frontend/index.html` in any web browser.

## Example Input and Output

**Input**: 
> "Patient reports increased thirst, frequent urination, and unexplained weight loss. Fasting blood sugar level is elevated."

**Output**: 
> **Diabetes**

---
*Created for academic assignment purposes.*
