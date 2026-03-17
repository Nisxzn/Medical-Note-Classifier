document.addEventListener('DOMContentLoaded', () => {
    const noteInput = document.getElementById('medical-note');
    const predictBtn = document.getElementById('predict-btn');
    const resultContainer = document.getElementById('result-container');
    const predictionResult = document.getElementById('prediction-result');
    const errorBox = document.getElementById('error-box');
    const spinner = document.getElementById('spinner');
    const btnText = predictBtn.querySelector('.btn-text');

    const API_URL = 'http://127.0.0.1:5000/predict';

    predictBtn.addEventListener('click', async () => {
        const note = noteInput.value.trim();

        if (!note) {
            showError('Please enter a medical note.');
            return;
        }

        // Reset UI
        hideError();
        resultContainer.style.display = 'none';
        setLoading(true);

        try {
            const response = await fetch(API_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ note: note }),
            });

            const data = await response.json();

            if (response.ok) {
                predictionResult.textContent = data.prediction;
                resultContainer.style.display = 'block';
                // Scroll to result on mobile
                resultContainer.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
            } else {
                showError(data.error || 'Failed to get prediction from server.');
            }
        } catch (error) {
            console.error('Error:', error);
            showError('Could not connect to the backend server. Make sure the Flask app is running.');
        } finally {
            setLoading(false);
        }
    });

    function setLoading(isLoading) {
        if (isLoading) {
            predictBtn.disabled = true;
            spinner.style.display = 'block';
            btnText.style.opacity = '0';
        } else {
            predictBtn.disabled = false;
            spinner.style.display = 'none';
            btnText.style.opacity = '1';
        }
    }

    function showError(message) {
        errorBox.textContent = message;
        errorBox.style.display = 'block';
    }

    function hideError() {
        errorBox.textContent = '';
        errorBox.style.display = 'none';
    }
});
