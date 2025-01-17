import os
from flask import Flask, render_template, request
import joblib
import pandas as pd
import re

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

app = Flask(__name__)

# Load the model and vectorizer
model = joblib.load('sport_model.pkl')
vectorizer = joblib.load('sport_vectorizer.pkl')

# Preprocessing function
stop_words = set(stopwords.words('english'))
stemmer = SnowballStemmer('english')

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[0-9]', '', text)
    text = ' '.join([word for word in text.split() if word not in stop_words and len(word) > 1])
    text = re.sub(r'\s+', ' ', text).strip()
    text = ' '.join([stemmer.stem(word) for word in text.split()])
    return text

label_map_reverse = {0: 'football', 1: 'rugby', 2: 'cricket', 3: 'athletics', 4: 'tennis'}

def predict_sport_category(text):
    processed_text = preprocess_text(text)
    text_series = pd.Series([processed_text])
    text_vectorized = vectorizer.transform(text_series)
    prediction = model.predict(text_vectorized)[0]
    predicted_sport = label_map_reverse[prediction]
    return predicted_sport

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        news_text = request.form['news']
        prediction = predict_sport_category(news_text)
        return render_template('index.html', prediction=prediction, news=news_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("8080"), debug=True)